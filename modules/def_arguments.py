"""
Parser

USAGE : {MANDATORY} -f [REF_FILE] -r [READS_FILE]
"""


########################## MODULES TO IMPORT ##################################

import argparse
import os
import sys

###############################################################################


def isfile(path):
    """
    Check if path is an existing file
    """

    if not os.path.isfile(path):

        if os.path.isdir(path):
            err = f"{path} is a directory"
        else:
            err = f"{path} does not exist"

        raise argparse.ArgumentTypeError(err)

    return path


def arguments():
    """
    set arguments
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--ref_file", dest = "ref_file",
        type = isfile, required = True,
        help = "ref_file is a .fasta file containing the reference sequence")

    parser.add_argument("-r", "--reads_file", dest = "reads_file",
        type = isfile, required = True,
        help = "reads_file is a .fasta file containing the reads")

    args = parser.parse_args()

    return args.ref_file, args.reads_file


if __name__ == "__main__":
    sys.exit()