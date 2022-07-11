import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def u_curve(df, weighted, output_file, contig_mode_flag, log=False):
    plt.figure()
    plt.grid()

    sns.histplot(data=df,
                 x='genomes',
                 weights='mean_length' if weighted else None,
                 hue='chroms' if not contig_mode_flag else None,
                 bins=np.arange(df.genomes.min() - 0.5, df.genomes.max() + 0.5, 1) if df.genomes.max() < 50 else 50,
                 log_scale=(False, log),
                 element="step")

    plt.ylabel('Length of fragments that are present\n in n genomes, nucleotides'
               if weighted else 'Number of blocks')
    plt.xlabel('Number of genomes')
    plt.title(f'{"Weighted f" if weighted else "F"}requency of synteny blocks')

    plt.tight_layout()
    plt.savefig(output_file)