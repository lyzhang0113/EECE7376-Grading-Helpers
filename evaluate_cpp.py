import os
import sys
import subprocess


def compile_and_run(root, file):
    # Generate Paths for the files
    src = os.path.join(root, file)
    # Remove the '.c' extension for the output file
    executable = os.path.splitext(file)[0]
    dst = os.path.join(root, executable)
    while True:
        # Compile using gcc
        subprocess.run(['gcc', src, '-o', dst], check=True)
        # Execution
        args = input(f"?? Enter args:\n  $ ./{executable} ").split(" ")
        subprocess.run(["./" + dst] + args)
        if input(f"?? Execute {executable} again? [y/N]") != 'y':
            break
    os.remove(dst) # Cleanup


def main(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.endswith('.c'):
                continue
            student = os.path.basename(os.path.dirname(os.path.join(root, file)))
            # Compile this file
            print(f"\n++ Compiling {student} {file} ...")
            # if input(f"Do you want to skip this file? [y/N]") == 'y':
                # continue
            while True:
                try:
                    dst = compile_and_run(root, file)
                except subprocess.CalledProcessError:
                    if input(f"?? Failed! Re-compile {student} {file}? [y/N]") == 'y':
                        continue
                    print(f"++ Skipping Evaluation of {student} {file} due to unsuccessful compilation")
                break


if __name__ == "__main__":
    # Pass in the directory as arguments e.g. 'Homework 2/'
    main(sys.argv[1])
