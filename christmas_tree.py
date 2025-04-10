#!/usr/bin/env python
# coding: utf-8

# In[1]:

from colorama import Fore
import random

def print_tree(n, f, ornaments_count):
    positions = []  # List to store positions where ornaments should be placed

    # Find possible positions to place ornaments (between stars)
    for i in range(n):
        for j in range(f):
            if (f // 2 - i) <= j <= (f // 2 + i):
                if (j - (f // 2 - i)) % 2 == 1:  # Odd positions will be for ornaments
                    positions.append((i, j))

    # Randomly select positions for ornaments, ensuring the correct number
    ornament_positions = random.sample(positions, min(ornaments_count, len(positions)))

    # Print the tree with the ornaments
    for i in range(0, n):
        for j in range(0, f):
            if i == 0 and f // 2 == j:
                print(Fore.YELLOW + "★", end="")  # Top star
            elif (f // 2 - i) <= j <= (f // 2 + i):  # Tree's width
                if (j - (f // 2 - i)) % 2 == 0:  # Green branches
                    print(Fore.GREEN + "*", end="")
                elif (i, j) in ornament_positions:  # Place ornaments
                    print(Fore.RED + "o", end="")
                else:  # Empty space between branches
                    print(Fore.WHITE + " ", end="")
            else:
                print(" ", end="")  # Outer spaces
        print()  # Newline after each row

    # Tree trunk
    for i in range(n // 4):
        print(Fore.RED + " " * (f // 2 - 1) + "|||")

    # Bottom line
    print(Fore.RED + " " * (f // 2 - 6) + "_ _ _|||_ _ _")

# Example usage
print_tree(12, 36, 10)





