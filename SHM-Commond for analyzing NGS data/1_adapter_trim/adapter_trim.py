import subprocess

source_directory = "/media/sf_Share/SHM/"
result_directory = "/media/sf_Share/SHM/1_adapter_trim/"

five_primer = "TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGCAGCTCAGAACAGTCCAGTGTAGG"
three_primer = "GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAGAAAGGACAGTGCTTAGATCCGAGG"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sample_id in sample_IDs:
    R1_file = source_directory + str(sample_id) + '_1.fastq'
    R2_file = source_directory + str(sample_id) + '_2.fastq'    
    R1_output_file = result_directory + str(sample_id) + '_1.fastq.trim' 
    R2_output_file = result_directory + str(sample_id) + '_2.fastq.trim'  
    command = ['cutadapt',
               '-g', five_primer,
               '-G', three_primer,
               '-o', R1_output_file,
               '-p', R2_output_file,
               '-O', '10',
               '-m', '50',
               '-q', '17',
               '-f', 'fastq',
               R1_file,
               R2_file] 
    subprocess.call(command)
   

