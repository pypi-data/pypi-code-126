import matplotlib.pyplot as plt
import seaborn as sns


def length_distribution(df, output_file, contig_mode_flag, log=False):
    plt.figure()
    plt.grid()

    sns.histplot(df,
                 x='mean_length',
                 hue='chroms' if not contig_mode_flag else None,
                 bins=50,
                 log_scale=(False, log),
                 element="step")

    plt.ylabel('Number of blocks')
    plt.xlabel('Mean length in nucleotides')
    plt.xlim(xmin=0)
    plt.title(f'Distribution of synteny blocks length')

    plt.tight_layout()
    plt.savefig(output_file)