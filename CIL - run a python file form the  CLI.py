import subprocess

# call the run.py python file 3 times using the CLI
for i in range (3):
    subprocess.check_call(['python', 'run.py'])

