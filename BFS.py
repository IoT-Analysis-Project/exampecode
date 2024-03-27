from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)  # Bir defaultdict kullanarak bir kenar listesi oluşturur.

    # Grafikte bir kenar ekler.
    def addEdge(self, u, v):
        self.adjList[u].append(v)

    # Breadth-First Search (BFS) algoritması
    def bfs(self, startNode):
        queue = deque()  # Bir deque (kuyruk) oluşturur.
        visited = [False] * (max(self.adjList.keys()) + 1)  # Ziyaret edilen düğümleri tutar.

        visited[startNode] = True  # Başlangıç düğümünü ziyaret edildi olarak işaretler.
        queue.append(startNode)  # Başlangıç düğümünü kuyruğa ekler.

        # BFS döngüsü
        while queue:
            currentNode = queue.popleft()  # Kuyruğun başından bir düğüm çıkarır.
            print(currentNode, end=" ")  # Çıkarılan düğümü yazdırır.

            # Çıkarılan düğümün komşularını kontrol eder.
            for neighbor in self.adjList[currentNode]:
                if not visited[neighbor]:  # Komşu düğüm ziyaret edilmemişse:
                    visited[neighbor] = True  # Ziyaret edildi olarak işaretler.
                    queue.append(neighbor)  # Kuyruğa ekler.

graph = Graph()

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(2, 4)

print("Breadth First Traversal starting from vertex 0:", end=" ")
graph.bfs(0)



