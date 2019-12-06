import numpy as np
import random
import argparse

import os, sys

TARGET_STRING = 'Hello GA'


def initialize_population(len_population):

    def initialize_cell():
        cell_word = []
        for _  in range(len(TARGET_STRING)-1):
            rchar = chr(random.randint(0, 32000)%90 + 32)
            cell_word.append(rchar)

        ret_word = ''.join(cell_word)
        return ret_word

    populations = []
    for i in range(len_population):
        populations.append(initialize_cell())

    return populations

    

#fitness function
def string_fitness(string_individual):

    fitness = 0

    for ipos in range(0, len(TARGET_STRING)):
        fitness += abs(ord(string_individual[ipos]) -
                       ord(TARGET_STRING[ipos]))

    return fitness


def mutate_string(string_individual):

    ipos = random.randint(0, len(TARGET_STRING)-1)

    rchar = chr(random.randint(0, 32000)%90 + 32)
    string_individual = string_individual[0:ipos] + rchar + string_individual[(ipos + 1): ]

    return string_individual


#recombination -> 
def crossover(p1_string, p2_string):

    ipos = random.randint(1, len(TARGET_STRING)-2)
    return p1_string[0:ipos] + p2_string[ipos:]


def genetic_optimizer(init_population, elit_percent, max_iteration,
                      mutation_probability):

    pass





def get_args():

    parser = argparse.ArgumentParser('')

    parser.add_argument('')
    parser.add_argument('')


    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = get_args()
