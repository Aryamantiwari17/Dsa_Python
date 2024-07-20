from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py3
            
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_connection_input(n):
    connections = []
    print("Enter the connections (one per line, space-separated):")
    for _ in range(n):
        while True:
            try:
                connection = list(map(int, input().split()))
                if len(connection) != 2:
                    print("Invalid connection format. Please enter two space-separated integers.")
                else:
                    connections.append(connection)
                    break
            except ValueError:
                print("Invalid input. Please enter space-separated integers.")
    return connections

def get_query_input(q):
    queries = []
    print("Enter the queries (one per line, space-separated):")
    for _ in range(q):
        while True:
            try:
                query = list(map(int, input().split()))
                if len(query) != 2:
                    print("Invalid query format. Please enter two space-separated integers (query type and pod ID).")
                else:
                    queries.append(query)
                    break
            except ValueError:
                print("Invalid input. Please enter space-separated integers.")
    return queries

def recoverDeadPods(pods: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
    uf = UnionFind(pods + 1)  # +1 because pod IDs start from 1
    active_pods = set(range(1, pods + 1))
    
    # Connect pods based on given connections
    for a, b in connections:
        uf.union(a, b)
    
    results = []
    
    for query_type, pod_id in queries:
        if query_type == 1:  # Data-sending query
            if pod_id not in active_pods:
                results.append(-1)
                continue
            
            region = uf.find(pod_id)
            min_active_pod = min(active_pods, key=lambda x: (uf.find(x) == region, x != pod_id, x))
            
            results.append(min_active_pod)
        
        else:  # Database-connection-failure query
            active_pods.discard(pod_id)
    
    return results

def main():
    pods = get_int_input("Enter the number of pods: ")
    n = get_int_input("Enter the number of connections: ")
    connections = get_connection_input(n)
    q = get_int_input("Enter the number of queries: ")
    queries = get_query_input(q)

    # Get the results
    results = recoverDeadPods(pods, connections, queries)
    
    # Output the results
    print("Results:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()