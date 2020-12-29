"""
Burrows - Wheeler Algorithm Module
"""

########################## MODULES TO IMPORT ##################################

from operator import itemgetter
from collections import Counter
import copy
import sys
    
###############################################################################


def burwheel_transform(sequence):   
    """
    create the Burrows-Wheeler transform based on a sequence
    """

    sequence = "$" + sequence
    seq_length = len(sequence)
    
    seq_sorted = sorted([sequence[i:seq_length] + 
        sequence[0:i] for i in range(1, seq_length + 1)])
    
    index_seq = seq_sorted.index(sequence)
    transformed = ''.join([j[-1] for j in seq_sorted])

    return index_seq, transformed


def burwheel_restore(index_seq, transformed):
    """
    Restore the reference sequence
    """

    transformed_length, index_transformed = gen_pos(index_seq, transformed)
    index_seq_init = [index_seq]

    for i in range(1, transformed_length - 1):
        index_seq_init.append(index_transformed[index_seq_init[i - 1]])
    seq_init_reversed = [transformed[i] for i in index_seq_init]
    seq_init_reversed.reverse()
    restored_seq = ''.join(seq_init_reversed)
    
    return restored_seq


def tally_table(transformed):
    """
    generate a tally table based on the Burrows-Wheeler transform
    """

    dictionnaire, tally = {"$": 0, "A" : 0, "C" : 0, "G" : 0, "T" : 0}, []
    
    for nt in transformed:
        dictionnaire[nt] += 1
        tally.append(copy.deepcopy(dictionnaire))

    return tally


def nb_inf(transformed):
    """
    generate a dictionnary of characters count
    """

    infs, count = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0}, Counter(sorted(transformed))
    nb = 0
    for nt in infs.keys():
        infs[nt] = nb
        nb += count[nt]

    return infs


def gen_pos(index_seq, transformed):
    """
    Retrieve the character position in the start sequence
    """

    transformed_length = len(transformed)
    
    couple_index_base = sorted([(i, x) for i, x in enumerate(transformed)], key = itemgetter(1))
    index_transformed = [None for i in range(transformed_length)]
    
    for index, couple in enumerate(couple_index_base):
        j,_ = couple
        index_transformed[j] = index

    return transformed_length, index_transformed


def map_read_genome(read, infs, tally):
    """
    Retrieve the alignment of the read with the reference genome
    """

    i = len(read) - 1
    term_inf = infs[read[i]]
    term_supp = infs[read[i]] + tally[-1][read[i]] - 1

    while i >= 1 and term_inf <= term_supp:
        i -= 1
        term_inf = infs[read[i]] + tally[term_inf - 1][read[i]]
        term_supp = infs[read[i]] + tally[term_supp][read[i]] - 1

    return term_inf, term_supp


def display_alignment(seq_ref, read, index_transformed, bornes):
    """
    Retrieve the alignment of a read with the reference sequence
    """

    positions = []
    for i in range(bornes[0], bornes[1] + 1):
        positions.append(index_transformed[i] + 1)
    
    positions.sort()
    nb_match = len(positions)

    alignments = "." * len(seq_ref)
    for pos in positions:
        alignments = alignments[:pos] + read + alignments[pos + len(read):]
    

    return alignments, nb_match


def display_positions(index_transformed, bornes):
    """
    Retrieve the number of matches for each read
    """

    positions = []
    for i in range(bornes[0], bornes[1] + 1):
        positions.append(index_transformed[i] + 1)
    positions.sort()
    matches = len(positions)

    return positions, matches


if __name__ == "__main__":
    sys.exit()