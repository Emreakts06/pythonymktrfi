print("Yemek Tarifi �devi ")



yemektarif = open("yemektarifleri.txt", "w") 
yemektarif.write(input(  "Yemek ad� giriniz = " )) 
yemektarif.write(input( "Yemek tarifi giriniz = " ))
yemektarif.close()

dosya = open("yemektarifleri.txt","r")
oku = dosya.read()
print("Yemek Ad� ve Tarifi = " ,oku)
