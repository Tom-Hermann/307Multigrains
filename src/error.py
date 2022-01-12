##
## EPITECH PROJECT, 2022
## B-MAT-500-RUN-5-1-307multigrains-tom.hermann
## File description:
## error
##


from src.constante import FAILURE, SUCCESS
from sys import stderr

def printUsage():
    print()

def error(argv):
    int_argv = []
    if "-h" in  argv or "--help" in argv:
        printUsage()
        exit(SUCCESS)
    if len(argv) != 9:
        print("Error arg: need 9 arg", file=stderr)
        exit(FAILURE)
    for i in argv:
        try:
            int_argv.append(float(i))
        except:
            print("Error arg: {} must be an interger".format(i), file=stderr)
            exit(FAILURE)
        if int_argv[-1] < 0:
            print("Error arg: {} must be an positive".format(i), file=stderr)
            exit(FAILURE)
    return int_argv[:4], int_argv[4:]
