## Directory structure 

- project220: main project directory
  - strain_genome: contains individual genome files
  - bclA_analysis: searching bclA gene homologs in 13 initial strain genome


## Step 1 


### Finding bclA gene homologs in 13 initial strain genome using megablast

`blastn -query bclA.fasta -subject 13_genome.fasta 
-outfmt "6 qseqid sseqid pident length mismatch 
gapopen qstart qend sstart send evalue bitscore sstrand" > megablast.output`

### Extracting gene sequence using BLAST output indice. 

This python scripts creates a  fasta file named 'blast_hits.fasta' and save extracted subsequences from genome based on BLAST output

`python exFasBlstIndc.py ../bclA_analysis/megablast.output ../bclA_analysis/13_genome.fasta`

After getting sub-sequences, need to find ORFs, translate into protein sequences, do conserved domain search in NCBI and prosite

### ORF search
Load Emboss tools
`module load emboss`
Find ORFs in the sequences whihc are atleast 300bp long
`getorf -sequence blast_hits_extracted_subseq.fasta -outseq orf.out.txt -minsize 300 -reverse no`
