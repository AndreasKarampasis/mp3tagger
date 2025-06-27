import os
import csv
import argparse
from mutagen.easyid3 import EasyID3

def list_mp3_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.lower().endswith('.mp3')]

def export_metadata(folder_path, output_csv):
    mp3_files = list_mp3_files(folder_path)
    with open(output_csv, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "title", "artist", "album"])
        for filename in mp3_files:
            filepath = os.path.join(folder_path, filename)
            try:
                audio = EasyID3(filepath)
                writer.writerow([
                    filename,
                    audio.get("title", [""])[0],
                    audio.get("artist", [""])[0],
                    audio.get("album", [""])[0]
                    ])
                print(f"✅ Exported: {filename}")
            except Exception as e:
                print(f"⚠️ Could not read {filename}: {e}")
                writer.writerow([filename, "", "", ""])

def import_metadata(folder_path, input_csv):
    with open(input_csv, mode="r", newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            filename = row["filename"]
            filepath = os.path.join(folder_path, filename)
            if not os.path.exists(filepath):
                print(f"❌ File not found: {filename}")
                continue
            try:
                audio = EasyID3(filepath)
                audio["title"] = row["title"]
                audio["artist"] = row["artist"]
                audio["album"] = row["album"]
                audio.save()
                print(f"✅ Updated: {filename}")
            except Exception as e:
                print(f"⚠️ Failed to update {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(
            description="MP3 Metadata Tool (UTF-8 safe, ideal for Greek text)"
            )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Export command
    export_parser = subparsers.add_parser("export", help="Export metadata to CSV")
    export_parser.add_argument("--folder", required=True, help="Folder with MP3 files")
    export_parser.add_argument("--csv", required=True, help="Output CSV filename")

    # Import command
    import_parser = subparsers.add_parser("import", help="Import metadata from CSV")
    import_parser.add_argument("--folder", required=True, help="Folder with MP3 files")
    import_parser.add_argument("--csv", required=True, help="CSV file to import from")

    args = parser.parse_args()

    if args.command == "export":
        export_metadata(args.folder, args.csv)
    elif args.command == "import":
        import_metadata(args.folder, args.csv)

if __name__ == "__main__":
    main()

