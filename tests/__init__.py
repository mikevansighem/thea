import os.path
import sys

# Ensure importing from parent directory is possible
for directory in os.walk(os.getcwd()):
    sys.path.append(directory[0])
