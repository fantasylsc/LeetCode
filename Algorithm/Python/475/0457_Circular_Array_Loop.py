class Solution1:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = {}

        for i in range(n):
            if i in visited:
                continue
            visited[i] = 1
            curr = i
            m = {}

            while True:
                next = ((curr + nums[curr]) % n + n) % n
                if next == curr or nums[next] * nums[curr] < 0:
                    break
                if next in m:
                    return True

                m[curr] = next
                curr = next
                visited[next] = 1

        return False


# slow fast pointer

class Solution2:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getNext(nums, i):
            n = len(nums)
            return ((nums[i] + i) % n + n) % n

        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = getNext(nums, i)
            val = nums[i]

            while val * nums[fast] > 0 and val * nums[getNext(nums, fast)] > 0:
                if slow == fast:
                    if slow == getNext(nums, slow):
                        break
                    return True

                slow = getNext(nums, slow)
                fast = getNext(nums, getNext(nums, fast))

            slow = i
            while val * nums[slow] > 0:
                next = getNext(nums, slow)
                nums[slow] = 0
                slow = next

        return False
