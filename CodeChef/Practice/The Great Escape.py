import sys
import collections

def bidirectional_bfs(graph, S, T):
    if S == T:
        return 0
    n = len(graph) - 1
    distS = [-1] * (n + 1)
    distT = [-1] * (n + 1)
    qs = collections.deque([S])
    qt = collections.deque([T])
    distS[S] = 0
    distT[T] = 0
    
    while qs and qt:
        if len(qs) <= len(qt):
            for _ in range(len(qs)):
                u = qs.popleft()
                for v in graph[u]:
                    if distS[v] == -1:
                        distS[v] = distS[u] + 1
                        qs.append(v)
                        if distT[v] != -1:
                            return distS[v] + distT[v]
        else:
            for _ in range(len(qt)):
                u = qt.popleft()
                for v in graph[u]:
                    if distT[v] == -1:
                        distT[v] = distT[u] + 1
                        qt.append(v)
                        if distS[v] != -1:
                            return distS[v] + distT[v]
    return 0

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    # Build the graph.
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u = int(next(it))
        v = int(next(it))
        graph[u].append(v)
        graph[v].append(u)
    
    S = int(next(it))
    T = int(next(it))
    
    result = bidirectional_bfs(graph, S, T)
    print(result)

if __name__ == '__main__':
    main()