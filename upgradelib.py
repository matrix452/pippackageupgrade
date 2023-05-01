import subprocess, os
packages = []
output = subprocess.getoutput('python3 -m pip list')
outputs = output.split('\n')
for i in range(2,len(outputs)):
    packages.append((outputs[i].split(' '))[0])
for package in packages:
    command = "python3 -m pip install --upgrade " + package
    os.system(command)
