from collections import Counter


def longestSubstring(s: str, k: int) -> int:
    counter = Counter(s)
    unique_char = len(counter)
    res = 0

    for currUnique in range(1, unique_char + 1):
        char_counter = [0] * 26
        start = 0
        end = 0
        unique = 0
        countAtLeastK = 0
        index = 0

        while end < len(s):
            if unique <= currUnique:
                index = ord(s[end]) - ord('a')
                if char_counter[index] == 0:
                    unique += 1
                char_counter[index] += 1
                if char_counter[index] == k:
                    countAtLeastK += 1
                end += 1
            else:
                index = ord(s[start]) - ord('a')
                if char_counter[index] == k:
                    countAtLeastK -= 1
                char_counter[index] -= 1
                if char_counter[index] == 0:
                    unique -= 1
                start += 1

            if unique == currUnique and unique == countAtLeastK:
                res = max(res, end - start)

    return res


