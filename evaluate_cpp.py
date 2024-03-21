import os
import sys
import subprocess
from organize import organize_by_student_name

def compile_c_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.c'):
                full_path = os.path.join(root, file)
                # Remove the '.c' extension for the output file
                output_file = os.path.join(root, os.path.splitext(file)[0])
                # File for compiler warnings and errors
                error_file = os.path.join(root, os.path.splitext(file)[0] + '_errors.txt')
                
                # Compile the C file
                with open(error_file, 'w') as ef:
                    try:
                        subprocess.run(['gcc', full_path, '-o', output_file], 
                                       stderr=ef, 
                                       check=True)
                        print(f"Compiled: {full_path} to {output_file}")
                    except subprocess.CalledProcessError as e:
                        print(f"Failed to compile {full_path}, see {error_file} for details")

                # Delete the error file if it is empty
                if os.path.getsize(error_file) == 0:
                    os.remove(error_file)

if __name__ == "__main__":
    # Pass in the directory as arguments e.g. 'Homework 2/'
    compile_c_files(sys.argv[1])
