"""
Main Program
"""

########################## MODULES TO IMPORT ##################################

from modules.def_arguments import arguments
from modules import read_fasta_file as fasta
from modules import BWT as bwt
from modules import write_csv_file as write

###############################################################################


def main():
    """
    Main program function
    """

    # get arguments
    ref_file, reads_file = arguments()

    # get reference sequence and reads
    sequence_reference = fasta.read_seq_ref(ref_file)
    reads = fasta.read_reads(reads_file)
    
    # get Burrows-Wheeler transform
    index_seq, transformed = bwt.burwheel_transform(sequence_reference)
    
    # get start sequence
    sequence_initiale = bwt.burwheel_restore(index_seq, transformed)
    
    # verify if the start sequence is the same as the reference sequence
    if sequence_initiale == sequence_reference:
        print("\nBurrows-Wheeler Transform and reference sequence are identical\n")
    else:
        print("\nBurrows-Wheeler Transform and reference sequence are not identical\n")
    
    # Build tally table
    tally = bwt.tally_table(transformed)

    # get characters count
    infs = bwt.nb_inf(transformed)

    # get characters position
    transformed_length, index_transformed = bwt.gen_pos(index_seq, transformed)

    # build the alignments
    alignment = {}  
    for id_read, read in reads.items():
        
        bornes = bwt.map_read_genome(read, infs, tally)
        pos, matches = bwt.display_positions(index_transformed, bornes)
        alignment[id_read] = {"Matches" : matches, "Position" : pos}


    write.write_alignment(alignment)
    write.write_transform(transformed)


if __name__ == "__main__":
    main()