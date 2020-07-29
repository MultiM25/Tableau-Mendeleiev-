import elements
import pygame
import couleur
    
pygame.init()

largeur = 75                                                                                            # INITIALISATION PYGAME
hauteur = 75

fenetre = pygame.display.set_mode((1500,800))

pygame.display.set_caption("Tableau Périodiques")

continuer = True

police1 = pygame.font.Font(None,35)                                                                     #   Création Polices
police2 = pygame.font.Font(None,30)                                                                     #
police3 = pygame.font.Font(None,15)

liste_symbole = []
liste_numéro = []
liste_nom = []

for i in range(len(elements.elements)):                                                                 #
    texte = police1.render(elements.elements[i]["Symbole"],True,(0,0,0))                                #   Crétation des listes pour les symboles/noms/numéros
    texte1 = police2.render(elements.elements[i]["Numéro"],True,(0,0,0))                                #
    texte2 = police3.render(elements.elements[i]["Nom"],True,(0,0,0))
    liste_symbole.append(texte)
    liste_numéro.append(texte1)
    liste_nom.append(texte2)

choix = 0

solide = police1.render("Solide",True,(0,0,0))                                                          #
gaz = police1.render("Gaz",True,(0,0,0))                                                                #   Création des textes constants
inconnu = police1.render("Inconnu",True,(0,0,0))                                                        #
defaut = police1.render("Touche N : Defaut",True,(0,0,0))
famille = police1.render("Touche F : Famille",True,(0,0,0))
etat_naturel = police1.render("Touche E : Etat Naturel",True,(0,0,0))


famille1 = police3.render("Alcalins",True,(0,0,0))
famille2 = police3.render("Alcalino-Terreux",True,(0,0,0))
famille3 = police3.render("Lanthanides",True,(0,0,0))
famille4 = police3.render("Actinides",True,(0,0,0))
famille5 = police3.render("Métaux de transition",True,(0,0,0))
famille6 = police3.render("Métaux pauvre",True,(0,0,0))
famille7 = police3.render("Métalloîdes",True,(0,0,0))
famille8 = police3.render("Non-Métal",True,(0,0,0))
famille9 = police3.render("Halogèmes",True,(0,0,0))
famille10 = police3.render("Gaz Nobles",True,(0,0,0))
famille0 = police3.render("Non Classé",True,(0,0,0))

