# Minimum sıçramaları hesaplamak için bir fonksiyon
def sıçramalarıAzalt(dizi):
    n = len(dizi)
     
    # Benzer değerlerin dizinleriyle eşleşen bir harita için başlangıç
    eşleme = {}
     
    # Dizi elemanlarını dizinleriyle eşleştirme
    for i in range(n):
        if dizi[i] in eşleme:
            eşleme.get(dizi[i]).append(i)
        else:
            eşleme.update({dizi[i]: [i]})
     
    q = []
    ziyaretEdildi = [False] * n
     
    # Başlangıç elemanını kuyruğa ekleyip ziyaret edildi olarak işaretleyin
    q.append(0)
    ziyaretEdildi[0] = True
     
    # Son dizine ulaşmak için minimum geçerli sıçramaların sayısını saymak için bir sayaç başlatın
    sayac = 0
     
    # Kuyruk boyutu 0'dan büyük olduğu sürece döngüyü devam ettirin
    while(len(q) > 0):
        boyut = len(q)
         
        # Kuyruktaki tüm elemanlar üzerinde döngü yapın
        for i in range(boyut):
            # Ön sıradaki elemanı alın ve kuyruktan çıkarın
            mevcut = q[0]
            q.pop(0)
             
            # Eğer mevcut dizinin son dizini ise, sıçramaların yarısını döndürün
            if(mevcut == n - 1):
                return sayac // 2
             
            # Eğer mevcut + 1 geçerli bir pozisyon ise, ziyaret edilmiş olarak işaretleyin
            if(mevcut + 1 < n and ziyaretEdildi[mevcut + 1] == False):
                q.append(mevcut + 1)
                ziyaretEdildi[mevcut + 1] = True
             
            # Eğer mevcut - 1 geçerli bir pozisyon ise, ziyaret edilmiş olarak işaretleyin
            if(mevcut - 1 >= 0 and ziyaretEdildi[mevcut - 1] == False):
                q.append(mevcut - 1)
                ziyaretEdildi[mevcut - 1] = True
             
            # Şimdi, mevcut ile benzer olan tüm elemanları kontrol edin
            if dizi[i] in eşleme:
                for j in range(len(eşleme[dizi[mevcut]])):
                    cocuk = eşleme.get(dizi[mevcut])[j]
                    if(mevcut == cocuk):
                        continue
                     
                    # Eğer çocuk geçerli bir pozisyon ise, ziyaret edilmiş olarak işaretleyin
                    if(ziyaretEdildi[cocuk] == False):
                        q.append(cocuk)
                        ziyaretEdildi[cocuk] = True
             
            # Yukarıdaki adımlarda geçerli sıçramaları zaten dikkate aldığımızdan, mevcut dizinin tüm tekrarlarını haritadan kaldırın
            if dizi[mevcut] in eşleme:
                eşleme.pop(dizi[mevcut])
             
         
        # Sıçrama sayısını artırın
        sayac = sayac + 1
     
    # Son olarak, sayacı döndürün
    return sayac // 2

# Sürücü kodu
dizi = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
 
# Fonksiyon çağrısı
print(sıçramalarıAzalt(dizi))
