#!/usr/bin/env python3

# Extract fasta from BLAST indices
# This script use a formated BLAST output file with the following header:
#      query_id subject_id pct_identity aln_length n_of_mismatches gap_openings q_start q_end s_start s_end e_value bit_score  strand
# Usage: python exFasBlstIndc.py blat.output genome.fasta

import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

indices = {}
extracted_seqs = []

# Extracting indices and strand info from blast output file
print('BLAST indices info:')
print('seq_id\tseq_start\tseq_end\tstrand')
with open(sys.argv[1]) as fh:
    for line in fh.readlines():
        line = line.strip().split('\t')
        if line[0].startswith('query_id'):
            pass
        else:
            seq_id = line[1]
            s_start = line[8]
            s_end = line[9]
            strand = line[-1]

            indices[seq_id] = [s_start, s_end, strand]
            print('{}\t{}\t{}\t{}'.format(seq_id, s_start, s_end, strand))

# Extract sequences using the indices
print('\n\nSubseq extraction from genome file:')
print('seq_id\textracted_len')
for seq_record in SeqIO.parse(sys.argv[2], 'fasta'):
    if seq_record.id in indices.keys():
        if indices[seq_record.id][2] == 'plus':
            sub_seq = seq_record[int(indices[seq_record.id][0]):
                int(indices[seq_record.id][1])+1]
        else:
            sub_seq = seq_record.reverse_complement()[int(indices[seq_record.id][1]):
                int(indices[seq_record.id][0])+1]
        sub_seq = SeqRecord(Seq(str(sub_seq.seq)), id=seq_record.id, description=seq_record.description)
        extracted_seqs.append(sub_seq)

        print('{}\t{}'.format(seq_record.id, len(sub_seq.seq)))

# Write new file 
SeqIO.write(extracted_seqs, 'blast_hits.fasta', 'fasta')
#for i in extracted_seqs:
#    print(i,'\n')
