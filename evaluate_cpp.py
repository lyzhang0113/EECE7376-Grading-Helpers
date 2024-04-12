import os
import sys
import subprocess


def compile_and_run(root, file):
    # Remove the '.c' extension for the output file
    executable = os.path.splitext(file)[0]

    while True:
        # Compile using gcc
        subprocess.run(['gcc', file, '-o', executable], check=True)
        # Execution
        args = input(f"?? Enter args:\n  $ ./{executable} ").split(" ")
        subprocess.run(["./" + executable] + args)
        if input(f"?? Execute {executable} again? [y/N]") != 'y':
            break
    os.remove(executable) # Cleanup




def main(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.endswith('.c'):
                continue
            cwd = os.getcwd() # Save cwd
            student = os.path.basename(os.path.dirname(os.path.join(root, file)))
            # Compile this file
            print(f"\n++ Compiling {student} {file} ...")
            # if input(f"Do you want to skip this file? [y/N]") == 'y':
                # continue
            while True:
                try:
                    os.chdir(os.path.dirname(os.path.join(root, file)))
                    dst = compile_and_run(root, file)
                except subprocess.CalledProcessError:
                    if input(f"?? Failed! Re-compile {student} {file}? [y/N]") == 'y':
                        continue
                    print(f"++ Skipping Evaluation of {student} {file} due to unsuccessful compilation")
                finally:
                    os.chdir(cwd) # Move back to original working directory
                break


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <Homework directory>")
        exit(1)
    # Pass in the directory as arguments e.g. 'Homework 2/'
    main(sys.argv[1])
