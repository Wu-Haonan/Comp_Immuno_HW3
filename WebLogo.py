import logomaker
import pandas as pd
import numpy as np
from Bio import SeqIO
import matplotlib.pyplot as plt

def read_fasta_sequences(file_path):
    """
    Read sequences from a FASTA file
    
    Args:
    file_path (str): Path to the FASTA file
    
    Returns:
    list: List of sequences
    """
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append(str(record.seq))
    return sequences

def create_weblogo(sequences, output_file='weblogo.png'):
    """
    Create a WebLogo plot from a list of sequences
    
    Args:
    sequences (list): List of sequences of equal length
    output_file (str): Path to save the output image
    """
    # Validate sequences have same length
    if len(set(len(seq) for seq in sequences)) > 1:
        raise ValueError("All sequences must have the same length")
    
    # Calculate count matrix
    seq_length = len(sequences[0])
    count_matrix = np.zeros((seq_length, 20), dtype=int)
    amino_acids = 'ACDEFGHIKLMNPQRSTVWY'
    
    # Count amino acid occurrences
    for seq in sequences:
        for pos, aa in enumerate(seq):
            if aa in amino_acids:
                count_matrix[pos, amino_acids.index(aa)] += 1
    
    # Create DataFrame for logomaker
    count_df = pd.DataFrame(
        count_matrix, 
        columns=list(amino_acids),
        index=[f'Pos {i+1}' for i in range(seq_length)]
    )
    
    # Create logo
    logo = logomaker.Logo(count_df, 
                          color_scheme='hydrophobicity',
                          figsize=(12, 4))
    
    # Customize logo
    logo.style_spines(visible=False)
    logo.style_xticks(rotation=45, fmt='%d', anchor=0)
    
    # Save or show the logo
    plt.title('Sequence Logo')
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    # Replace with your FASTA file path
    fasta_file = '/path/to/your/sequences.fasta'
    
    try:
        # Read sequences
        sequences = read_fasta_sequences(fasta_file)
        
        # Create WebLogo
        create_weblogo(sequences)
        print(f"WebLogo created successfully. Saved as weblogo.png")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
