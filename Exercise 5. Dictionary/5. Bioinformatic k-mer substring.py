def k_mer(dna, k):
    res = {}
    for i in range(len(dna) + 1 - k):
        res.setdefault(dna[i:i+k], 0)
        res[dna[i:i+k]] += 1
    return res


print(k_mer("ATGCATGCGTCGAGTCTGA", 2))
# the dna can actually be a sentence or anything else,
# the working principle is the same, return a dict of k-substrings and their counts
