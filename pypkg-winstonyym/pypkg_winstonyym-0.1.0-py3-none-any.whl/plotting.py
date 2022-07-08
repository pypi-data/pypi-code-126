import matplotlib.pyplot as plt

def plot_words(word_counts, n=10):
    """Plot bar chart of word counts

    Args:
        word_counts (collections.Counter): Counter object with word counts
        n (int, optional): Top n words to plot. Defaults to 10.

    Returns:
        matplotlib.container.BarContainer: Bar chart of word counts
    """     
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)
    fig = plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    plt.show()
    return fig

