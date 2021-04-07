from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m = len(s1)
        n = len(s2)

        count1 = Counter(s1)
        count2 = Counter(s2[0:m])

        if count1 == count2:
            return True

        for i in range(n - m):
            count2[s2[i]] -= 1
            if count2[s2[i]] == 0:
                del count2[s2[i]]

            if s2[i + m] in count2:
                count2[s2[i + m]] += 1
            else:
                count2[s2[i + m]] = 1

            if count1 == count2:
                return True

        return False