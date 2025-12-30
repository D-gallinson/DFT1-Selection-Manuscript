import pandas as pd
import sys


# This script does the following:
# 1) Determine if any sequences are collapsed
# 2) Write collapse to file (rather than print to stdout)
# 3) Only write to file if >0 sequences are collapsed
# 4) Print to stdout if any sequences were collapsed



# NOTE: argv always takes the python script itself as the first argument, so we expect that implicit arg plus
#               the user-defined seq
if(len(sys.argv) != 3):
	print("There should be exactly 2 arguments to this script (the path to the un-collapsed fasta file and the output path). Exiting.")
	exit()

seq_path = sys.argv[1]
outpath = sys.argv[2]

# Read in tmp un-collapsed fasta path and generate a big string from the file
with open(seq_path, 'r') as h:
	seq = h.readlines()
	seq = "".join(seq)

# Generate dataframe by splitting > then \n
seq_arr = seq.split(">")[1:]
seq_arr = pd.DataFrame([seq.rstrip().split("\n") for seq in seq_arr if seq.rstrip().split("\n")])

# Grouping by seqs and joining names where seqs are identical
collapsed_seqs = seq_arr.groupby(by=1, sort=False)[0].apply(".".join)
collapsed_seqs_str = ">" + collapsed_seqs + "\n" + collapsed_seqs.index
collapsed_seqs_str = collapsed_seqs_str.str.cat(sep="\n")

# Check if any haplotypes were collapsed. If none were, print False, otherwise print the list of collapsed names separated by spaces
# which can be parsed as an array by a bash script
has_collapsed = seq_arr.shape[0] != collapsed_seqs.shape[0]
if has_collapsed:
	has_collapsed = collapsed_seqs.str.cat(sep=" ")
print(has_collapsed)

# If there are any collapsed haplotypes, write to file
with open(outpath, 'w') as h:
        h.write(collapsed_seqs_str)
