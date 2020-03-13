import subprocess

source_directory = "/media/sf_Share/SHM/1_adapter_trim/"
result_directory = "/media/sf_Share/SHM/2_quality_trim/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    R1_file = source_directory + str(sample_id) + '_1.fastq.trim'
    R2_file = source_directory + str(sample_id) + '_2.fastq.trim'    
    R1_output_file = result_directory + str(sample_id) + '_1.fastq.trim.LQ' 
    R2_output_file = result_directory + str(sample_id) + '_2.fastq.trim.LQ'  
    Single_output_file = result_directory + str(sample_id) + '_single.fastq'
    command = ['sickle',
              'pe',
              '-f', R1_file,
              '-r', R2_file,
              '-t', 'sanger',
              '-o', R1_output_file,
              '-p', R2_output_file,
              '-s', Single_output_file,
              '-q', '20',
              '-l', '50']
    subprocess.call(command)
   

