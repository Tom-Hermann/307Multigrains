##
## EPITECH PROJECT, 2022
## B-MAT-500-RUN-5-1-307multigrains-tom.hermann
## File description:
## Makefile
##


MAIN = src/main.py

NAME = 307Multigrains

NAME_TEST = unittest

MAIN_TEST = test/unitest.py


all: $(NAME)

$(NAME):
	cp $(MAIN) ./$(NAME)
	chmod +x $(NAME)

fclean:
	rm -f $(NAME_TEST)
	rm -f $(NAME)

re: fclean all

test:
	cp $(MAIN_TEST) ./$(NAME_TEST)
	chmod +x $(NAME_TEST)
	coverage run --branch $(NAME_TEST)
	coverage report -m

.PHONY: test all fclean re
