class Solution:
    def __init__(self):
        self.hash = {}
    
    def domino(self, n):
        if n == 1: return 1
        elif n == 2: return 2
        elif n not in self.hash:
            self.hash[n] = self.domino(n - 1) + self.domino(n - 2)
        return self.hash[n]

test = Solution()
print(test[1])