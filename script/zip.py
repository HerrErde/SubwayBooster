import zipfile
import os

def zip_folder(folder_path="temp", output_zip="SubwayBooster.zip"):
    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Copy src/version.json into "files/" within the ZIP archive
        version_file_path = os.path.join("src/version.json")
        zipf.write(version_file_path, arcname="Android/data/com.kiloo.subwaysurf/files/version.json")

        # Iterate through the folder and include JSON files
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zip_arcname = os.path.join(
                    "Android/data/com.kiloo.subwaysurf/files/profile/", arcname
                )
                if file.endswith(".json"):  # Include only JSON files
                    zipf.write(file_path, arcname=zip_arcname)

zip_folder()
