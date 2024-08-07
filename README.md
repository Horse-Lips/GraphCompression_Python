# GraphCompression_Python
Graph compression algorithms written in Python. Each file contains a compress function that takes expects a graph as a weight matrix and a set of terminals as a list of ints.
```
graph = [
  [0,  20, 0,  0,  50],
  [20, 0,  15, 10, 0 ],
  [0,  15, 0,  0,  0 ],
  [0,  10, 0,  0,  0 ],
  [50, 0,  0,  0,  0 ]
]

terminals = [0, 3, 4]
```

## src/Gaussian.py
Compresses the graph using the Gaussian elimination method. In this method, non-terminals are removed and edges are created between each pair of neighbours. Existing edges are replaced by a shorter edge if possible.
