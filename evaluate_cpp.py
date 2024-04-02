import os
import sys
import subprocess

def compile_file(root, file):
    # Generate Paths for the files
    src = os.path.join(root, file)
    # Remove the '.c' extension for the output file
    dst = os.path.join(root, os.path.splitext(file)[0])

    # Compile using gcc
    subprocess.run(['gcc', src, '-o', dst], check=True)

    # Execution
    subprocess.run("./" + dst)
    os.remove(dst) # Cleanup

def evaluate_file(executable):
    subprocess.run("./" + executable)
    os.remove(executable) # Cleanup

def main(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.c'):
                student = os.path.basename(os.path.dirname(os.path.join(root, file)))
                # Compile this file
                input(f"Press Enter to Compile and Evaluate {student} {file}")
                while True:
                    try:
                        dst = compile_file(root, file)
                    except subprocess.CalledProcessError:
                        if input(f"Failed! Re-compile {student} {file}? [y/N]") == 'y':
                            continue
                        print(f"Skipping Evaluation of {student} {file} due to unsuccessful compilation")
                    break


if __name__ == "__main__":
    # Pass in the directory as arguments e.g. 'Homework 2/'
    main(sys.argv[1])
