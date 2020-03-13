import pandas as pd
import numpy as np

source_directory = "/media/sf_Share/SHM/8_varscan/"
coverage_directory = "/media/sf_Share/SHM/9_SNP_frequency/"
result_directory = "/media/sf_Share/SHM/9_SNP_frequency/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

IUPAC_Codes = {'A': set(['A']),
               'C': set(['C']),
               'G': set(['G']),
               'T': set(['T']),
               'R': set(['A', 'G']),
               'Y': set(['T', 'C']),
               'S': set(['G', 'C']),
               'W': set(['A', 'T']),
               'K': set(['G', 'T']),
               'M': set(['A', 'C'])}

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    output_file = result_directory + str(sample_id) + '_AlleleFreq.csv'
    coverage_file = coverage_directory + str(sample_id) + '.coverage'
    coverage_data = np.loadtxt(coverage_file)
    input_file = source_directory + str(sample_id) + '.SNPs'
    SNPs = pd.read_table(input_file)
    with open(output_file, 'w') as f: 
        f.write('position,Reference,SNP,Count,AlleleFreq\n')
        for i in SNPs.index:
            reference_base = SNPs.loc[i, 'Ref']
            consensus_base = SNPs.loc[i, 'Cons']
            snp_base = IUPAC_Codes[consensus_base] - set([reference_base])
            actual_base = list(snp_base)[0]
            position = SNPs.loc[i, 'Position']
            total_depth = coverage_data[position - 1]
            snp_depth = SNPs.loc[i, 'Reads2']
            allele_frequency = float (snp_depth) / total_depth
            f.write(str(position) + ',' + reference_base + ',' + actual_base + ',' + str(snp_depth) + ',' + str(allele_frequency) + '\n')
