# -*- coding: utf-8 -*-
import urx
from urx.robotiq_two_finger_gripper import Robotiq_Two_Finger_Gripper
import numpy as np

## Réglage de connection TCP/IP ###
TCP_Robot = "192.168.1.22"          # Adresse IP du robot
TCP_Mon_Ordi = "192.168.1.100"      # Adresse IP de mon ordi (Il faut paramétrer une liaison manuellement
                                    # et écrire une adresse IP dans le même sous réseau
                                    # que le robot 192.168.1.XX)
TCP_PORT_GRIPPER = 40001            # Ne pas changer
TCP_PORT = 50002                    # Ne pas changer

# Connection au robot
robot = urx.Robot(TCP_Robot)
robot.set_tcp((0, 0, 0.3, 0, 0, -0.43)) # Position du Tool Center Point par rapport au bout du robot (x,y,z,Rx,Ry,Rz)
                                    # (en mm et radians)
robot.set_payload(2.152, (0, 0, 0.1))       # Poids de l'outil et position de son centre de gravité (en kg et mm)

# Connection à la pince
gripper = Robotiq_Two_Finger_Gripper(robot)

# Caractéristique de mouvement
acc = 0.1                        # Accélération maximale des joints
vel = 0.05                           # Vitesse maximale des joints
deg2rad = np.pi/180
angular_pos = [-71*deg2rad, -79*deg2rad, -93*deg2rad, -93*deg2rad, 89*deg2rad, -12*deg2rad]

# Commandes robot
'''
Les différentes commandes sont disponibles dans les fichiers python-urx/urx/robot.py 
                                                          et python-urx/urx/urrobot.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ATTENTION les coordonnées  données dans cet exemple
ne sont pas nécessairement compatibles avec la disposition de votre robot.
Avant d'enlever de lancer le programme
assurez vous que cela est possible en sécurité pour les humains et le matériel
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Décommenter les lignes suivantes pour lancer le programme d'exemple
'''
robot.movel([0.09, -0.45, 0.25, 0.82, -3, 0.1], acc=acc, vel=vel)        # Bouge le robot aux coordonnées cartésiennes

# robot.movej(angular_pos, acc=acc, vel=vel)	                    # Bouge le robot en articulaire (radian)
# print(robot.get_pose())                                          # Renvoie le (x, y, z) du TCP
# robot.up()
# robot.down()
# robot.translate([0.1, 0.1, 0.1])

# Commandes pince
'''
Les différentes commandes sont disponibles dans le fichier python-urx/urx/robotiq_two_fingers_gripper.py
dans la classe Robotiq_Two_Finger_Gripper                                             
'''
# gripper.open_gripper()                                  # Ferme entièrement le gripper
# gripper.close_gripper()                                 # Ouvre entièrement le gripper
# gripper.gripper_action(150)                             # Ouvre le gripper à une certaine taille (0:ouvert, 255: fermé)
# print(gripper.send_opening(TCP_Mon_Ordi, TCP_PORT_GRIPPER))  # Retourne l'ouverture de la pince


# for i in range(5):
#     robot.movel([0.09, -0.45, 0.25, 0.82, -3, 0.1], acc=acc, vel=vel)
#     robot.movel([0.01, -0.45, 0.25, 0.82, -3, 0.1], acc=acc, vel=vel)

# Fermeture propre de la connection
# gripper.open_gripper()

robot.close()
