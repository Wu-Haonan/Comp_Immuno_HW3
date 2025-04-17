# Comp_Immuno_HW3
homework 3 of Computational Immunogenomics



1. The original VDJ sequences are stored  `./data/PRJNA324093_Dnr4_10k.fasta`
2. ImmunoTools (https://immunotools.github.io/immunotools/) is used to align and analyze VDJ sequences. The results are stored in `./Alignment_results`. The output we focused on is `compressed_cdr3s.fasta`, which shows all the CDR3 sequences, counts, and corresponding V, J genes. 
3. Run `./clonal_lineage` to generate 
   1. Statistics information for clonal lineages. 
   2. The usage of V genes among each clonal lineages (stored in `./V_usages.txt`).
   3. The fasta file of CDR3 sequence for largest clonal lineage (stored in `./largest_clonal_lineage_CDR3.fasta`).
4. Run `python WebLogo.py` to generate a web logo plot of amino acid sequences of CDR3s from the largest clonal lineages.
5. Run `python V_usage_plot.py` a usage plot of the V genes.
