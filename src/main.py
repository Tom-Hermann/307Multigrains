#!/usr/bin/python3
##
## EPITECH PROJECT, 2022
## B-MAT-500-RUN-5-1-307multigrains-tom.hermann
## File description:
## main
##


from sys import argv
from src.error import error

def main():
    error(argv[1:])
    exit(0)

if __name__ == "__main__":
    main()
