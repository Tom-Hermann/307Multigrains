##
## EPITECH PROJECT, 2022
## B-MAT-500-RUN-5-1-307multigrains-tom.hermann
## File description:
## error
##


from src.constante import FAILURE, SUCCESS

def printUsage():
    print()

def error(argv):
    if "-h" in  argv or "--help" in argv:
        printUsage()
        exit(SUCCESS)