import numpy as np

# output data as tsv
"""
sample_id	chrom	start	end	cn_a	cn_b
taxon_1	chrom1	0	1	1	1
taxon_1	chrom1	1	2	1	0
taxon_1	chrom1	2	3	1	0
taxon_1	chrom1	3	4	1	1
taxon_1	chrom1	4	5	1	1
taxon_1	chrom2	0	1	1	1
taxon_1	chrom2	1	2	1	1
taxon_1	chrom2	2	3	1	1
"""

def generate_random_samples(num_samples, num_chromosomes):
    return 0

class Cell:
    def __init__(self, num_chromosomes, chromosome_length):
        self.num_chromosomes = num_chromosomes
        self.chromosome_length = chromosome_length
        self.genome = np.zeros((num_chromosomes, chromosome_length), dtype=int)  # Initialize genome with all zeros
    
    def grow(self):
        # Simulate cell growth
        pass
    
    def introduce_mutation(self, mutation_rate):
        # Introduce mutations with a certain probability
        for i in range(self.num_chromosomes):
            for j in range(self.chromosome_length):
                if np.random.rand() < mutation_rate:
                    # Mutate chromosome i, position j
                    self.genome[i, j] = np.random.randint(0, 2)  # Random mutation (0 or 1)

def simulate(num_generations, num_cells, num_chromosomes, chromosome_length, mutation_rate):
    # Initialize cells
    cells = [Cell(num_chromosomes, chromosome_length) for _ in range(num_cells)]
    
    # Simulate multiple generations
    for generation in range(num_generations):
        print(f"Generation {generation + 1}:")
        
        # Grow each cell
        for cell in cells:
            cell.grow()
        
        # Introduce mutations
        for cell in cells:
            cell.introduce_mutation(mutation_rate)
        
        # Print the state of each cell
        for i, cell in enumerate(cells):
            print(f"Cell {i + 1}: {cell.genome}")


def main():
    # Randomize
    np.random.seed(3)
    
    # Parameters
    num_generations = 5
    num_cells = 3
    num_chromosomes = 4
    mutation_rate = 0.5
    chromosome_length = 50

    # Simulate
    simulate(num_generations, num_cells, num_chromosomes, chromosome_length, mutation_rate)

if __name__ == "__main__":
    main()
    
    
    


