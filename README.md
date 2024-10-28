# DynamicMedianFinder

## Overview
This project implements a **dynamic median-finding algorithm** in Python using two heaps (`heapq`), optimized for online or real-time applications where new numbers are continuously added, and the median needs to be recalculated quickly.

## Features
- **Efficient Median Calculation:** Quickly find the median of a growing data stream.
- **Optimized Performance:** Uses a max-heap and min-heap to maintain balance, achieving O(log n) insertion and O(1) median retrieval.
- **Real-Time Updates:** Suitable for applications that require real-time median updates, like financial data analysis or telemetry systems.

## How It Works
The algorithm maintains two heaps:
1. **Max-heap** (`lower_half`): Contains the lower half of the numbers. Python's `heapq` is used with negated values to simulate a max-heap.
2. **Min-heap** (`upper_half`): Contains the upper half of the numbers.

After each addition, the heaps are balanced so their sizes differ by at most 1, allowing efficient retrieval of the median:
- If the sizes of both heaps are equal, the median is the average of the two middle elements.
- Otherwise, the median is the root of the max-heap (`lower_half`).

## Usage

```python
from median_finder import MedianFinder

median_finder = MedianFinder()

# Adding numbers and retrieving the median
median_finder.add_number(5)
print(median_finder.get_median())  # Outputs 5.0

median_finder.add_number(10)
print(median_finder.get_median())  # Outputs 7.5

median_finder.add_number(3)
print(median_finder.get_median())  # Outputs 5.0
