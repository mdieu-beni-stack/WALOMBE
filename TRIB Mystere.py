import random
def jeu_nombre_mystere():
    "jeu où l'ordinateur choisit un nombre entre 1 et 100"
    # l'ordinateur tire un nombre aleatoire
    nombre_mystere= random.randint(1, 100)
    nombre_essais = 0
    print("=== JEU DU NOMBRE MYSTERE ===")
    print("J'ai choisi un nombre entre 1 et 100.")
    print("A vous de le déviner !\n")
    i=5
    while i>1:
        # Demander à l'utilisateur de deviner
        try:
            proposition = int(input("Votre proposition :"))
            nombre_essais += 1
            if proposition > 100 or proposition < 1:
                 print("entrer un nombre valide")
                 continue
            # Comparer avec le nombre secret
            if proposition < nombre_mystere:
                print("X Trop petit ! Essayer encore.\n")
            elif proposition > nombre_mystere:
                print("X Trop grand ! Essayez encore.\n")
            else:
                print(f" Bravo ! Vous avez trouvé le nombre mystere {nombre_essais} en essai(s) !")
                break
        except ValueError:
            print(" Veuillez entrer un nombre valide.\n")
#  Lancer le jeu
jeu_nombre_mystere()                         

