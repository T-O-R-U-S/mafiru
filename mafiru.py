#!/usr/bin/python

import os
import re
from sys import argv

# This method is now depracated in favor of os.scandir(), however the extra properties it provides are useless in this case
# os.scandir() also has variability depending on the platform -- it returns either posixPath (*nix/macOS) or windowsPath (windows).
directory = os.listdir('.')

if len(argv) < 3:
    print("Must specify two arguments")
    exit(1)

argv[1] = re.compile(argv[1])

extension_detect = re.compile(r'\[e\]|\[f\]')
extension_replace = re.compile(r'.*\.')

iteration = 0

for filename in directory:
    if re.match(argv[1], filename):
        iteration += 1
        new_name = argv[2]

        functions = [
            [r'\[i\]', str(iteration)],
            [
                r'\[f\]|\[e\]',
                re.sub(r'.*\.', '.', filename)
            ],
            [
                r'\[n\]',
                re.sub(r'\..*', '', filename)
            ]
        ]

        if not re.search("\[i\]|\[n\]", argv[2]):
            print("No iteration or filename specifier -- renaming would result in file overwrite! Cancelling operation...")
            exit(1)

        for part in functions:
            new_name = re.sub(part[0], part[1], new_name)

        print(new_name)

        os.rename('./'+filename, new_name)
