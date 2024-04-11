def similarPairs(words: list[str]) -> int:
    res = []
    pair_count = 0

    for word in words:
        res.append(set(word))

    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] == res[j]:
                pair_count += 1

    return pair_count


# print(similarPairs(["aabb", "ab", "ba"]))
print(similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
# print(similarPairs(["aabb", "ab", "ba"]))
