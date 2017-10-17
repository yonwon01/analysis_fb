import collections
import matplotlib.pyplot as plt

RESULT_DIRECTORY = '__results__/graph'

def graph_bar(
        title=None,
        xlabel=None,
        ylabel=None,
        showgrid=False,
        values=None,
        ticks=None,
        filename=None,
        showgraph=True):

    fig, subplots = plt.subplots(1, 1)
    subplots.bar(range(len(values)), values, align='center')

    # ticks
    if ticks is not None and isinstance(ticks, collections.Sequence):
        subplots.set_xticks(range(len(ticks)))
        subplots.set_xticklabels(ticks, rotation=70, fontsize='small')

    # title
    if title is not None and isinstance(title, str):
        pass

    # xlabel
    if xlabel is not None and isinstance(xlabel, str):
        pass

    # ylabel
    if ylabel is not None and isinstance(ylabel, str):
        pass

    if filename is not None and isinstance(filename, str):
        save_filename = '%s/bar_%s' % (RESULT_DIRECTORY, filename)
        plt.savefig(save_filename, dpi=400, bbox_inches='tight')

    # show grid
    subplots.grid(showgrid)

    if showgraph:
        plt.show()
