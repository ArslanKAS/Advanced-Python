#!/usr/bin/env python

import subprocess

# Open the README.md file and add a character
with open('README.md', 'a') as file:
    file.write('a')

# Commit and push the changes to the repository
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Added a character to the README.md file'])
subprocess.run(['git', 'push'])
print("Success")