"""
Exercice A

Checklist :
    - Diagramme
    - Construction classe Player
    - Construction classe Musique
    
"""


# DIAGRAMME DE CLASSE PLAYER (son nom, son score par chanson, son total de points, la moyenne, ses pires et meilleures performances)
"""
CLASSE PLAYER   

+ name
+ score
+ total
+ moyenne
+ perfs
+ txt

- getScore
- getName
- getTotal
- getMoyenne
- getPerfs
- getTexte

"""
game = False


#Classe Player, definition des conditions et creation de ses caracteristiques

class Player:
    def __init__ (self, name, score, total, moyenne, perfs, txt):
        self.__nom = name
        self.__score = score
        self.__total = total
        self.__moyenne = moyenne
        self.__perfs = perfs
        self.__texte = txt
        
    
    def getName (self):
        return self.__nom
    def getScore (self):
        return self.__score
    def getTotal (self):
        return self.__total
    def getMoyenne (self):
        return self.__moyenne
    def getPerfs (self):
        return self.__perfs
    def getTexte (self):
        return self.__texte


#Attribution des caractéristiques à chaque valeurs d'un joueur (joueur Un, joueur Deux etc...)

Un = Player("Un", (50+50+50), 150, 50, "Vous êtes à l'équilibre, votre maximum et votre minimum sont à 50", 1)
Deux = Player("Deux", (60+70+60), 190, 63, "Votre maximum : 70 et votre minimum : 60",1)
Trois = Player("Trois", (50 + 60 + 80), 190, 63, "Votre maximum 80 et votre minimum : 50",1)
Quatre = Player("Quatre", (50 + 50 + 100), 200, 63, "Votre maximum : 90 et votre minimum : 50", 1)



#Classe Karaoke qui definit les titres des musiques, les paroles et les points qu'elles attribuent
class Karaoke:
    def __init__ (self, titre, pistes, record):
        self.__titre = titre
        self.__pistes = pistes
        self.__record = record

    def getTitre (self):
        return self.__titre
    def getPistes (self):
        return self.__pistes
    def getRecord (self):
        return self.__record


#Caractéristiques par musiques (Titre, Nombres de personnes par musique et record par musique)

Ah = Karaoke("Ah", "Nombre de joueur autorisé est de 3", "Joueur 2 possède le meilleur score sur cette musique !")
Oh = Karaoke("Oh", "Nombre de joueur autorisé est de 2", "Joueur 1 possède le meilleur score sur cette musique !")
Eh = Karaoke("Eh", "Nombre de joueur autorisé est de 3", "Joueur 4 possède le meilleur score sur cette musique !")
Uh = Karaoke("Uh", "Nombre de joueur autorisé est de 4", "Joueur 2 possède le meilleur score sur cette musique !")
Ih = Karaoke("Ih", "Nombre de joueur autorisé est de 3", "Joueur 1 possède le meilleur score sur cette musique !")




#Commencer par identifier le nombre de joueurs et le joueur qui joue

if game == False:
    print ("Avant de débuter, nos savons l'intérêt que porte notre clientèle au menu Recordmen, neanmois, nous vous prions de nous excusez, le menu Recordmen permettant d'analyser et de comparer les meilleures moyennes est en cours de développement chez nos meilleurs techniciens")
    nombre = input ("Tapez le nombre de joueurs en toutes lettres 'Un', 'Deux', 'Trois', 'Quatre'...")
    if (nombre == "Un"):
        choix = input("Veuillez choisir votre identifiant de joueur : Un")
    if (nombre == "Deux"):
        choix = input("Veuillez choisir votre identifiant de joueur : Un, Deux")
    if (nombre == "Trois"):
        choix = input("Veuillez choisir votre identifiant de joueur : Un, Deux, Trois")
    if (nombre == "Quatre"):
        choix = input("Veuillez choisir votre identifiant de joueur : Un, Deux, Trois ou Quatre")
    game = True