while continuer:
    
    fenetre.fill((255,255,255))
    if choix == 1:
        for i in range(len(elements.elements)):
            x = 10 + largeur * elements.elements[i]["col"]
            y = 10 + hauteur * elements.elements[i]["lin"]
            
            if elements.elements[i]["Famille"] == "Non-Métal":
                pygame.draw.rect(fenetre,couleur.vert,(x,y,largeur,hauteur))                            #
            elif elements.elements[i]["Famille"] == "Halogènes":                                        #
                pygame.draw.rect(fenetre,couleur.jaune,(x,y,largeur,hauteur))                           #   Affichage des informations a l'appui d'une touche (F,E ou N)
            elif elements.elements[i]["Famille"] == "Gaz Nobles":                                       #
                pygame.draw.rect(fenetre,couleur.bleu,(x,y,largeur,hauteur))                            #
            elif elements.elements[i]["Famille"] == "Métaux de transition":                             #
                pygame.draw.rect(fenetre,couleur.rose,(x,y,largeur,hauteur))                            #
            elif elements.elements[i]["Famille"] == "Alcalins":
                pygame.draw.rect(fenetre,couleur.rouge,(x,y,largeur,hauteur))
            elif elements.elements[i]["Famille"] == "Alcalino-Terreux":
                pygame.draw.rect(fenetre,couleur.beige,(x,y,largeur,hauteur))
            elif elements.elements[i]["Famille"] == "Lanthanides":
                pygame.draw.rect(fenetre,couleur.mauve,(x,y,largeur,hauteur))
            elif elements.elements[i]["Famille"] == "Actinides":
                pygame.draw.rect(fenetre,couleur.violet,(x,y,largeur,hauteur))
            elif elements.elements[i]["Famille"] == "Alcalin":
                pygame.draw.rect(fenetre,couleur.rouge,(x,y,largeur,hauteur))
            elif elements.elements[i]["Famille"] == "Métalloîdes":
                pygame.draw.rect(fenetre,couleur.marron,(x,y,largeur,hauteur))
            elif elements.elements[i]["Famille"] == "Métaux pauvres":
                pygame.draw.rect(fenetre,couleur.gris,(x,y,largeur,hauteur))
            pygame.draw.rect(fenetre,couleur.rouge,(50,765,100,30))
            fenetre.blit(famille1,(60,780))
            pygame.draw.rect(fenetre,couleur.beige,(160,765,100,30))
            fenetre.blit(famille2,(170,780))
            pygame.draw.rect(fenetre,couleur.mauve,(270,765,100,30))
            fenetre.blit(famille3,(280,780))
            pygame.draw.rect(fenetre,couleur.violet,(380,765,100,30))
            fenetre.blit(famille4,(390,780))
            pygame.draw.rect(fenetre,couleur.rose,(490,765,100,30))
            fenetre.blit(famille5,(490,780))
            pygame.draw.rect(fenetre,couleur.gris,(600,765,100,30))
            fenetre.blit(famille6,(610,780))
            pygame.draw.rect(fenetre,couleur.marron,(710,765,100,30))
            fenetre.blit(famille7,(720,780))
            pygame.draw.rect(fenetre,couleur.vert,(820,765,100,30))
            fenetre.blit(famille8,(830,780))
            pygame.draw.rect(fenetre,couleur.jaune,(930,765,100,30))
            fenetre.blit(famille9,(940,780))
            pygame.draw.rect(fenetre,couleur.bleu,(1040,765,100,30))
            fenetre.blit(famille10,(1050,780))
            pygame.draw.rect(fenetre,(255,255,255),(1150,765,100,30))
            fenetre.blit(famille0,(1160,780))
    if choix == 2:
        for i in range(len(elements.elements)):
            x = 10 + largeur * elements.elements[i]["col"]
            y = 10 + hauteur * elements.elements[i]["lin"]
            
            if elements.elements[i]["Etat naturel"] == "Gaz":
                pygame.draw.rect(fenetre,(0,0,200),(x,y,largeur,hauteur))
            if elements.elements[i]["Etat naturel"] == "Liquie":
                pygame.draw.rect(fenetre,(0,200,0),(x,y,largeur,hauteur))
            if elements.elements[i]["Etat naturel"] == "Solide":
                pygame.draw.rect(fenetre,(200,0,0),(x,y,largeur,hauteur))
            pygame.draw.rect(fenetre,(0,0,200),(50,600,100,50))
            fenetre.blit(gaz,(70,620))
            pygame.draw.rect(fenetre,(200,0,0),(50,660,100,50))
            fenetre.blit(solide,(70,680))
            pygame.draw.rect(fenetre,(255,255,255),(50,710,100,50))
            fenetre.blit(inconnu,(50,730))
            
    if choix == 3:
        fenetre.fill((255,255,255))
                
    for i in range(len(elements.elements)):
        x = 10 + largeur * elements.elements[i]["col"]                                                                              #
        y = 10 + hauteur * elements.elements[i]["lin"]                                                                              #   Création et affichage du Tableau avec Symbole/Nom/Numéro
        pygame.draw.line(fenetre,(0,0,0),(x,y),(x+largeur,y))                                                                       #
        pygame.draw.line(fenetre,(0,0,0),(x+largeur,y),(x+largeur,y+hauteur))
        pygame.draw.line(fenetre,(0,0,0),(x+largeur,y+hauteur),(x,y+hauteur))
        pygame.draw.line(fenetre,(0,0,0),(x,y+hauteur),(x,y))
        

    for i in range(len(liste_symbole)):
        fenetre.blit(liste_symbole[i],(45 + largeur * elements.elements[i]["col"],28 + hauteur * elements.elements[i]["lin"]))
        fenetre.blit(liste_numéro[i],(15 + largeur * elements.elements[i]["col"],15 + hauteur * elements.elements[i]["lin"]))
        fenetre.blit(liste_nom[i],(15 + largeur * elements.elements[i]["col"],60 + hauteur * elements.elements[i]["lin"]))

    
    fenetre.blit(defaut,(200,550))                                                                  
    fenetre.blit(famille,(500,550))                                                                 
    fenetre.blit(etat_naturel,(800,550))                                                            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:                                                            #
            if event.key == pygame.K_f:                                                             #   Gestion des événements
                choix = 1                                                                           #
            if event.key == pygame.K_e:
                choix = 2
            if event.key == pygame.K_n:
                choix = 3
    
    pos = pygame.mouse.get_pos()
    x = pos[0]//largeur 
    y = pos[1]//hauteur

    for i in range(len(elements.elements)):
        if x == elements.elements[i]["col"] and y == elements.elements[i]["lin"]:

            symbole = police1.render(elements.elements[i]["Symbole"],True,(0,0,0))                  #
            nom = police1.render(elements.elements[i]["Nom"],True,(0,0,0))                          #       Creation texte pour l'affichage des caracteristiques des elements 
            numero = police1.render(elements.elements[i]["Numéro"],True,(0,0,0))                    #
            masse_atomique = police2.render(elements.elements[i]["Masse atomique"],True,(0,0,0))    #
            masse = police2.render("Masse atomique :",True,(0,0,0))                             
            rayon_atomique = police2.render(elements.elements[i]["Rayon atomique"],True,(0,0,0))    
            rayon = police2.render("Rayon atomique :",True,(0,0,0))                                                                           
            nb_isotope = police2.render(elements.elements[i]["Nombre d'isotopes"],True,(0,0,0))
            isotope = police2.render("Nombre d'isotopes : ",True,(0,0,0))
            tp_ebul = police2.render(elements.elements[i]["Température d'ébullition"],True,(0,0,0))
            ebullition = police2.render("° d'ébullition : ",True,(0,0,0))
            tp_fus = police2.render(elements.elements[i]["Température de fusion"],True,(0,0,0))
            fusion = police2.render("° de fusion : ",True,(0,0,0))
            famille = police2.render(elements.elements[i]["Famille"],True,(0,0,0))
            fam = police2.render("Famille : ",True,(0,0,0))
            date = police2.render(elements.elements[i]["Date de découverte"],True,(0,0,0))
            dt = police2.render("Date de découverte : ",True,(0,0,0))
            decouvreur = police2.render(elements.elements[i]["Decouvreur(s)"],True,(0,0,0))
            dec = police2.render("Découvreur(s) : ",True,(0,0,0))
            
            fenetre.blit(symbole,(170,35))                                                          #
            fenetre.blit(nom,(220,35))                                                              #           Affichage du texte
            fenetre.blit(numero,(170,10))                                                           #
            fenetre.blit(masse_atomique,(350,80))
            fenetre.blit(masse,(170,80))
            fenetre.blit(famille,(350,120))
            fenetre.blit(fam,(255,120))
            fenetre.blit(rayon_atomique,(350,100))
            fenetre.blit(rayon,(170,100))
            fenetre.blit(nb_isotope,(450,140))
            fenetre.blit(isotope,(250,140))
            fenetre.blit(tp_ebul,(450,180))
            fenetre.blit(ebullition,(300,180))
            fenetre.blit(tp_fus,(450,200))
            fenetre.blit(fusion,(317,200))
            fenetre.blit(date,(750,30))
            fenetre.blit(dt,(530,30))
            fenetre.blit(decouvreur,(750,50))
            fenetre.blit(dec,(580,50))
            
    pygame.display.update()
    
pygame.quit()
    
