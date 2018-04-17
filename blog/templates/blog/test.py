a=0
while a < 500:
     fichier = open(str(a)+"lire.txt", "a")
     fichier.write("Il y en a 500 comme ca :D")
     fichier.close()
     print("lol")
     a=a+1