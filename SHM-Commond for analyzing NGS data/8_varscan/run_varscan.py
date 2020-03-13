import subprocess

source_directory = "/media/sf_Share/SHM/7_pileup/"
result_directory = "/media/sf_Share/SHM/8_varscan/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    input_file = source_directory + str(sample_id) + '.pileup'
    output_file = result_directory + str(sample_id) + '.SNPs'
    with open(output_file, 'w') as f:
        command = ['varscan',
                   'pileup2snp',
                   input_file,
                   '--min-reads2', '2',
                   '--min-var-freq', '0.000001']
        subprocess.call(command, stdout=f)
  

