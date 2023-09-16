# Huffman and Lempel-Ziv

## Project Description
- This project is an implementation and comparison of Huffman and LZW compression algorithms
- Inputs are text or data files and outputs are their compressed versions
- Aim is to achieve compression rates of at least 40% to 60%
- Project is written in Python and the project language is English

## Overview of the selected algorithms
- Both are lossless compression techniques
- Huffman compresses data by assigning prefix codes to frequently used characters based on their occurrence using a binary tree
- Huffman time complexity is O(n log n) with its basic implementation and needs memory to store a tree structure that grows linearly with the size of the input
- Lempel-Ziv compresses data by referencing earlier sequences and building a dictionary that captures recurring patterns in the input, particular version of the Lempel-Ziv used is LZW. LZW replaces repeating sequences with a single code that references the dictionary.
- LZW time complexity is linear or slighly more and needs memory to store a dictionary that generally grows linearly with the size of the input until the dictionary is full

## Reviewed material

- https://en.wikipedia.org/wiki/Lossless_compression
- https://en.wikipedia.org/wiki/Huffman_coding
- https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
- https://rosettacode.org/wiki/Huffman_coding 
- https://en.wikipedia.org/wiki/LZ77_and_LZ78
- https://www.cs.helsinki.fi/group/pads/lz77.html
- https://rosettacode.org/wiki/LZW_compression
- https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-wusp/fb98aa28-5cd7-407f-8869-a6cef1ff1ccb

# Other
- Study program: Tietojenkäsittelytieteen kandiohjelma
- My programming languages: Mainly Python, NodeJS and frontend frameworks, somewhat familiar with Java having done some projects with it
