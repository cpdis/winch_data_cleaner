
# Winch Data Cleaner

Winch Data Cleaner is a web application that allows users to combine multiple winch data files, filter the data based on user-selected winch names, and generate a time series plot for a specified data column. The app is built using Flask, pandas, and Tailwind CSS.

## Features

- Upload multiple winch data files
- Input up to 4 winch names to filter the data
- Choose a data column to generate a time series plot
- Download the combined and filtered data as a CSV file
- View and download the time series plot as an image

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/winch_data_cleaner.git
```

2. Navigate to the project directory:

```bash
cd winch_data_cleaner
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows: `venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Run the Flask app:

```bash
python app.py
```

The app will be accessible at `http://127.0.0.1:5000`.

## Usage

1. Open the web app in your browser.
2. Upload the winch data files you want to combine.
3. Input the winch names you want to include in the combined data.
4. Choose a data column to generate a time series plot.
5. Click the "Process Data" button.
6. Download the combined data as a CSV file and the time series plot as an image.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update the tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

Feel free to modify the content as needed to better suit your project. Be sure to replace `yourusername` in the `git clone` command with your actual GitHub username.
