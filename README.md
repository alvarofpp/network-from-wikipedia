# Network from Wikipedia
`to_graphml.py` may be used to constructing a network from wikipedia pages.
This script is based on Colab from [ivanovitchm/network_analysis](https://github.com/ivanovitchm/network_analysis) (Week 07 Directed networks: case study of Wikipedia pages).
Output file example [here](output.graphml).

The snowballing process will be initialized from your `source` argument. 

> "When you start the snowballing, you will eventually (and quite soon) bump into the pages describing ISBN and ISSN numbers, the arXiv, PubMed, and the like. Almost all other Wikipedia pages refer to one or more of those pages. This hyper-connectedness transforms any network into a collection of almost perfect gigantic stars, making all Wikipedia-based networks look similar. To avoid the stardom syndrome, treat the known 'star' pages as stop words in information retrieval—in other words, ignore any links to them.
Constructing the black list of stop words, STOPS, is a matter of trial and error. We put thirteen subjects on it; you may want to add more when you come across other “stars.” We also excluded pages whose names begin with "List of", because they are simply lists of other subjects." - Ivanovitch's jupyter notebook

You can change the `STOPS` words in [`constants.py`](https://github.com/alvarofpp/dataset-network-from-wikipedia/blob/main/utils/constants.py#L4).

## Requirements
The script is written in Python. Dependant packages can be installed via:

```shell
pip install -r requirements.txt
```

## How to run
Run `to_graphml.py` providing:

| Argument | Required | Description | Default value |
| -------- | -------- | ----------- | ------------- |
| `-s` <br/> `--source` | Yes | Url or title from Wikipedia. | - |
| `-d` <br/> `--degree` | No | Number of degree that will be used in the filter of nodes. Equal to or greater than this value. | `2` |
| `-l` <br/> `--layers` | No | Number of search layers. | `2` |
| `-o` <br/> `--output` | No | Output filename. | `'output'` |
| `-v` <br/> `--verbose` | No | Increase output verbosity. | `False` |

### Examples

Basic usage:
```shell
python3 to_graphml.py --source='Complex network'
# Or (tested only on `en.wikipedia`)
python3 to_graphml.py --source='https://en.wikipedia.org/wiki/Complex_network'
```

Verbose mode:
```shell
python3 to_graphml.py --source='Complex network' --verbose
```

Search deeper, filtering by more degree and changing the output file:
```shell
python3 to_graphml.py --source='Complex network' --layers=5 --degree=10 --output=graph_5l_10d
# The output file is `graph_5l_10d.graphml`
```

## Contributing
Contributions are more than welcome. Fork, improve and make a pull request.
For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/dataset-network-from-wikipedia/issues).

## License
This project is licensed under the GNU Affero General Public License - see
the [LICENSE.md](LICENSE) file for details.
