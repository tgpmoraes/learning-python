#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random

class Greeter(object):
    #Toda vez que se cria uma nova instância da classe, a função abaixo será inicializada, assim podemos passar uma variável que poderá ser usada por outras funções da classe
    def __init__(self, name):
	#self nos permite criar uma variável para ser usadas em outras funções da classe
	self.name = name

    #Sempre colocará self em uma função definida para uma classe
    def hello(self):
	print("Hello " + self.name)


    def goodbye(self):
	print("Goodbye " + self.name)

#g = Greeter("Mariane")
#No momento de chamar a função dentro da classe, ignoramos a variável self
#g.hello()
#g.goodbye()

#Nova instância da classe existente
#g2 = Greeter("Tiago")
#g2.hello()
#g2.goodbye()

class Die(object):
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

class Deck(object):
    def shuffle(self):
	suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
	ranks = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
	self.cards = []
	for suit in suits:
	    for rank in ranks:
		self.cards.append(rank + " of " + suit)
	random.shuffle(self.cards)

    def deal(self):
	#Método no tipo de dados lista, onde pega o último e o remove da lista neste caso, já que não esta sendo fornecido o índice
	return self.cards.pop()	

#d = Die(20)
d = Deck()
d.shuffle()
print(d.deal())
print(d.deal())
print(d.deal())

