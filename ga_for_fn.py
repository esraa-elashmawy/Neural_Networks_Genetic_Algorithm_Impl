# -*- coding: utf-8 -*-
"""GA_for_fn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/121EdEBqwP6Zfbq-Q4pHudSDYvZNP7lC5
"""

import numpy
import random

# sol_per_pop = (1000,2) #x pop_per_sol=8
# num_parents_mating = 4
# pop_size = (sol_per_pop)

# new_value_population = numpy.random.uniform(low=-5.0, high=5.0, size=pop_size)

# new_value_population

def cal_pop_fitness(pop):
 fitness=[0 for x in range(len(pop))] 
 for i in range(len(pop)):
  fitness[i] = (pop[i][0]-3.14)**2 +(pop[i][1]-2.72)**2+ numpy.sin((3*pop[i][0])+1.41)+ numpy.sin((4*pop[i][1])-1.73)
 return fitness

def select_mating_pool(pop, fitness, num_parents):
 # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
 parents = numpy.empty((num_parents, pop.shape[1])) 
 for parent_num in range(num_parents):
  min_fitness_idx = numpy.where(fitness == numpy.min(fitness))
  min_fitness_idx = min_fitness_idx[0][0]
  parents[parent_num, :] = pop[min_fitness_idx, :]
  fitness[min_fitness_idx] = 99999999999
 return parents

def crossover(parents, offspring_size):
     offspring = numpy.empty(offspring_size)
     # The point at which crossover takes place between two parents. Usually, it is at the center.
     crossover_point = numpy.uint8(offspring_size[1]/2)
 
     for k in range(offspring_size[0]):
         # Index of the first parent to mate.
         parent1_idx = k%parents.shape[0]
         # Index of the second parent to mate.
         parent2_idx = (k+1)%parents.shape[0]
         # The new offspring will have its first half of its genes taken from the first parent.
         offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
         # The new offspring will have its second half of its genes taken from the second parent.
         offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
     return offspring

def mutation(offspring_crossover,mutation_prob):
    #number of genes that are going to be mutated:
    mutation_number=round(len(offspring_crossover)*mutation_prob)
    #print(mutation_number)
    mutation_gene_idxs=random.sample(range(0, len(offspring_crossover)), mutation_number)
    #print(mutation_gene_idxs)
    for idx in mutation_gene_idxs:
        # The random value to be added to the gene.
        random_value = numpy.random.uniform(-5, 5, 1)
        #select randomly which input will be mutauted (the x or y)
        XorY = random.randint(0, 1)
        if XorY ==1:
          offspring_crossover[idx, 1] =  random_value
        else:
          offspring_crossover[idx, 0] =  random_value

    return offspring_crossover

# num_generations = 10;
# num_parents_mating = 50
# AllMin=[];
# AllMinFitness=[];
# for generation in range(num_generations):
#    # Measuring the fitness of each chromosome in the population.
#      fitness = cal_pop_fitness(new_value_population)
#    # Selecting the best parents in the population for mating.
#      parents = select_mating_pool(new_value_population, fitness,num_parents_mating)
#    # Generating next generation using crossover.
#      offspring_crossover = crossover(parents,offspring_size=(pop_size[0]-parents.shape[0], 2))
#    # Adding some variations to the offsrping using mutation.
#      offspring_mutation = mutation(offspring_crossover)
     
#   # Creating the new population based on the parents and offspring.
#      new_value_population[0:len(parents)] = parents
#      new_value_population[len(parents):] = offspring_mutation
#      #print(new_value_population);
#   #must store the value that outputs the maximum fitness in each iteration 
#      Allfitness = cal_pop_fitness(new_value_population)
#      Minfitness_idx=numpy.argmin(Allfitness)
#     #  if new_value_population[Maxfitness_idx] >MaxVal:
#     #    MaxVal=new_value_population[Maxfitness_idx]
#      AllMin.append(new_value_population[Minfitness_idx])
#      AllMinFitness.append(min(Allfitness))

# print(new_value_population);
# print(AllMin)
# print(AllMinFitness)

# gen=[0 for x in range(len(AllMin))] 
# for n in range(10):
#   gen[n]=n+1

# gen

# import matplotlib.pyplot as plt
# import numpy as np
# ypoints = np.array([1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15])

# plt.plot(gen,AllMinFitness)
# plt.show()

# ALLX=[0 for x in range(len(AllMin))] 
# ALLY=[0 for x in range(len(AllMin))] 

# for x in range(len(AllMin)):
#   ALLX[x]=AllMin[x][0]
#   ALLY[x]=AllMin[x][1]

# print(ALLX)
# print(ALLY)

# import matplotlib.pyplot as plt
# x = ALLX
# y = ALLY
# print(x)
# print(y)
# # n = AllMinFitness

# plt.scatter(x, y, c ="blue")
# plt.show()

# # for i, txt in enumerate(n):
# #     ax.annotate(txt, (z[i], y[i]))