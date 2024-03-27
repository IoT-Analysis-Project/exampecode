# Belirli bir düğümün seviyesini bulma fonksiyonu
def dugumSeviyesiBul(N, kenarlar, X):
    # Grafın maksimum düğümünü saklamak için değişken
    maksDugum = 0

    # Kenarları döngüye alarak maksimum düğümü bul
    for kenar in kenarlar:
        maksDugum = max(maksDugum, max(kenar[0], kenar[1]))
     
    # Düğümler arasındaki bağlantıları saklamak için bir liste oluştur
    komsular = [[] for _ in range(maksDugum + 1)]
    
    # Kenarları kullanarak bağlantı listesini oluştur
    for kenar in kenarlar:
        komsular[kenar[0]].append(kenar[1])
        komsular[kenar[1]].append(kenar[0])
     
    # Eğer belirtilen düğüm (X) maksimum düğümden büyükse veya bağlantısı yoksa -1 döndür
    if X > maksDugum or len(komsular[X]) == 0:
        return -1
     
    # Genişlik Öncelikli Arama (BFS) için bir kuyruk oluştur
    kuyruk = []
    kuyruk.append(0)
    seviye = 0
     
    # Zaten ziyaret edilmiş düğümleri işaretlemek için bir ziyaret listesi oluştur
    ziyaret = [0] * (maksDugum + 1)
    ziyaret[0] = 1
     
    # BFS algoritması
    while len(kuyruk) > 0:
        boyut = len(kuyruk)
        while boyut > 0:
            suankiDugum = kuyruk[0]
            kuyruk.pop(0)
            if suankiDugum == X:
                return seviye
            for komsu in komsular[suankiDugum]:
                if not ziyaret[komsu]:
                    kuyruk.append(komsu)
                    ziyaret[komsu] = 1
            boyut -= 1
        seviye += 1
         
    return -1

# Test verileri
N = 5
kenarlar = [[0, 1], [0, 2], [1, 3], [2, 4]]
X = 3

# Fonksiyon çağrısı ve sonucun yazdırılması
seviye = dugumSeviyesiBul(N, kenarlar, X)
print(seviye)
