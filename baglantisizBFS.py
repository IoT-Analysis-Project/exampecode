import queue  # Kuyruk veri yapısını kullanabilmek için 'queue' modülünü içe aktarır.

def kenar_ekle(kenarlar, ilk, son): 
    # 'kenarlar' matrisine kenar ekleyen fonksiyon. İlk düğümden ikinci düğüme bir kenar ekler.
    kenarlar[ilk][son] = 1
  
def bfs_yazdir(kenarlar, V, baslangic, ziyaret_edildi): 
    # BFS (Genişlik Öncelikli Arama) kullanarak grafı dolaşan ve düğümleri yazdıran fonksiyon.
    if V == 0: 
        return
    bfs = queue.Queue()  # BFS sırasında kullanılacak bir kuyruk oluşturur.
    bfs.put(baslangic)  # Başlangıç düğümünü kuyruğa ekler.
    ziyaret_edildi[baslangic] = 1  # Başlangıç düğümünü ziyaret edilmiş olarak işaretler.
    while not bfs.empty():  # Kuyruk boş olana kadar döngüyü çalıştırır.
        data = bfs.get()  # Kuyruktan bir düğüm alır.
        print(data, end=' ')  # Alınan düğümü yazdırır.
        for i in range(V):  # Tüm düğümleri kontrol etmek için bir döngü başlatır.
            if kenarlar[data][i] == 1:  # Eğer düğümün komşusu ise...
                if ziyaret_edildi[i] == 0:  # Komşu düğüm daha önce ziyaret edilmemişse...
                    bfs.put(i)  # Komşu düğümü kuyruğa ekler.
                    ziyaret_edildi[i] = 1  # Komşu düğümü ziyaret edilmiş olarak işaretler.
  
def bfs_yardimci(kenarlar, V): 
    # Grafı BFS algoritması kullanarak dolaşan ve her düğümü ziyaret eden yardımcı fonksiyon.
    if V == 0: 
        return
    ziyaret_edildi = [0] * V  # Ziyaret edilen düğümleri tutan bir liste oluşturur.
    for i in range(V):  # Tüm düğümleri kontrol etmek için bir döngü başlatır.
        if ziyaret_edildi[i] == 0:  # Düğüm daha önce ziyaret edilmemişse...
            bfs_yazdir(kenarlar, V, i, ziyaret_edildi)  # BFS fonksiyonunu çağırarak düğümü ziyaret eder.
  
if __name__ == "__main__": 
    V = 5  # Grafın düğüm sayısı
    E = 6  # Grafın kenar sayısı
    if E == 0:  # Eğer grafın kenar sayısı 0 ise...
        for i in range(V): 
            print(i, end=' ')  # Düğümleri tek tek yazdırır.
        exit()  # Programdan çıkar.
  
    kenarlar = [[0 for _ in range(V)] for _ in range(V)]  # Grafı temsil eden bir matris oluşturur.
  
    # Kenarları ekler
    kenar_ekle(kenarlar, 0, 4) 
    kenar_ekle(kenarlar, 1, 2) 
    kenar_ekle(kenarlar, 1, 3) 
    kenar_ekle(kenarlar, 1, 4) 
    kenar_ekle(kenarlar, 2, 3) 
    kenar_ekle(kenarlar, 3, 4) 
  
    # BFS algoritmasıyla grafı dolaşır ve düğümleri ziyaret eder.
    bfs_yardimci(kenarlar, V)  
