#!/usr/bin/python3
# -*- coding: utf-8 -*

"""
PyZen :
----

1. Présentation : 
*****************

Au sein de ce petit jeu, vous incarnez Zio un jeune moine bouddhiste cherchant à retrouver la voie du juste milieu et de s'adonner à la sagesse du Ying et du Yang. 
Ainsi, parcourez l'ensemble du terrain de jeu et trouvez votre chemin en espérant ne pas vous confrontez à une voie obstruée.

2. Architecture :
****************

PyZen a été conçu d'une manière à ce qu'à l'avenir, l'on puisse y apporter des modifications en vue d'améliorer le jeu, de lui rajouter des modules... Ainsi l'arborescence se présente comme suit :

----> classes.pyc : au sein de ce fichier vous trouverez l'ensemble des classes utiles au programme.
----> constantes.pyc : ce fichier récapitule l'ensemble des variables constantes appelées au cours de l'exécution du programme.
----> PyZen.py : représente le fichier appelé couramment par "main" soit le programme principal.

"""

# Importation du module Pygame
###############################

import pygame
from pygame.locals import *

# Importation des fichiers classes et constantes 
#################################################
from classes import *
from constantes import *

pygame.init() # Initialisation de Pygame

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


# Boucle du jeu PyZen
#####################
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 'n1'		#On définit le niveau à charger
				#Lancement du niveau 2
				elif event.key == K_F2:
					continuer_accueil = 0
					choix = 'n2'
			
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		# Création du personnage
		moine = Perso("images/moine_droite.png", "images/moine_gauche.png", 
		"images/moine_haut.png", "images/moine_bas.png", niveau)

				
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					moine.deplacer('droite')
				elif event.key == K_LEFT:
					moine.deplacer('gauche')
				elif event.key == K_UP:
					moine.deplacer('haut')
				elif event.key == K_DOWN:
					moine.deplacer('bas')			
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(moine.direction, (moine.x, moine.y)) 
		pygame.display.flip()

		# Si le joueur parvient à trouver le zen alors retour à l'accueil
		if niveau.structure[moine.case_y][moine.case_x] == 'a':
			continuer_jeu = 0
