"""
Output Module
"""

########################## MODULES TO IMPORT ##################################

import csv
import sys
import os

###############################################################################


def fill(text, width = 80):
    """
    Split text with a line return to respect fasta format
    """

    return os.linesep.join(text[i:i + width] for i in range(0, len(text), width))



def write_transform(transformed):
    """
    save the Burrows-Wheeler transform in a txt file
    """

    with open("results/transformed.txt", "w") as filout:
        filout.write("> Burrows-Wheeler Transform" + "\n")
        filout.write(fill(transformed))


def write_alignment(alignements):
    """
    Generate a CSV file containing read's ID, number of matches
    and position for each match
    """

    with open("results/alignements.csv", "w") as filout:
        fields = ["Read", "Nb_Matches", "Position"]
        f_writer = csv.DictWriter(filout, fieldnames = fields)
        f_writer.writeheader()
        for read, value in alignements.items():
            data = {"Read" : read,
                    "Nb_Matches": value["Matches"],
                    "Position" : value["Position"]}
            f_writer.writerow(data)


if __name__ == "__main__":
    sys.exit()