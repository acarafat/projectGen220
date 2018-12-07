# Characterizing 13 Bradyrhizobium Genomes for N2-Fixation Associated Genes 

## Directory structure 

"
~/project220: main project directory
  /strain_genome: 
  	/strain_genome: contain individual genome files
  /bclA_analysis: searching bclA gene homologs in 13 initial strain genome
"


## Step 1 


### Appending all 13 Bradygenome in a single file
`cat *.fasta >> 13_genome.fasta`

### Finding bclA gene homologs in 13 initial strain genome using megablast

`blastn -query bclA.fasta -subject 13_genome.fasta 
-outfmt "6 qseqid sseqid pident length mismatch 
gapopen qstart qend sstart send evalue bitscore sstrand" > megablast.output`

### Extracting gene sequence using BLAST output indice. 

This python scripts creates a  fasta file named 'blast_hits.fasta' and save extracted subsequences from genome based on BLAST output

`python exFasBlstIndc.py ../bclA_analysis/megablast.output ../bclA_analysis/13_genome.fasta`

After getting sub-sequences, need to find ORFs, translate into protein sequences, do conserved domain search in NCBI and prosite

### ORF search
1. Load Emboss tools
`module load emboss`
2. Find ORFs in the sequences which are atleast 300bp long and get the translated protein sequences.
`getorf -sequence blast_hits_extracted_subseq.fasta -outseq orf.out.txt -minsize 300 -reverse no`
3. Use web-CD (Conserved domain) tool in a batch mood on `orf.out.txt` against CDD database (https://www.ncbi.nlm.nih.gov/Structure/bwrpsb/bwrpsb.cgi). After search completed successfully, downloaded dataset (concise, domain hits only). File renamed to `CDD_output.13_brady_genome.txt`
4. Find entries that have 'YddA' domain (the domain family for BclA protein) and save in a file
`grep 'YddA' CDD_output.13_brady_genome.txt | awk {'print $3'} | sed 's/^.// > id.Ydd.txt'`
5. Use a Python script to filter Ydd hit protein sequences in a different file.
`python filter_ydd.py`




