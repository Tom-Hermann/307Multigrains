#!/usr/bin/python3
##
## EPITECH PROJECT, 2022
## B-MAT-500-RUN-5-1-307multigrains-tom.hermann
## File description:
## main
##


from sys import argv
from src.error import error
from src.simplexe import simplexe_methode

def main():
    resources, prices = error(argv[1:])
    print("Resources:", end='')
    for re, i in zip(resources, range(len(resources))):
        print(" {} F{}".format(int(re), i + 1), end=',' if i != 3 else '\n\n')
    simplexe_methode(resources, prices)
    exit(0)

if __name__ == "__main__":
    main()
