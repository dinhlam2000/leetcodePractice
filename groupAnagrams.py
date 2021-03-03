from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for w in strs:
        groups[tuple(sorted(w))].append(w)

    return [list(a) for a in groups.values()]

if __name__ == "__main__":
    import pdb; pdb.set_trace()

    groupAnagrams(["eat","tea","tan","ate","nat","bat"])