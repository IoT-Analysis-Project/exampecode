# Minimum adımları bulmak için bir fonksiyon
def enKısaYol(matris, k):
 
    # Matrisin satır ve sütun sayısını alın
    n = len(matris)
    m = len(matris[0])
    
    # Eğer matris tek elemandan oluşuyorsa ve bu eleman 0 veya k'nın değeri 1'den büyükse, 0 dön
    if (n == 1 and m == 1 and (matris[0][0] == 0 or k >= 1)):
        return 0
 
    # Ziyaret edildi bilgisini saklamak için bir 3D dizi oluşturun
    ziyaretEdildi = [[[False for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    
    # Adım sayısını 0 olarak başlatın
    adım = 0
 
    # Bir kuyruk oluşturun ve başlangıç noktasını ekleyin
    q = []
    q.append([0, 0, k])
 
    # İleri, geri, sağ ve sol hareketleri temsil eden diziler
    ar1 = [1, -1, 0, 0]
    ar2 = [0, 0, -1, 1]
 
    # BFS işlemini gerçekleştirin
    while (len(q) != 0):
        boyut = len(q)
 
        # Her seferinde bir adım artırın
        adım += 1
        
        while (boyut):
            # Kuyruğun ilk elemanını alın
            mevcut = q.pop(0)
            i = mevcut[0]
            j = mevcut[1]
            w = mevcut[2]
 
            # Ziyaret edildi olarak işaretle
            ziyaretEdildi[i][j][w] = True
            
            # Dört yönde döngü yaparak hareket edin
            for yon in range(0, 4):
                yeni_x = i + ar1[yon]
                yeni_y = j + ar2[yon]
                yeni_k = w
                
                # Eğer yeni konum geçerliyse
                if (yeni_x >= 0 and yeni_x < n and yeni_y >= 0 and yeni_y < m):
                    # Yeni konumda engel yoksa ve daha önce ziyaret edilmemişse
                    if (matris[yeni_x][yeni_y] == 0 and (not ziyaretEdildi[yeni_x][yeni_y][yeni_k])):
                        # Eğer yeni konum hedef konumsa, adım sayısını dön
                        if (yeni_x == n - 1 and yeni_y == m - 1):
                            return adım
                        q.append([yeni_x, yeni_y, yeni_k])
                        ziyaretEdildi[yeni_x][yeni_y][yeni_k] = True
                    # Eğer yeni konum engelse ve k'nın değeri 1'den büyükse
                    elif (matris[yeni_x][yeni_y] == 1 and yeni_k >= 1 and (not ziyaretEdildi[yeni_x][yeni_y][yeni_k - 1])):
                        # Eğer yeni konum hedef konumsa, adım sayısını dön
                        if (yeni_x == n - 1 and yeni_y == m - 1):
                            return adım
                        q.append([yeni_x, yeni_y, yeni_k - 1])
                        ziyaretEdildi[yeni_x][yeni_y][yeni_k - 1] = True
            boyut -= 1
    # Son konuma ulaşılamıyorsa -1 dön
    return -1
 
# Ana kod
if __name__ == "__main__":
 
    matris = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    K = 1
 
    # Fonksiyon çağrısı
    print(enKısaYol(matris, K))
