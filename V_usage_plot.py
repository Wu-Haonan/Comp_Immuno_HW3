import matplotlib.pyplot as plt
import pandas as pd

def read_v_gene_usage(file_path):
    v_genes = []
    lineage_counts = []
    
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                v_gene = parts[0].strip()
                count = int(parts[1].strip())
                
                v_genes.append(v_gene)
                lineage_counts.append(count)
        
    return v_genes, lineage_counts

def plot_v_gene_usage(v_genes, lineage_counts, output_file='v_gene_usage.png'):

    plt.figure(figsize=(12, 6))
    
    plt.bar(v_genes, lineage_counts)

    plt.title('V Gene Usage in Clonal Lineages', fontsize=15)
    plt.xlabel('V Genes', fontsize=12)
    plt.ylabel('Number of Clonal Lineages', fontsize=12)
    
    plt.xticks(rotation=45, ha='right')

    for i, v in enumerate(lineage_counts):
        plt.text(i, v, str(v), ha='center', va='bottom')
    
    plt.tight_layout()
    
    plt.savefig(output_file, dpi=300)
    plt.close()

    

if __name__ == '__main__':
    v_usage_file = './V_usages.txt'
    output_image = 'v_gene_usage_plot.png'
    
    v_genes, lineage_counts = read_v_gene_usage(v_usage_file)

    plot_v_gene_usage(v_genes, lineage_counts, output_image)
    print(f"Saved as {output_image}")
 
