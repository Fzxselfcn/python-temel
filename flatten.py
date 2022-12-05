liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] // bize input olarak verilen liste
list_flat = [] // düzleştirilen elemanları koyacağımız listeyi oluşturuyoruz
def flatten(n): // düzleştirme fonksiyonunu yazıyoruz
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            list_flat.append(i)

flatten(liste) // fonksiyonumuzu listeye uyguluyoruz
print(list_flat) // yeni listeyi ekrana yazdırıyoruz
