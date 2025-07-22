def compute_lps(pattern):
    """
    Computes the Longest Prefix Suffix (LPS) array for the given pattern.
    lps[i] stores the length of the longest proper prefix of pattern[0..i]
    that is also a suffix of pattern[0..i].
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # Length of the previous longest prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """
    Searches for occurrences of 'pattern' in 'text' using the Knuth-Morris-Pratt algorithm.
    Returns a list of starting indices where 'pattern' is found in 'text'.
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []

    lps = compute_lps(pattern)
    match_indices = []
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            match_indices.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return match_indices


if __name__ == "__main__":
    # Test suite
    print("Running KMP String Matching tests...")
    
    # Test Case 1: Standard match
    text1 = "ABABDABACDABABCABAB"
    pattern1 = "ABABCABAB"
    expected1 = [10]
    assert kmp_search(text1, pattern1) == expected1, f"Failed Test 1: {kmp_search(text1, pattern1)}"
    
    # Test Case 2: Multiple occurrences
    text2 = "AAAAA"
    pattern2 = "AA"
    expected2 = [0, 1, 2, 3]
    assert kmp_search(text2, pattern2) == expected2, f"Failed Test 2: {kmp_search(text2, pattern2)}"
    
    # Test Case 3: No match
    text3 = "ABCDEF"
    pattern3 = "XYZ"
    expected3 = []
    assert kmp_search(text3, pattern3) == expected3, f"Failed Test 3"
    
    # Test Case 4: Pattern longer than text
    text4 = "ABC"
    pattern4 = "ABCD"
    expected4 = []
    assert kmp_search(text4, pattern4) == expected4, f"Failed Test 4"

    # Test Case 5: Empty pattern or text
    assert kmp_search("ABC", "") == []
    assert kmp_search("", "ABC") == []
    
    print("All KMP tests passed successfully!")
