import os
import sys
import subprocess
import shutil
import pathlib
from concurrent.futures import ThreadPoolExecutor

# Pass in the directory as arguments e.g. 'Homework 2/'
ROOT_DIR = os.path.abspath(sys.argv[1])
xv6_path = os.path.join(ROOT_DIR, 'xv6-public')

def setup_student(student):
    print(f"+ Begin Student {student} Setup")
    student_path = os.path.join(ROOT_DIR, student)
    student_xv6_path = os.path.join(student_path, 'xv6-public')
    if os.path.exists(student_xv6_path):
        print(f"- Student {student} has Already Been Setup")
        return
    # Make a copy of xv6 in this student's folder
    shutil.copytree(xv6_path, student_xv6_path)
    # Move student's solution into its xv6 folder
    for file in os.listdir(student_path):
        file_path = os.path.join(student_path, file)
        if file_path == student_xv6_path or pathlib.Path(file_path).suffix.lower() in ['.pdf', '.doc', '.docx']: 
            continue # Skip the xv6 folder itself, skip PDF report
        if os.path.exists(file_path_in_xv6:=os.path.join(student_xv6_path, file)):
            os.remove(file_path_in_xv6) # Replace the original xv6 file
        shutil.move(file_path, student_xv6_path)
    print(f"- Finished Student {student} Setup")

def setup():
    if os.path.exists(xv6_path):
        print("+ Cleaning existing xv6 ...")
        shutil.rmtree(xv6_path)

    students = os.listdir(ROOT_DIR)
    subprocess.run(['git', 'clone', 'https://github.com/mit-pdos/xv6-public', xv6_path])

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(setup_student, student) for student in students]
        for future in futures:
            future.result()
    shutil.rmtree(xv6_path)

def evaluate(student=None):
    students = os.listdir(ROOT_DIR) if not student else list(student)
    for student in students:
        os.chdir(os.path.join(ROOT_DIR, student, 'xv6-public'))
        input(f"+ Press Enter to Evaluating The Next Student {student}")
        while True:
            subprocess.run(['sudo', 'make', 'clean', 'qemu-nox'])
            if input(f"Do you want to re-evaluate Student {student}? [y/N]") != 'y':
                break
    os.chdir(ROOT_DIR)

if __name__ == "__main__":
    setup()
    evaluate()
