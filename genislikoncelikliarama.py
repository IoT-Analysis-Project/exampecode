from collections import defaultdict

class Graf:
    def __init__(self):
        self.graf = defaultdict(list)

    # Grafa bir kenar eklemek için kullanılan metot
    def kenarEkle(self, u, v):
        self.graf[u].append(v)

    # Genişlik Öncelikli Arama (BFS) algoritmasını uygulayan metot
    def BFS(self, s):
        ziyaret_edildi = [False] * (max(self.graf.keys()) + 1)  # Ziyaret durumunu tutan bir dizi oluştur

        kuyruk = []  # BFS sırasında kullanılacak kuyruk

        kuyruk.append(s)  # Başlangıç düğümünü kuyruğa ekle
        ziyaret_edildi[s] = True  # Başlangıç düğümünü ziyaret edilmiş olarak işaretle

        while kuyruk:
            s = kuyruk.pop(0)  # Kuyruktan bir düğüm çıkar

            # Çıkarılan düğümü yazdır
            print(s, end=' ')

            # Çıkarılan düğümün komşularını kontrol et
            for i in self.graf[s]:
                if ziyaret_edildi[i] == False:  # Komşu düğüm ziyaret edilmemişse
                    kuyruk.append(i)  # Kuyruğa ekle
                    ziyaret_edildi[i] = True  # Ziyaret edilmiş olarak işaretle

# Ana kod bölümü
if __name__ == '__main__':
    
    # Örnek bir graf oluştur
    g = Graf()
    g.kenarEkle(0, 1)
    g.kenarEkle(0, 2)
    g.kenarEkle(1, 2)
    g.kenarEkle(2, 0)
    g.kenarEkle(2, 3)
    g.kenarEkle(3, 3)
 
    # Grafın BFS sırasını yazdır
    print("Başlangıç düğümü 2 olan Genişlik Öncelikli Arama (Breadth First Search) sırası:")
    g.BFS(2)
