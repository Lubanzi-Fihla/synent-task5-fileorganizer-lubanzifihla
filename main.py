import os
import shutil

folder_path = input("Enter folder path: ")

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        extension = file.split(".")[-1].lower()

        if extension in ["jpg", "jpeg", "png"]:
            category = "Images"
        elif extension in ["pdf", "docx", "txt"]:
            category = "Documents"
        elif[- " extension in ["mp4", "avi"]:
        category = "Videos"
        else:
            category = "Others"

        destination = os.path.join(folder_path, category)
        os.makedirs(destination, exist_ok=True)

        shutil.move(file_path, os.path.join(destination, file))

print("Files organized successfully!")
