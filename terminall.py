#ont cree une variable true
lance = True
import os
#on lance la boucle pour dire tant que lance est true
while lance == True:
    saisi = input("> ")
    if saisi == "exit":
        lance = False
        if lance == False:
            break
    elif saisi == "hello":
        print("bonjour user (=")
    elif saisi == "help":
         print("exit")
         print("hello")
         print("help")
         print("acount")
         print("descri")
         print("conect")
         print("multi")
         print("divis")
         print("adis")
         print("sous")
         print("repet")
         print("roulette")
         print("see")
    elif saisi == "acount":
        identifiant = input("cree votre identifiant : ")
        password = input("cree votre mot de passe : ")
        print("bienvenue")
    elif saisi == "descri":
        print("exit permet de quiter")
        print("hello vous passe un bonjour")
        print("acount vous permet d'enregistrer un compte")
        print("conect permet de vous conecter")
        print("multi permet de faire une multiplication")
        print("divis permet de faire une division")
        print("adis permet de faire une adition")
        print("sous permet de faire une soustraction")
        print("help affiche les commande")
        print("descri affiche la description des commandes")
        print("repet permet de repeter ce que vous marquez tapeexit pour sortir")
        print("roulette est le jeu du franc prix")
        print("see permet de voir le code")
    elif saisi == "conect":
        id = input("rentrer votre identifiant : ")
        passw = input("rentre votre mot de passe : ")
        if id in identifiant:
            print("identifiant corect")
        else:
            print("identifiant incorect")
        if passw in password:
            print("mot de passe corect")
        else:
            print("mot de passe incorect")
    elif saisi == "caca":
        print("vous etes oficiellement un gamin =)")
    elif saisi == "multi":
        mul1 = int(input("premier chiffre pour la multiplication : "))
        mul2 = int(input("deuxieme chiffre pour la multiplication : "))
        print("le resultat est {}".format(mul1 * mul2))
    elif saisi == "divis":
        div1 = int(input("premier chiffre pour la division : "))
        div2 = int(input("deuxieme chiffre pour la division : "))
        print("le resultat est {}".format(div1 / div2))
    elif saisi == "adis":
        add1 = int(input("premier chiffre pour l'adition : "))
        add2 = int(input("deuxieme chiffre pour l'adition : "))
        print("le reultat est {}".format(add1 + add2))
    elif saisi == "sous":
        sous1 = int(input("premier chiffre pour la soustraction : "))
        sous2 = int(input("deuxieme chiffre pour la soustraction : "))
        print("le resultat est {}".format(sous1 - sous2))
    elif saisi == "repet":
        lance2 = True
        while lance2 == True: 
            saisi2 = input("repet ")
            print(saisi2)
            if saisi2 == "exit":
                break
    elif saisi == "roulette":
    	print("ceci est le jeu du franc prix")
    	print("le chiffre est entre 1 et 1000 bonne chance")
    	import random
    	prix = random.randint(1, 1000)
    	prix2 = int(input("chiffre : "))

    	if prix == prix2:
    		print("vous avez gagnez bravo ! ")
    	else:
    		print("perdu le chiffre etatait {}".format(prix))
    elif saisi == "see":
    		conclu = input("voulez vous voir le code du programme ? : ")
    		if conclu == "oui":
    			print("voici le lien pour le code : https://github.com/priniwin/terminall.py/blob/master/terminall.py")
    		else:
    			print("dacord")	
    else:
    	print("commande introuvable")

