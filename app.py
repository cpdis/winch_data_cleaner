from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file,
    flash,
    session,
)
import os
from werkzeug.utils import secure_filename
from combine_data import combine_data
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"txt"}

app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static", "uploads")


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file[]" not in request.files:
            flash("No file part", category="danger")
            return redirect(request.url)

        files = request.files.getlist("file[]")
        valid_files = []

        for file in files:
            if file.filename == "":
                flash("No selected file", category="danger")
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(file_path)
                valid_files.append(file_path)

        if not valid_files:
            flash("No valid files", category="danger")
            return redirect(request.url)

        winch_names = request.form.getlist("winch_name[]")
        line_number = request.form.get("line_number")
        operation_type = request.form.get("operation_type")

        output_file = f"line_{line_number}_{operation_type}.txt"
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], output_file)

        combined_data = combine_data(valid_files, winch_names, output_path)

        if combined_data:
            session["output_file"] = output_path
            flash("Files combined successfully.", category="success")
        else:
            session.pop("output_file", None)
            flash("Error combining files.", category="danger")

        return redirect(url_for("index"))

    output_file = session.get("output_file", None)
    return render_template("index.html", output_file=output_file)


@app.route("/download", methods=["GET"])
def download():
    output_file = session.get("output_file", None)
    if output_file and os.path.exists(output_file):
        return send_file(
            output_file,
            as_attachment=True,
            attachment_filename=os.path.basename(output_file),
        )
    else:
        flash("No output file available for download.", category="danger")
        return redirect(url_for("index"))


if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
