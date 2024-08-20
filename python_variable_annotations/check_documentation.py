#!/usr/bin/env python3
import os
import sys

def check_documentation(file_path):
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    with open(file_path, 'r') as file:
        content = file.read()
        if '"""' in content or "'''" in content:
            print("OK")
        else:
            print("Module not documented or not enough")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./check_documentation.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    check_documentation(file_path)
