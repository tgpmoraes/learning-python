#!/usr/bin/python
# -*- coding: utf-8 -*-

capitals_dict = {
    'Acre' : 'Rio Branco',
    'Alagoas' : 'Maceió',
    'Amapá' : 'Macapá',
    'Amazonas' : 'Manaus',
    'Bahia' : 'Salvador',
    'Ceará' : 'Fortaleza',
    'Distrito Federal' : 'Brasília',
    'Espírito Santo' : 'Vitória',
    'Goiás' : 'Goiânia',
    'Maranhão' : 'São Luiz',
    'Mato Grosso' : 'Cuiabá',
    'Mato Grosso do Sul' : 'Campo Grande',
    'Minas Gerais' : 'Belo Horizonte',
    'Pará' : 'Belém',
    'Paraíba' : 'João Pessoa',
    'Paraná' : 'Curitiba',
    'Pernambuco' : 'Recife',
    'Piauí' : 'Teresina',
    'Rio de Janeiro' : 'Rio de Janeiro',
    'Rio Grande do Norte' : 'Natal',
    'Rio Grande do Sul' : 'Porto Alegre',
    'Rondônia' : 'Porto Velho',
    'Roraima' : 'Boa Vista',
    'Santa Catarina' : 'Florianópolis',
    'São Paulo' : 'São Paulo',
    'Sergipe' : 'Aracajú',
    'Tocantins' : 'Palmas'
}

import os, sys
import random

states = list(capitals_dict.keys())
while True:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = raw_input("Qual é a capital do(a) " + state + "? ")
    
    if capital_guess.lower() == "quit":
	break
    elif capital_guess == capital:
        print("Correto! Bom trabalho.")
    else:
        print("Incorreto. A capital do(a) " + state + " é " + capital + ".")
    
print("Terminado")
