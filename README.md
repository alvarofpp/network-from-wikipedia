# Network from Wikipedia
`to_graphml.py` may be used to constructing a network from wikipedia pages.
This script is based on Colab from [ivanovitchm/network_analysis](https://github.com/ivanovitchm/network_analysis) (Week 07 Directed networks: case study of Wikipedia pages).
Output file example [here](output.graphml).

## Requirements
The script is written in Python. Dependant packages can be installed via:

```shell
pip install -r requirements.txt
```

## How to run
Run `to_graphml.py` providing:

| Argument | Required | Description | Default value |
| -------- | -------- | ----------- | ------------- |
| `-s`, `--source` | Yes | Url or title from Wikipedia. | |
| `-d`, `--degree` | No | Number of degree that will be used in the filter of nodes. Equal to or greater than this value. | `2` |
| `-l`, `--layers` | No | Number of search layers. | `2` |
| `-o`, `--output` | No | Output filename. | `'output'` |
| `-t`, `--threads` | No | Number of threads that will be used. | `-1` |
| `-v`, `--verbose` | No | Increase output verbosity. | `False` |

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
Contributions are more than welcome. Fork, improve and make a pull request. For bugs, ideas for improvement or other, please create an [issue](https://github.com/alvarofpp/dataset-network-from-wikipedia/issues).

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
