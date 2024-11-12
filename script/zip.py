import zipfile
import os


def zip_folder(folder_path="temp/data", output_zip="SubwayBooster.zip"):
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Copy src/version.json into the ZIP archive
        version_file_path = os.path.join("src", "version.json")
        zipf.write(version_file_path, arcname=os.path.join("version.json"))

        # Iterate through the folder and include JSON files
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Calculate the relative path and zip archive path
                arcname = os.path.relpath(file_path, folder_path)
                zip_arcname = os.path.join("profile", arcname)
                zipf.write(file_path, arcname=zip_arcname)


zip_folder()
