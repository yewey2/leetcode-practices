from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        ## start time: 0948
        ## most optimal path will NOT traverse same node again
        ## this means we can create the same paths, with the double weights backwards.
        for i in range(len(edges)):
            u,v,w = edges[i]
            edges.append([v,u,w*2])
        print('add edge opk')
        ## now we have all the edges
        ## traverse as pernormal
        # create a hashmap first so we can check easily?
        edgemap = {}
        ## pause time: 0953
        for u,v,w in edges:
            ## continue time:0958
            if not edgemap.get(u):
                edgemap[u]=[]
            edgemap[u].append((v, w))
        print('edge map created ok')
        # ## if not in edgemap, means cannot traverse
        # if n-1 not in edgemap.keys() or 0 not in edgemap.keys():
        #     return -1
        # ## now, we need create cost map
        # # costmap = {} ## this is my visited map below
        # ## pause 1000
        # # start 2132
        # # visitedmap = {}
        # visitedmap = {0: 0}
        # tovisit = set()
        # for x,w in edgemap[0]:
        #     tovisit.add((0,x,w))
        # print('tovisit ok')
        # def visit(v, u, w):
        #     # tovisit.remove(v)
        #     if v in visitedmap:
        #         # return min(visitedmap[v], w+visitedmap[u])
        #         if visitedmap[v] > w+visitedmap[u]:
        #             for x,w in edgemap[v]:
        #                 tovisit.add((v,x,w))
        #         return min(visitedmap[v], visitedmap[u]+w)
        #     visitedmap[v] = visitedmap[u] + w
        #     for x,w in edgemap[v]:
        #         tovisit.add((v,x,w))
        #     return visitedmap[v]
        # while tovisit:
        #     x,v,w = tovisit.pop()
        #     print('tovisitnow:', x,v,w)
        #     visit(x,v,w)
        #     if n-1 in visitedmap:
        #         return visitedmap[n-1]
        # return -
        ## RESTART: time = 2204
        costmap = {0: 0}
        visited_edges = set([0])
        while n-1 not in costmap:
            all_edges_to_visit = set()
            for u in costmap:
                for v, w in edgemap[u]:
                    all_edges_to_visit.add(v)
            # if not visited_edges - all_edges_to_visit:
            #     return -1
            xxx = set(costmap.keys())
            for u in xxx:
                for v,w in edgemap[u]:
                    if costmap.get(v):
                        costmap[v] = min(costmap[u] + w, v)
                    else:
                        costmap[v] = costmap[u] + w
            
        return costmap[n-1]
        ## end at 2213
        ## Did NOT succeed. to look through again with answers, and try again
