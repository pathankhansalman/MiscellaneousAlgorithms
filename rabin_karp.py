# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 2026

@author: Antigravity
"""

from typing import List

def rabin_karp_search(pattern: str, text: str, prime: int = 101) -> List[int]:
    """
    Searches for occurrences of a pattern in a text using the Rabin-Karp algorithm.
    
    Args:
        pattern: The substring to search for.
        text: The string to search within.
        prime: A prime number to use for hashing (default 101).
        
    Returns:
        A list of starting indices where the pattern is found in the text.
    """
    m = len(pattern)
    n = len(text)
    indices = []
    
    if m == 0 or n < m:
        return indices
        
    d = 256  # Number of characters in the input alphabet
    p_hash = 0  # Hash value for pattern
    t_hash = 0  # Hash value for text
    h = 1
    
    # The value of h would be "pow(d, m-1) % prime"
    for i in range(m - 1):
        h = (h * d) % prime
        
    # Calculate the hash value of pattern and first window of text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime
        
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if the hash values of current window of text and pattern match
        if p_hash == t_hash:
            # Check for characters one by one
            if text[i : i + m] == pattern:
                indices.append(i)
                
        # Calculate hash value for next window of text: Remove leading digit,
        # add trailing digit
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            # We might get negative value of t_hash, converting it to positive
            if t_hash < 0:
                t_hash = t_hash + prime
                
    return indices

if __name__ == "__main__":
    test_text = "GEEKS FOR GEEKS"
    test_pattern = "GEEK"
    
    print("Running Rabin-Karp string matching algorithm test...")
    results = rabin_karp_search(test_pattern, test_text)
    print(f"Text: '{test_text}'")
    print(f"Pattern: '{test_pattern}'")
    print(f"Pattern found at indices: {results}")
