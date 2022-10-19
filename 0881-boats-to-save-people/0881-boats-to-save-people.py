class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r = 0,len(people)-1
        res = 0
        people.sort()
        while r >= l:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                r -= 1
                l += 1
            res += 1
        return res