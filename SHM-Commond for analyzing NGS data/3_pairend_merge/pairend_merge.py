import subprocess

source_directory = "/media/sf_Share/SHM/2_quality_trim/"
result_directory = "/media/sf_Share/SHM/3_pairend_merge/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    R1_file = source_directory + str(sample_id) + '_1.fastq.trim.LQ'
    R2_file = source_directory + str(sample_id) + '_2.fastq.trim.LQ' 
    output_file = result_directory + str(sample_id) + '_.merged'   
    command = ['pear',
              '-f', R1_file,
              '-r', R2_file,
              '-o', output_file]
    subprocess.call(command)
   

