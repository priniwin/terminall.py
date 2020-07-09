#ont cree une variable true
lance = True
import os
#on lance la boucle pour dire tant que lance est true
while lance == True:
    saisi = input("> ")
    if saisi == "quiter":
        break
    elif saisi == "hello":
        print("bonjour user (=")
    elif saisi == "help":
        print("quiter,hello,help,acount,descri,conect,surprise")
    elif saisi == "acount":
        identifiant = input("cree votre identifiant : ")
        password = input("cree votre mot de passe : ")
        print("bienvenue")
    elif saisi == "descri":
        print("quiter permet de quiter le programme,hello afiche un message de bienvenue,help affiche toute les commande, acount sert a cree sont compte, conect permet de se conecter et surprise est une surprise")
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
    else:
        print("commande introuvable")


