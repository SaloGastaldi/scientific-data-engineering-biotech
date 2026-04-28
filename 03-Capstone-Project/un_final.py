#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Technical Assessment: OOP, Memory Efficiency & Algorithmic Complexity.
This module explores advanced Python concepts including dunder methods, 
generators for memory optimization, and Big O analysis for sorting.
"""

class Lote:
    """
    Represents a batch of products (Stock Management).
    Demonstrates the use of dunder methods for professional object representation.
    """
    def __init__(self, name, units, price):
        self.name = name
        self.units = units
        self.price = price
    
    def __repr__(self):
        """Official string representation for debugging and developers."""
        return f'Lote({self.name!r}, {self.units}, {self.price})'
    
    def __str__(self):
        """User-friendly string representation."""
        return f'Lote: {self.name} | Units: {self.units} | Price: ${self.price:.2f}'
    
    def costo(self):
        """Calculates total cost of the batch."""
        return self.units * self.price
    
    def vender(self, n):
        """Decreases stock by n units."""
        if n <= self.units:
            self.units -= n
        else:
            raise ValueError("Insufficient stock to perform sale.")

# --- Section 1: Object Representation (Internal Logic) ---
# Difference between __str__ and __repr__:
# __str__ is for the end user (informational).
# __repr__ is for the developer (unambiguous, useful for debugging).

# --- Section 2: Memory Efficiency with Generators ---
def even_iterator(n):
    """
    Yields even numbers up to n.
    Uses 'yield' to create a generator, optimizing memory by not 
    storing the entire list in RAM.
    """
    for i in range(n):
        if i % 2 == 0:
            yield i

# Why does it only return 5 elements for n=10?
# Because generators are 'lazy iterators'. They produce values on the fly 
# and terminate once the loop condition is met, saving computational resources.

# --- Section 3: Algorithmic Complexity (Case Study) ---
"""
CASE STUDY: Selection Sort vs Merge Sort for Top-K Elements.
Scenario: Sequence S of 10^9 elements, need to find K=12 largest elements.

Analysis:
1. Merge Sort: 
   Complexity is O(N log N). For 1 billion elements, this requires a full 
   sorting of the entire dataset, which is computationally expensive.

2. Selection Sort (Partial):
   Complexity for finding K elements is O(K * N). 
   Since K (12) is significantly smaller than log N (log2(10^9) ≈ 30), 
   Selection Sort is more efficient here. It only performs K passes 
   over the data to find the top K, rather than sorting the entire billion elements.

Conclusion: 
For Top-K problems where K << N, a partial sort or a Heap-based approach 
is superior to a full sort like Merge Sort.
"""

if __name__ == "__main__":
    # Quick Test
    milote = Lote("Naranja", 100, 32.2)
    print(milote)  # Uses __str__
    
    print("\nIterating even numbers (Generator):")
    for val in even_iterator(10):
        print(val, end=" ")
    print()
