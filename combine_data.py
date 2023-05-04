import os
import tempfile
import shutil


def combine_data(input_files, winch_name, output_file):
    data = []
    timestamps = []

    for file in input_files:
        with open(file, "r") as infile:
            lines = infile.readlines()
            for line in lines:
                if line.startswith("COMMENT:"):
                    continue
                else:
                    line_data = line.strip().split(";")
                    if winch_name in line_data[2]:
                        timestamp = line_data[0].strip()
                        if timestamp not in timestamps:
                            timestamps.append(timestamp)
                            data.append(line)

    # Sort the data by timestamps
    data.sort(key=lambda x: timestamps.index(x.split(";")[0].strip()))

    # Write the sorted data to the output file
    with open(output_file, "w") as outfile:
        for line in data:
            outfile.write(line + "\n")

    return output_file


def process_uploaded_files(files, winch_name):
    input_files = []
    output_file = None

    with tempfile.TemporaryDirectory() as temp_dir:
        for file in files:
            temp_input_file = os.path.join(temp_dir, file.filename)
            file.save(temp_input_file)
            input_files.append(temp_input_file)

        output_file_path = os.path.join(temp_dir, "combined_data.txt")
        combine_data(input_files, winch_name, output_file_path)

        output_file = tempfile.NamedTemporaryFile(delete=False)
        shutil.copy2(output_file_path, output_file.name)

    return output_file
