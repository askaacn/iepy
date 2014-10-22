#!/usr/bin/env python

"""
IEPY instance creator.

Usage:
    iepy <folder_name>

Options:
  -h --help             Show this screen
"""

import os
import sys
import json
import shutil

from docopt import docopt

from iepy import defaults


def execute_from_command_line(argv=None):
    opts = docopt(__doc__, argv=argv, version=0.1)
    folder_name = opts["<folder_name>"]

    if os.path.exists(folder_name):
        print("Folder already exists")
        sys.exit(1)

    iepy_base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    iepy_scripts_path = os.path.join(iepy_base_path, "scripts")

    files_to_copy = [
        os.path.join(iepy_scripts_path, "csv_to_iepy.py"),
        os.path.join(iepy_scripts_path, "preprocess.py"),
        os.path.join(iepy_scripts_path, "iepy_runner.py"),
        os.path.join(iepy_scripts_path, "iepy_rules_runner.py"),
    ]

    # Create folders
    bin_folder = os.path.join(folder_name, "bin")

    os.mkdir(folder_name)
    os.mkdir(bin_folder)

    for filepath in files_to_copy:
        filename = os.path.basename(filepath)
        destination = os.path.join(bin_folder, filename)
        shutil.copyfile(filepath, destination)

    # Create empty rules file
    rules_filepath = os.path.join(folder_name, "rules.py")
    with open(rules_filepath, "w") as filehandler:
        filehandler.write("# Write here your rules\n")
        filehandler.write("# RELATION = 'your relation here'\n")

    # Create extractor config
    extractor_config_filepath = os.path.join(folder_name, "extractor_config.json")
    with open(extractor_config_filepath, "w") as filehandler:
        json.dump(defaults.extractor_config, filehandler, indent=4)


if __name__ == "__main__":
    execute_from_command_line()
