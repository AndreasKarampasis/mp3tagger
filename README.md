# MP3Tagger CLI

A simple Python CLI tool to export and edit MP3 metadata in bulk using CSV files. Perfect for fixing non-Unicode tags (like Greek music collections).

## Features

- Export ID3 metadata to CSV
- Edit CSV in Excel, LibreOffice, or Google Sheets
- Re-import and apply changes
- Greek/UTF-8 character support

## Installation

```bash
pip install -r requirements.txt
cd mp3tagger
pip install -r requirements.txt
```

## Usage
```bash
python mp3tagger.py export --folder "/path/to/mp3/folder" --csv "output.csv"
```
`--folder`: Path to the folder containing MP3 files

`--csv`: Output CSV file to create or overwrite

This creates a CSV with columns:
```
filename,title,artist,album
```

## Edit the CSV
Open the exported CSV in any spreadsheet editor and update the metadata.

## Import Metadata from CSV
```bash
python mp3tagger.py import --folder "/path/to/mp3/folder" --csv "output.csv"
```
This will update the .mp3 files in the given folder based on the CSV content.

## Contributing
Contributions are welcome! Feel free to submit pull requests to add new features, fix bugs, or improve documentation.

## License
This project is licensed under the MIT License.
