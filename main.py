
#escalier/scales
def escalier(taille,nombre_de_marche):
    import turtle 
    t=turtle.Turtle()

    for i in range(0,int(nombre_de_marche)):
        t.forward(int(taille))
        t.left(90)
        t.forward(int(taille))
        t.right(90)
        #taille=taille-5
        taille_int=int(taille)
        taille_int-=10
    t.forward(taille)
    turtle.done()

#carre/square
def carre (taille):
    import turtle
    t=turtle.Turtle()
    for i in range(4):
        t.forward(taille)
        t.left(90)
    turtle.done()


#carres/squares
def carres(taille_depart, nb_carre):
    import turtle
    t=turtle.Turtle()
    for i in range(nb_carre):
        taille=(i+1)*taille_depart
        for i in range(4):
            t.forward(taille)
            t.left(90)
    turtle.done()


print(""" Jeu de la tortue 
      1-creation de marches (escaliers)
      2-creation d'un carre 
      3-creation de plusieurs carres imbriqués 
      """)


choix=input("faites votre choix :")
if int(choix )==1:
    taille=input("creation d'excaliers: veuillez entrer la taille de marches : ")
    nombre_demarche=input("le nombre de marche ")
    escalier(taille,nombre_demarche)
if int(choix)==2:
    taille_carre=input("création de carré: veuillez entrer la taille de chaque coté :")
    carre(int(taille_carre))
if int(choix)==3:
    nb_carres=input("creation de plusieurs carrés imbriqués : veuillez entrer le nombre de carrés : ")
    taille_carres=input('entrez la taille coté du premier carré :')
    carres(int(taille_carres),int(nb_carres))