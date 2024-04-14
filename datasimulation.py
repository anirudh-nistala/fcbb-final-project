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
    def __init__(self, num_chromosomes, chromosome_length, copy_from=None):
        self.num_chromosomes = num_chromosomes
        self.chromosome_length = chromosome_length
        if copy_from is None:
            self.genome_a = np.zeros((num_chromosomes, chromosome_length), dtype=int)  # Initialize genome a with all zeros
            self.genome_b = np.zeros((num_chromosomes, chromosome_length), dtype=int)  # Initialize genome b with all zeros
        else:
            self.genome_a = np.copy(copy_from.genome_a)
            self.genome_b = np.copy(copy_from.genome_b)
    
    def introduce_mutation(self, mutation_rate):
        # Introduce mutations with a certain probability
        for i in range(self.num_chromosomes):
            for j in range(self.chromosome_length):
                if np.random.rand() < mutation_rate:
                    # Mutate chromosome i, position j
                    self.genome_a[i, j] = 1  # Random mutation
                if np.random.rand() < mutation_rate:
                    self.genome_b[i, j] = 1

def simulate(num_generations, num_cells, num_chromosomes, chromosome_length, mutation_rate, growth_rate):
    # Initialize cells
    cells = [Cell(num_chromosomes, chromosome_length) for _ in range(num_cells)]
    
    # Simulate multiple generations
    for generation in range(num_generations):
        
        # Introduce mutations
        for cell in cells:
            if np.random.rand() < growth_rate:
                cells.append(Cell(num_chromosomes, chromosome_length, cell))
            cell.introduce_mutation(mutation_rate)

    return cells


def main():
    # Randomize
    np.random.seed(3)
    
    # Parameters
    num_generations = 10
    num_cells = 3
    num_chromosomes = 4
    mutation_rate = 0.01
    growth_rate = 0.2
    chromosome_length = 10

    # Simulate
    cells = simulate(num_generations, num_cells, num_chromosomes, chromosome_length, mutation_rate, growth_rate)

    # Output cells as tsv
    file_name = "output.tsv"
    with open(file_name, "w") as f:
        f.write("sample_id\tchrom\tstart\tend\tcn_a\tcn_b\n")  # Write header
        for idx, cell in enumerate(cells):
            sample_id = f"sample_{idx + 1}"
            for chrom_idx in range(num_chromosomes):
                for start, end in zip(range(0, chromosome_length, 1), range(1, chromosome_length + 1, 1)):
                    chrom = f"chrom{chrom_idx + 1}"
                    cn_a = int(cell.genome_a[chrom_idx, start:end])
                    cn_b = int(cell.genome_b[chrom_idx, start:end])
                    f.write(f"{sample_id}\t{chrom}\t{start}\t{end}\t{cn_a}\t{cn_b}\n")
    print(f"Data has been written to '{file_name}'")
    

if __name__ == "__main__":
    main()
    
    
    


