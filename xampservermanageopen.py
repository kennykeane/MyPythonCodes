##########################################################
#####                                                  ###
#####  script to open gui of xampserver to arch linux				                                   ###								
#####   by Faustino Quifuta                                               ###
####
#####
##########################################################
#: /usr/bin/python3
import os
import sys
choice =input("Do you want open xampserver-manager ? y/n:   ")

if choice == 'y' or choice == 'Y':
	os.system('sudo  /opt/lampp/manager-linux-x64.run')

elif choice == n or choice == N:
	exit()

