from Bio import SeqIO

# get list of Ydd ids from commandline output file

id_container = []
seq_records = []

with open('id.Ydd.txt', 'r') as fh:
    for line in fh:
        seq_id = line.strip()
        id_container.append(seq_id)

for seq_record in SeqIO.parse('orf.out.txt', 'fasta'):
    if seq_record.id in id_container:
        seq_records.append(seq_record)

SeqIO.write(seq_records, 'Ydd_hits.fasta', 'fasta') 
