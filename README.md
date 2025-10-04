# terminal-plotter

![obrazek](https://github.com/user-attachments/assets/63e795f4-c55f-44f6-a523-108c2b164869)

Plot ascii art-style graphs in your terminal! Usage information and a better writeup are available in the [calc README](CALC_README.md)

## Video demo:

![Demo video showcasing the plotter function](https://github.com/strawberry-p/terminal-plotter/raw/refs/heads/main/demo.mp4)

## Features:

- Adjustable dimensions for the plotted graph
- Choice of different axis scaling methods (linear, logarithmic, quadratic...)
- .csv input for easy data imports
- Labels for x and y axis

## Installation

The package is [available on PyPI](https://pypi.org/project/hc-term-graph/). You can install it with `pip install hc-term-graph` or `pipx install hc-term-graph`
For other installation options, refer to the CALC_README.md file

## Specific options:
(these options are applicable to `termgraph.py` only)

- `--old-parse` use old parsing (each line from the csv is a dataset of its own, new parsing has each new csv column as a dataset)
- `--y-space` space available for graph output in characters
- `--csv-points` only available with new parsing, shows exact points rather than bars in the graph output
