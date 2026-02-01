from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ## start 7.36pm
        ## feels like a graph problem?
        ## start node to end node, find the minimum cost path for ALL of the starts and ends
        ## sum of graph traversal
        ## gemini says use floyd warshall
        ## naive is one by one djikstra
        ## even more naive is DFS with cache. 

        ## floyd warshall is just creating a 26x26 map, then update ALL of the maps. 
        d = {}
        for i in range(26):
            for j in range(26):
                d[(i,j)] = 10**7 ## use the max for cost
        start_index = ord('a')
        for o,ch,co in zip(original, changed, cost):
            ## now update the entire table
            d[(ord(o) - start_index, ord(ch)-start_index)] = min(d[(ord(o) - start_index, ord(ch)-start_index)], co)

        ## for every i, j, and intermediary k: can i find a path that pass through node k?
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    d[(i,j)] = min(d[(i,j)], d[(i,k)] + d[(k,j)])
        total_cost = 0
        for s,t in zip(source, target):
            if s==t: continue
            s, t = ord(s)- start_index, ord(t) - start_index
            if d[(s,t)] >= 10**7:
                # print(s, t, 'not compatible')
                return -1
            total_cost += d[(s,t)]
        return total_cost
        ## stop 7.52. checked answer ok
