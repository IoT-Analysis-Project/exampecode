def kenarEkle(liste, kaynak, hedef):
    # Kaynak düğümden hedef düğüme bir kenar ekler.
    liste[kaynak].append(hedef)

def displayGraph(liste, v):
    for i in range(v):
        print(i, "--> ", end = "")     # Düğümün numarasını yazdırır.
        for j in range(len(liste[i])):
            print(liste[i][j], end = " ")    # Düğümün komşularını yazdırır.
        print()

def transposeGraph(liste, transpose, v):
    for i in range(v):
        for j in range(len(liste[i])):
            # Her kenarın yönünü tersine çevirerek transpoz matrisine ekler.
            kenarEkle(transpose, liste[i][j], i)

if __name__ == '__main__':
    v = 5
    liste = [[] for i in range(v)] 
    
    # Graf için kenarları ekler
    kenarEkle(liste, 0, 1) 
    kenarEkle(liste, 0, 4) 
    kenarEkle(liste, 0, 3) 
    kenarEkle(liste, 2, 0) 
    kenarEkle(liste, 3, 2) 
    kenarEkle(liste, 4, 1) 
    kenarEkle(liste, 4, 3) 

    transpose = [[] for i in range(v)]
    transposeGraph(liste, transpose, v) 

    # Transpoz grafiği görselleştirir
    displayGraph(transpose, v)
