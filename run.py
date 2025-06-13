import sys
import os
import subprocess

# Add root directory to PYTHONPATH
os.environ['PYTHONPATH'] = f"{os.getcwd()}:{os.environ.get('PYTHONPATH', '')}"

# Run the script passed as argument
if len(sys.argv) < 2:
    print("Usage: python run.py <relative_path_to_script>")
    sys.exit(1)

script_to_run = sys.argv[1]
subprocess.run(['python', script_to_run])

