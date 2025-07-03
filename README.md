# terminal-plotter

![obrazek](https://github.com/user-attachments/assets/63e795f4-c55f-44f6-a523-108c2b164869)

Plot ascii art-style graphs in your terminal!

## Features:

- Adjustable dimensions for the plotted graph
- Choice of different axis scaling methods (linear, logarithmic, quadratic...)
- .csv input for easy data imports
- Labels for x and y axis

## Specific options:
(these options are applicable to `termgraph.py` only)

- `--old-parse` use old parsing (each line from the csv is a dataset of its own, new parsing has each new csv column as a dataset)
- `--y-space` space available for graph output in characters
- `--csv-points` only available with new parsing, shows exact points rather than bars in the graph output