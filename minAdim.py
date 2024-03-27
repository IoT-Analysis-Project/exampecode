# Minimum adımları bulmak için bir fonksiyon
def getMinMoves(N, K, nums):
 
    # Sağdaki sonraki daha büyük elemanı depolar
    nger = [0 for _ in range(N)]
    s = []
 
    # nger vektörünü doldurmak için döngü
    for i in range(N-1, -1, -1):
        while (len(s) != 0 and nums[s[len(s) - 1]] <= nums[i]):
            s.pop()
 
        if (len(s) == 0):
            nger[i] = -1
 
        else:
            nger[i] = s[len(s) - 1]
 
        s.append(i)
 
    while (len(s) != 0):
        s.pop()
 
    # Soldaki sonraki daha büyük elemanı depolar
    ngel = [0 for _ in range(N)]
 
    # ngel vektörünü doldurmak için döngü
    for i in range(0, N):
 
        while(len(s) != 0 and nums[s[len(s) - 1]] <= nums[i]):
            s.pop()
 
        if (len(s) == 0):
            ngel[i] = -1
 
        else:
            nger[i] = s[len(s) - 1]
 
        s.append(i)
 
    # BFS için bir çift kuyruk alırız. Çiftin ilk elemanı indeks, ikincisi başlangıç indeksinden o indekse ulaşmak için minimum adımları içerir.
    q = []
    q.append([K, 0])
    visited = [False for _ in range(N)]
    visited[K] = True
 
    # BFS işlemi gerçekleştirilir
    while (len(q) != 0):
        par = q[0]
        q.pop(0)
 
        # Eğer son indeks bulunduysa minimum adımları döndür
        currentIndex = par[0]
        minimumAdımlar = par[1]
        if (currentIndex == N - 1):
            return minimumAdımlar
 
        child1 = ngel[currentIndex]
        child2 = nger[currentIndex]
        if (child1 != -1 and (not visited[child1])):
            q.append([child1, minimumAdımlar + 1])
            visited[child1] = True
 
        if (child2 != -1 and not visited[child2]):
            q.append([child2, minimumAdımlar + 1])
            visited[child2] = True
 
    # Son indekse ulaşılamadıysa -1 döndür
    return -1
 
# Ana kod
if __name__ == "__main__":
 
    N, K = 0, 0
    nums = [0, -1, 2]
    N = len(nums)
 
    # Fonksiyon çağrısı
    minAdımlar = getMinMoves(N, K, nums)
    print(minAdımlar)
