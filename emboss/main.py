import argparse
import sys
import subprocess

print('subprocess.run(["./water", "-version"])')
subprocess.run(["./water", "-version"])
print('subprocess.run(["./water", "-version"], capture_output=True)')
process = subprocess.run(["./water", "-version"], capture_output=True)
print(process.stderr)
print("success")
