from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        n = len(s2)

        counter1 = Counter(s1)
        counter2 = Counter(s2[0:m])

        if counter1 == counter2:
            return True

        for i in range(1, n - m + 1):
            counter2[s2[i - 1]] -= 1
            if counter2[s2[i - 1]] == 0:
                del counter2[s2[i - 1]]

            if s2[i + m - 1] in counter2:
                counter2[s2[i + m - 1]] += 1
            else:
                counter2[s2[i + m - 1]] = 1

            if counter1 == counter2:
                return True

        return False