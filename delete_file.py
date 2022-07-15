#!/usr/bin/env python3
import argparse
import os
import string


def delete_folder(delete_file):
    try:
        os.remove(delete_file)
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('delete_file', type=str, help='Name of file to delete')
    args = parser.parse_args()
    res = delete_folder(args.delete_file)