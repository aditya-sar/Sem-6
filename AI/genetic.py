import random

def fitness(individual):
    return sum(individual)

def genetic_algorithm(population_size, chromosome_size, generations, mutation_rate):
    population = [[random.randint(0, 1) for j in range(chromosome_size)] for i in range(population_size)]

    for generation in range(generations):
        fitness_scores = [fitness(individual) for individual in population]
        parents = []
        for i in range(population_size // 2):
            parent1 = population[fitness_scores.index(max(fitness_scores))]
            fitness_scores[fitness_scores.index(max(fitness_scores))] = -1

            parent2 = population[fitness_scores.index(max(fitness_scores))]
            fitness_scores[fitness_scores.index(max(fitness_scores))] = -1

            parents.append((parent1, parent2))
        
        population = []
        for parent1, parent2 in parents:
            child1, child2 = parent1[:], parent2[:]
            for i in range(chromosome_size):
                if random.random() < mutation_rate:
                    child1[i] = 1 - child1[i]
                if random.random() < mutation_rate:
                    child2[i] = 1 - child2[i]
            population.append(child1)
            population.append(child2)
    
    fitness_scores = [fitness(individual) for individual in population]
    return population[fitness_scores.index(max(fitness_scores))]


fittest_individual = genetic_algorithm(
    population_size=100, chromosome_size=10, generations=50, mutation_rate=0.01)
print("Fittest individual:", fittest_individual)
