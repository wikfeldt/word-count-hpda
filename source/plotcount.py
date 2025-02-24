import matplotlib.pyplot as plt
import click


def plot_bar_chart(x_values, y_values, title, plot_file):
    plt.figure(figsize=(10, 5))
    plt.bar(x_values, y_values)
    plt.xticks(rotation=45)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(plot_file)


@click.command()
@click.option("-n", "--nb-words", default=10, help="Limit to the top N number of words")
@click.argument("data-file", type=click.Path(exists=True))
@click.argument("plot-file")
def main(data_file, plot_file, nb_words):
    r"""Arguments:

    DATA_FILE: str

        Input data file in plain text generated by `wordcount.py` and found in `processed_data` directory

    PLOT_FILE: str

        Output image file. It can be something like `results/pg42.png`

    """
    # read data from input_file
    x_values = []
    y_values = []
    with open(data_file) as data:
        for index, line in enumerate(data.readlines()):
            word, count, _percent = line.split()
            x_values.append(word)
            y_values.append(int(count))
            if (index + 1) == nb_words:
                break

    # now plot the data
    plot_bar_chart(x_values, y_values, f"{nb_words} most common words", plot_file)


if __name__ == "__main__":
    main()
