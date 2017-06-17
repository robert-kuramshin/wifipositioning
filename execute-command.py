import subprocess

proc = subprocess.Popen('ping google.com', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
tmp = proc.stdout.read()
print tmp
