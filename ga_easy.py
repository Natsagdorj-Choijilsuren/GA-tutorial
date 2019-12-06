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
    string_individual = string_individual[0:ipos] + rchar + string_individual[(ipos + 1):]

    return string_individual


#recombination -> 
def crossover(p1_string, p2_string):

    ipos = random.randint(1, len(TARGET_STRING)-2)
    return p1_string[0:ipos] + p2_string[ipos:]


def genetic_optimizer(init_population, elit_percent, max_iteration,
                      mutation_probability):

    initialized_population = initialized_population(init_population)
    original_population_size = len(initialized_population)
    
    top_elite = int(elit_percent*original_population_size)
    population = initialized_population
    
    for i in range(max_iteration):

        individual_scores = [(string_fitness(v), v)
                             for v in population]
    
        individual_scores.sort()

        ranked_individuals = [v for (s, v) in individual_scores]

        population = ranked_individuals[0:top_elite]

        while len(population) < original_population_size:

            if random.random() < mutation_probability:

                c = random.randint(0, top_elite)
                population.append(mutate_string(ranked_individuals[c]))
                            
            else:

                c1 = random.randint(0, top_elite)
                c2 = random.randint(0, top_elite)

                population.append(crossover(ranked_individuals[c1],
                                            ranked_individuals[c2]))

        if individual_scores[0][0] == 0:
            return individual_scores[0][1]

    return individual_scores[0][1]


def get_args():

    parser = argparse.ArgumentParser('')

    parser.add_argument('--init_population_size', type=int,
                        default=100)
    parser.add_argument('--mutation_percentage', type=float,
                        default=0.25)
    parser.add_argument('--elite_percentage', type=float,
                        default=0.1)
    parser.add_argument('--max_iteration', type=int,
                        default=100)
    
    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = get_args()

    genetic_optimizer(args.init_population_size, args.elite_percentage,
                      args.max_iteration, args.mutation_percentage)

    
