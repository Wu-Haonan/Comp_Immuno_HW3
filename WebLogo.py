import logomaker
import pandas as pd
import numpy as np
from Bio import SeqIO
from Bio.Seq import Seq
import matplotlib.pyplot as plt

def translate_sequence(nucleotide_seq):
    seq_obj = Seq(nucleotide_seq)
    aa_seq = str(seq_obj.translate())
    aa_seq = aa_seq.replace('*', '')
    return aa_seq

def read_and_translate_fasta(file_path):
    amino_acid_sequences = []
    
    for record in SeqIO.parse(file_path, "fasta"):
        nucleotide_seq = str(record.seq)
        aa_seq = translate_sequence(nucleotide_seq)
        
        amino_acid_sequences.append(aa_seq)
    
    return amino_acid_sequences

def create_weblogo(sequences, output_file='weblogo.png'): 
    
    # count matrix
    seq_length = len(sequences[0])
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    count_matrix = np.zeros((seq_length, len(amino_acids)), dtype=int)
    
    # Count amino acid occurrences
    for seq in sequences:
        for pos, aa in enumerate(seq):
            if aa in amino_acids:
                count_matrix[pos, amino_acids.index(aa)] += 1
    
    count_df = pd.DataFrame(
        count_matrix, 
        columns=list(amino_acids),
        index=range(seq_length)  
    )
    
    plt.figure(figsize=(12, 4))
    logo = logomaker.Logo(count_df, color_scheme='hydrophobicity')
    
    plt.title('Amino Acid Sequence Logo')
    plt.xlabel('Position')
    plt.ylabel('Bits')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    fasta_file = './largest_clonal_lineage_CDR3.fasta'
    output_logo = 'amino_acid_weblogo.png'

    amino_acid_sequences = read_and_translate_fasta(fasta_file)
    
    create_weblogo(amino_acid_sequences, output_logo)
    print(f"Saved as {output_logo}")