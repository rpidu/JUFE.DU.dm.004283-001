#!/bin/bash
import csv
import random

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y'])
    for _ in range(10000):
        writer.writerow([random.uniform(0, 1), random.uniform(0, 1)])

print("data.csv generated with 10,000 rows")