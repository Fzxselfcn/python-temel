input = [[1, 2], [3, 4], [5, 6, 7]] # bize input olarak verilen liste
input.reverse() #listeye fonksiyonu uyguluyoruz
for i in range(len(input)): #Her eleman için, alt listeyi tersine döndüren döngü
    (input[i])=(input[i])[::-1]

print(input) #listeyi ekrana yazdırıyoruz
