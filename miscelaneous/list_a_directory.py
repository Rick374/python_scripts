#!/usr/bin/env python3
import argparse
import os
import string
import shutil


def list_dir(path_to_list_dir):
    try:
        # get all files inside a specific folder
        dir_path = path_to_list_dir
        for path in os.scandir(dir_path):
            if path.is_file():
                print(path.name)
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s." % (e.strerror))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_list_dir', type=str, help='Path to list directory')
    args = parser.parse_args()
    res = list_dir(args.path_to_list_dir)