#Premier Joueur !

if (choix == "Un"):
    print ("Premier joueur, bienvenu au karaoké :")
    menu1 = input ("Veuillez taper l'action choisie : Chanter ou Score")

#Debut de creation du menu pour comparer les records (manque de temps)
    """if (menu1 == "Recordmen"):
        BestMoyenne = Un.getMoyenne()"""
    



    if (menu1 == "Chanter"):
        chanson = input ("Selectionnez la musique souhaitez : Ah, Oh, Eh, Uh, Ih")


        # Si le joueur veut chanter


#Musique 1
        if (chanson == "Ah"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ah.getTitre())
            if (action1 == "Joueurs"):
                print (Ah.getPistes())
            if (action1 == "Record"):
                print (Ah.getRecord())


#Musique 2
        if (chanson == "Eh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Eh.getTitre())
            if (action1 == "Joueurs"):
                print (Eh.getPistes())
            if (action1 == "Record"):
                print (Eh.getRecord())


#Musique 3
        if (chanson == "Oh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Oh.getTitre())
            if (action1 == "Joueurs"):
                print (Oh.getPistes())
            if (action1 == "Record"):
                print (Oh.getRecord())


#Musique 4
        if (chanson == "Uh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Uh.getTitre())
            if (action1 == "Joueurs"):
                print (Uh.getPistes())
            if (action1 == "Record"):
                print (Uh.getRecord())


    #Musique 5    
        if (chanson == "Ih"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ih.getTitre())
            if (action1 == "Joueurs"):
                print (Ih.getPistes())
            if (action1 == "Record"):
                print (Ih.getRecord())






        # Si le joueur veut consulter ses scores


    if (menu1 == "Score"):
        select = input ("Choisissez si vous voulez : Consulter, Total, Moyenne, Performances")
        if (select == "Consulter"):
            print (Un.getScore())
        if (select == "Total"):
            print (Un.getTotal())
        if (select == "Moyenne"):
            print (Un.getMoyenne())
        if (select == "Performances"):
            print (Un.getPerfs())



#Deuxieme Joueur !

if (choix == "Deux"):
    game = True
    print ("Premier joueur, bienvenu au karaoké :")
    menu2 = input ("Veuillez taper l'action choisie : Chanter ou Score")

    if (menu2 == "Chanter"):
        chanson = input ("Selectionnez la musique souhaitez : Ah, Oh, Eh, Uh, Ih")

         #Si le joueur veut chanter



        if (chanson == "Ah"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ah.getTitre())
            if (action1 == "Joueurs"):
                print (Ah.getPistes())
            if (action1 == "Record"):
                print (Ah.getRecord())



        if (chanson == "Eh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Eh.getTitre())
            if (action1 == "Joueurs"):
                print (Eh.getPistes())
            if (action1 == "Record"):
                print (Eh.getRecord())



        if (chanson == "Oh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Oh.getTitre())
            if (action1 == "Joueurs"):
                print (Oh.getPistes())
            if (action1 == "Record"):
                print (Oh.getRecord())



        if (chanson == "Uh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Uh.getTitre())
            if (action1 == "Joueurs"):
                print (Uh.getPistes())
            if (action1 == "Record"):
                print (Uh.getRecord())


        
        if (chanson == "Ih"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ih.getTitre())
            if (action1 == "Joueurs"):
                print (Ih.getPistes())
            if (action1 == "Record"):
                print (Ih.getRecord())



    # Si le joueur veut consulter ses scores


    if (menu2 == "Score"):
        select = input ("Choisissez si vous voulez : Consulter, Total, Moyenne, Performances")
        if (select == "Consulter"):
            print (Deux.getScore())
        if (select == "Total"):
            print (Deux.getTotal())
        if (select == "Moyenne"):
            print (Deux.getMoyenne())
        if (select == "Performances"):
            print (Deux.getPerfs())
        game = False




# Troisieme Joueur

if (choix == "Trois"):
    game = True
    print ("Premier joueur, bienvenu au karaoké :")
    menu3 = input ("Veuillez taper l'action choisie : Chanter ou Score")

    if (menu3 == "Chanter"):
        chanson = input ("Selectionnez la musique souhaitez : Ah, Oh, Eh, Uh, Ih")


    
     #Si le joueur veut chanter



        if (chanson == "Ah"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ah.getTitre())
            if (action1 == "Joueurs"):
                print (Ah.getPistes())
            if (action1 == "Record"):
                print (Ah.getRecord())



        if (chanson == "Eh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Eh.getTitre())
            if (action1 == "Joueurs"):
                print (Eh.getPistes())
            if (action1 == "Record"):
                print (Eh.getRecord())



        if (chanson == "Oh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Oh.getTitre())
            if (action1 == "Joueurs"):
                print (Oh.getPistes())
            if (action1 == "Record"):
                print (Oh.getRecord())



        if (chanson == "Uh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Uh.getTitre())
            if (action1 == "Joueurs"):
                print (Uh.getPistes())
            if (action1 == "Record"):
                print (Uh.getRecord())


        
        if (chanson == "Ih"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ih.getTitre())
            if (action1 == "Joueurs"):
                print (Ih.getPistes())
            if (action1 == "Record"):
                print (Ih.getRecord())


        # Si le joueur veut consulter ses scores


    if (menu3 == "Score"):
        select = input ("Choisissez si vous voulez : Consulter, Total, Moyenne, Performances")
        if (select == "Consulter"):
            print (Trois.getScore())
        if (select == "Total"):
            print (Trois.getTotal())
        if (select == "Moyenne"):
            print (Trois.getMoyenne())
        if (select == "Performances"):
            print (Trois.getPerfs())
        game = False




# Quatrieme Joueur

if (choix == "Quatre"):
    game = True
    print ("Premier joueur, bienvenu au karaoké :")
    menu4 = input ("Veuillez taper l'action choisie : Chanter ou Score")

    if (menu4 == "Chanter"):
        chanson = input ("Selectionnez la musique souhaitez : Ah, Oh, Eh, Uh, Ih")

    

     #Si le joueur veut chanter



        if (chanson == "Ah"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ah.getTitre())
            if (action1 == "Joueurs"):
                print (Ah.getPistes())
            if (action1 == "Record"):
                print (Ah.getRecord())



        if (chanson == "Eh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Eh.getTitre())
            if (action1 == "Joueurs"):
                print (Eh.getPistes())
            if (action1 == "Record"):
                print (Eh.getRecord())



        if (chanson == "Oh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Oh.getTitre())
            if (action1 == "Joueurs"):
                print (Oh.getPistes())
            if (action1 == "Record"):
                print (Oh.getRecord())



        if (chanson == "Uh"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Uh.getTitre())
            if (action1 == "Joueurs"):
                print (Uh.getPistes())
            if (action1 == "Record"):
                print (Uh.getRecord())


        
        if (chanson == "Ih"):
            action1 = input ("Tapez 'Titre' pour voir le titre, 'Joueurs' pour voir le nombre max ou Record pour voir qui détient le record sur celle-ci")


            if (action1 == "Titre"):
                print ("Le titre est", Ih.getTitre())
            if (action1 == "Joueurs"):
                print (Ih.getPistes())
            if (action1 == "Record"):
                print (Ih.getRecord())




        # Si le joueur veut consulter ses scores


    if (menu4 == "Score"):
        select = input ("Choisissez si vous voulez : Consulter, Total, Moyenne, Performances")
        if (select == "Consulter"):
            print (Quatre.getScore())
        if (select == "Total"):
            print (Quatre.getTotal())
        if (select == "Moyenne"):
            print (Quatre.getMoyenne())
        if (select == "Performances"):
            print (Quatre.getPerfs())
        game = False








