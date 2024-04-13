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

def main():
    np.random.seed(3)
    num_samples = 10
    num_chromosomes = 4
    
    


