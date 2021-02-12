import sys
import subprocess

#pip as subprocess
subprocess.check_call([sys.executable,'-m','pip','install','instabot'])
subprocess.check_call([sys.executable,'-m','pip','install','mysql-connector-python'])
subprocess.check_call([sys.executable,'-m','pip','install','Pillow'])
subprocess.check_call([sys.executable,'-m','pip','install','matplotlib'])
