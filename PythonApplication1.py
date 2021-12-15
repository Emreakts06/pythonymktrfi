print("Yemek Tarifi Ödevi ")



yemektarif = open("yemektarifleri.txt", "w") 
yemektarif.write(input(  "Yemek adý giriniz = " )) 
yemektarif.write(input( "Yemek tarifi giriniz = " ))
yemektarif.close()

dosya = open("yemektarifleri.txt","r")
oku = dosya.read()
print("Yemek Adý ve Tarifi = " ,oku)
