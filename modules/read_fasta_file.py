"""
Read fasta files module
"""

########################## MODULES TO IMPORT ##################################

import sys

###############################################################################


def read_seq_ref(fasta_file):
    """
    Retrieve the reference sequence from a fasta file
    """

    with open(fasta_file, "r") as filin:
        sequence_reference = ""
        for line in filin:
            if not line.startswith(">"):
                sequence_reference += line.strip()

    return sequence_reference


def read_reads(fasta_file):
    """
    Retrieve the reads from a reads containing file
    """

    with open(fasta_file, "r") as filin:
        reads = {}
        for line in filin:
            
            if line.startswith(">"):
                reads_id = line.split(".")[0].split(">")[1]
                reads[reads_id] = ""
            
            else:
                reads[reads_id] += line.strip()
    
    return reads


if __name__ == "__main__":
    sys.exit()