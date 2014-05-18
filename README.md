=== PYZEN ===

1.1 INSTALLATION 

sudo apt-get install python2.7, python-pygame -y ---> cette commande permet d'installer d'une part python version 2.7 + module pygame 

1.2 LANCEMENT JEU PYZEN : 

Première étape consiste à démarrer un terminal (si vous êtes sous une distribution dérivée de DEBIAN alors CTRL+ALT+T)
Ensuite se rendre dans le dossier du jeu (cd /arborescencedujeu/ ) et faire la commande : python PyZen.py

1.3 PRESENTATION DU JEU PYZEN :


PyZen :
----

1. Présentation : 
================

Au sein de ce petit jeu, vous incarnez Zio un jeune moine bouddhiste cherchant à retrouver la voie du juste milieu et de s'adonner à la sagesse du Ying et du Yang. 
Ainsi, parcourez l'ensemble du terrain de jeu et trouvez votre chemin en espérant ne pas vous confrontez à une voie obstruée.

2. Architecture :
================

PyZen a été conçu d'une manière à ce qu'à l'avenir, l'on puisse y apporter des modifications en vue d'améliorer le jeu, de lui rajouter des modules... Ainsi l'arborescence se présente comme suit :

----> classes.pyc : au sein de ce fichier vous trouverez l'ensemble des classes utiles au programme.
----> constantes.pyc : ce fichier récapitule l'ensemble des variables constantes appelées au cours de l'exécution du programme.
----> PyZen.py : représente le fichier appelé couramment par "main" soit le programme principal.
