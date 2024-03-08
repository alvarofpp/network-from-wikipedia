import argparse

import networkx as nx

from utils.functions import clean, download, truncate


def main():
    parser = argparse.ArgumentParser(description='Download and make a graphml'
                                                 'file from Wikipedia page.')
    parser.add_argument('-s', '--source',
                        required=True,
                        type=str,
                        help='Url or title from Wikipedia.')
    parser.add_argument('-d', '--degree',
                        default=2,
                        type=int,
                        help='Number of degree that will be used in the filter'
                             'of nodes. Equal to or greater than this value.')
    parser.add_argument('-l', '--layers',
                        default=2,
                        type=str,
                        help='Number of search layers.')
    parser.add_argument('-o', '--output',
                        default='output',
                        type=str,
                        help='Output filename.')
    parser.add_argument('-v', '--verbose',
                        default=False,
                        action='store_true',
                        help='Increase output verbosity.')
    args = parser.parse_args()
    args_dict = dict(vars(args).items())

    graph = download(
        source=args_dict['source'],
        verbose=args_dict['verbose'],
        layers=args_dict['layers']
    )
    graph = clean(graph)
    graph = truncate(
        graph,
        verbose=args_dict['verbose'],
        degree=args_dict['degree']
    )
    nx.write_graphml(graph, '{}.graphml'.format(args_dict['output']))


if __name__ == '__main__':
    main()
