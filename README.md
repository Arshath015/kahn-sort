# Topological Sort via Kahn's Algorithm

[![Build Status](https://travis-ci.org/travis-ci/travis-web.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Topological sort on Directed Acyclic Graphs (DAGs) using Kahn's algorithm.

## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Documentation](#documentation)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)

## Overview
This is a command-line tool for performing topological sort on DAGs using Kahn's algorithm.

## Tech Stack
* Python 3.x
* argparse
* collections

## Architecture
```
+---------------+
|  CLI Entry  |
+---------------+
        |
        |
        v
+---------------+
|  Argument    |
|  Parsing      |
+---------------+
        |
        |
        v
+---------------+
|  Graph        |
|  Construction |
+---------------+
        |
        |
        v
+---------------+
|  Topological  |
|  Sort         |
+---------------+
        |
        |
        v
+---------------+
|  Result       |
|  Output       |
+---------------+
```

## Theoretical Background
Kahn's algorithm is a popular method for performing topological sort on DAGs. It works by maintaining a queue of vertices with no incoming edges and repeatedly removing vertices from the queue and adding them to the sorted list. The algorithm terminates when the queue is empty or when a cycle is detected.

## Installation
To install the required dependencies, run the following command:
pip install -r requirements.txt
git clone https://github.com/your-username/kahn-sort.git

## Usage
To use the tool, run the following command:
python cli.py --vertices 6 --edges '5 2' '5 0' '4 0' '4 1' '2 3' '3 1'

## API Reference
* `Graph` class: represents a directed graph with `num_vertices` vertices and `adj_list` adjacency list
* `add_edge` method: adds an edge between two vertices
* `topological_sort` function: performs topological sort on the graph and returns the sorted list of vertices

## Documentation
For more information, see [docs/analysis.md](docs/analysis.md)

## Testing
To run the tests, navigate to the `tests` directory and run the following command:
pytest

## Limitations
This implementation assumes that the input graph is a DAG. If the graph contains a cycle, the algorithm will terminate with an error.

## Roadmap
* Add support for weighted graphs
* Implement other topological sort algorithms

## License
This project is licensed under the MIT License