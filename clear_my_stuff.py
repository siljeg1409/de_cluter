import os
import datetime

origin_folder = "origin_folder_path"
backup_folder = "C:\\Backup\\"

image_extensions = ['.jpg', '.png', '.jpeg']
video_extensions = ['.mp4', '.webm', '.swf']
document_extensions = ['.doc', '.docx', '.pdf', '.txt', '.xml', '.dat', '.csv', '.xls', '.odt']
application_extensions = ['.exe']
compressed_extensions = ['.zip', '.7z', '.rar', '.ZIP']
misc_extensions = ['.sql', '.edi', '.json', '.log', '.htm', '.ini', '.crdownload']


def get_sufix():
    return datetime.datetime.today().strftime('%Y%m%d%H%M%S') + "_"


def get_folder(ext):
    if ext in image_extensions:
        return "images\\"
    if ext in video_extensions:
        return "videos\\"
    if ext in document_extensions:
        return "documents\\"
    if ext in application_extensions:
        return "applications\\"
    if ext in compressed_extensions:
        return "zips\\"
    if ext in misc_extensions:
        return "miscs\\"
    else:
        return ""


def check_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def clean_files():
    print("Processing...")
    for f in os.listdir(origin_folder):
        filename, file_extension = os.path.splitext(f)
        origin_file = origin_folder + f
        subfolder = get_folder(file_extension)
        if subfolder == "":
            continue
        new_file = check_folder(backup_folder + subfolder) + get_sufix() + f
        print("Moving file: " + f)
        os.replace(origin_file, new_file)
    print("Done!")

clean_files()
