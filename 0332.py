class Solution:
    def findItinerary(self, tickets):
        self.forward = {}
        for ticket in tickets:
            start, end = tuple(ticket)
            if start not in self.forward:
                self.forward[start] = []
            self.forward[start].append(end)

        for city in self.forward:
            self.forward[city].sort()

        self.result = []
        self.DFS("JFK")

        return self.result[::-1]

    def DFS(self, start):
        end_locations = self.forward[start]
        while end_locations:
            next = end_locations.pop()
            self.DFS(next)
        self.result.append(start)