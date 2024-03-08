import networkx as nx
import wikipedia

from utils.constants import SOURCE_URL, STOPS
from utils.helpers import check_source, print_if


def download(source: str = None,
             verbose: bool = False,
             layers: int = 2):
    # Check source
    code = check_source(source)
    if code == SOURCE_URL:
        source = source.split('/')[-1].replace('_', ' ')
    SEED = source.title()

    todo_lst = [(0, SEED)]  # The SEED is in the layer 0
    todo_set = set(SEED)  # The SEED itself
    done_set = set()  # Nothing is done yet
    graph = nx.DiGraph()
    layer, page = todo_lst[0]

    while layer < layers:
        # Remove the name page of the current page from the todo_lst,
        # and add it to the set of processed pages.
        # If the script encounters this page again, it will skip over it.
        del todo_lst[0]
        done_set.add(page)

        # Show progress
        print_if(verbose, layer, page)

        # Attempt to download the selected page.
        try:
            wiki = wikipedia.page(page)
        except Exception:
            layer, page = todo_lst[0]
            print_if(verbose, 'Could not load', page)
            continue

        for link in wiki.links:
            link = link.title()
            if link not in STOPS and not link.startswith('List Of'):
                if link not in todo_set and link not in done_set:
                    todo_lst.append((layer + 1, link))
                    todo_set.add(link)
                graph.add_edge(page, link)
        layer, page = todo_lst[0]
    return graph


def clean(graph):
    # Remove self loops
    graph.remove_edges_from(nx.selfloop_edges(graph))

    # Identify duplicates like that: 'network' and 'networks'
    duplicates = [
        (node, node + 's') for node in graph if node + 's' in graph
    ]

    for dup in duplicates:
        graph = nx.contracted_nodes(graph, *dup, self_loops=False)

    duplicates = [(x, y) for x, y in
                  [(node, node.replace('-', ' ')) for node in graph]
                  if x != y and y in graph]

    for dup in duplicates:
        graph = nx.contracted_nodes(graph, *dup, self_loops=False)

    # nx.contracted creates a new node/edge attribute called contraction
    # the value of the attribute is a dictionary, but GraphML
    # does not support dictionary attributes
    nx.set_node_attributes(graph, 0, 'contraction')
    nx.set_edge_attributes(graph, 0, 'contraction')

    return graph


def truncate(graph,
             verbose: bool = False,
             degree: bool = 2):
    # Filter nodes with degree greater than or equal to {degree}
    core = [node for node, deg in dict(graph.degree()).items() if deg >= degree]

    # Select a subgraph with 'core' nodes
    subgraph = nx.subgraph(graph, core)

    print_if(verbose, f'{len(subgraph)} nodes, {nx.number_of_edges(subgraph)} edges')

    return subgraph
