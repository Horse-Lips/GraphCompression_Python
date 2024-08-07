#!/usr/bin/env python

"""
    Gaussian_test.py: Performs a set of tests for the Gaussian.py compress method
"""

from Gaussian import compress

__author__ = "Jake Haakanson"
__license__ = "MIT"


graph_small = [
    [0, 20, 0, 0, 50],
    [20, 0, 15, 10, 0],
    [0, 15, 0, 0, 0],
    [0, 10, 0, 0, 0],
    [50, 0, 0, 0, 0]
]

graph_small_compressed = [
    [0, 30, 50],
    [30, 0, 0],
    [50, 0, 0]
]

graph_small_terminals = [0, 3, 4]


def test_compress_small():
    assert compress(graph_small, graph_small_terminals) == graph_small_compressed
