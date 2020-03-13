import numpy as np
import pandas as pd

source_directory = "/media/sf_Share/SHM/9_SNP_frequency/"
result_directory = "/media/sf_Share/SHM/11_total_mutation_frequency/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

allele_freq_upper_limit = 0.1

output_file = result_directory + 'total_mutation_frequency.csv'
with open(output_file, 'w') as f:
    f.write('sampleID,SNPCount, TotalCount,MutationFreq\n')
    for sample_id in sample_IDs:
        print('Now processing Sample', sample_id)
        snp_file = source_directory + str(sample_id) + '_AlleleFreq.csv'
        coverage_file = source_directory + str(sample_id) + '.coverage'
        coverage_data = np.loadtxt(coverage_file)
        TotalCount = coverage_data.sum()
        SNP_data = pd.read_csv(snp_file)
        snp_counts = SNP_data.loc[ SNP_data['AlleleFreq'] < allele_freq_upper_limit, 'Count' ].values
        TotalSNPCount = snp_counts.sum()
        TotalMutationFreq = float(TotalSNPCount) / TotalCount
        f.write(str(sample_id) + ',' + str(TotalSNPCount) + ',' + str(TotalCount) + ',' + str(TotalMutationFreq) + '\n')
