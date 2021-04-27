def largest_proper_prefix_suffix(s):
    print(s)
    lps = [0] * len(s) # Longest proper Prefix which is also Suffix

    i = 1
    j = 0
    while (i < len(s)):
        if (s[i] == s[j]):
            lps[i] = j + 1
            i += 1
            j += 1
        elif (j != 0):
            j = lps[j - 1] # go backwards
        else:
            lps[i] = 0
            i += 1

    return lps 

def kmp(string, pattern):
    """
    Use KMP algorithm to find all occurences
    of `pattern` in `string`.
    """
    lps = largest_proper_prefix_suffix(pattern)
    j = 0
    i = 0
    all_occurences = []
    while (i < len(string)):
        if (string[i] == pattern[j]):
            j += 1
            i += 1
            if (j == len(pattern)):
                # Match found
                all_occurences.append(i - len(pattern))
                j = lps[j - 1] 
        else:
            # Find all matching (prefix&suffix)s
            if (j != 0):
                j = lps[j - 1]
            else:
                i += 1

    
    return all_occurences

