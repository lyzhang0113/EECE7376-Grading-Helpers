import os
import shutil
import sys
import zipfile

SUBMISSIONS_ZIP_FILE = sys.argv[1]

def _split_student_and_filename(filename):
    """
    Extract prefix from the filename.
    Assumes the prefix is the part before the first underscore.
    """
    filename = filename.replace('_LATE', '').replace('-1', '').replace('-2', '')
    items = filename.split('_')
    return items[0], '_'.join(items[3:])

def organize_by_student_name(directory):
    """
    Move files into subfolders based on their prefixes and remove the prefix in the process.
    """

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            student, new_filename = _split_student_and_filename(filename)
            student_dir = os.path.join(directory, student)

            if not os.path.exists(student_dir):
                os.makedirs(student_dir)

            shutil.move(file_path, os.path.join(student_dir, new_filename))

if __name__ == "__main__":
    dir = input("Please Enter the Name of this Homework (e.g. Homework 1): ")
    with zipfile.ZipFile(SUBMISSIONS_ZIP_FILE, 'r') as submissions:
        input(f"Press Enter to UNZIP submission.zip into {dir}")
        submissions.extractall(dir)

    # Pass in directory as argument e.g. 'Homework 2/'
    organize_by_student_name(dir)
