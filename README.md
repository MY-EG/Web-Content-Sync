# URLSync

URLSync is a Python script designed to continuously check a specified document accessible via URL for updates and save its contents locally. This script is useful for scenarios where real-time synchronization between an online document and a local file is required.

## Features

- Automatically retrieves content from a document using its URL.
- Monitors changes in the document and updates the local file accordingly.
- Customizable start and end markers to specify the portion of the document to synchronize.
- Error handling for network issues and document parsing errors.
- Simple and easy-to-understand Python script.

## Usage

1. Clone or download this repository to your local machine.
2. Install the required Python packages using `pip install requests`.
3. Modify the script variables to specify your document URL, local file name, and synchronization interval.
   - You can change the document URL to any link you want, not limited to Google documents.
4. Run the script using `python Web-Content-Sync.py`.
5. The script will continuously monitor the document for updates and save its contents locally.

### Running in the Background

To run the script in the background without a terminal window, you can use the provided "Run-without-terminal.vbs" file. This VBScript file launches the Python script invisibly.

1. Ensure both the Python script (Web-Content-Sync.py) and the Run-without-terminal.vbs file are in the same directory.
2. Double-click the Run-without-terminal.vbs file to execute it.
3. The script will run in the background, continuously monitoring the specified document.

## Configuration

- `url`: URL of the document to synchronize.
- `file`: Name of the local file to save the synchronized content.
- `start` and `end`: Markers to specify the portion of the document to synchronize.
- `yeni`: Interval (in seconds) to wait between synchronization attempts.
- `error`: Interval (in seconds) to wait before retrying after encountering an error.

## Dependencies

- [requests](https://pypi.org/project/requests/): HTTP library for making requests and handling responses.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

