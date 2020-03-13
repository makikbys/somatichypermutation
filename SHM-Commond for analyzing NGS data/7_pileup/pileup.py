import subprocess

source_directory = "/media/sf_Share/SHM/6_indel_realignment/"
result_directory = "/media/sf_Share/SHM/7_pileup/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ref_file = '/media/sf_Share/SHM/Ref/ref.fasta'

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    input_file = source_directory + str(sample_id) + '.realigned.bam'
    output_file = result_directory + str(sample_id) + '.pileup'
    with open(output_file, 'w') as f:
        command = ['samtools',
                   'mpileup',
                   '-d', '1000000',
                   '-L', '1000000',
                   '-f', ref_file,
                   input_file]
        subprocess.call(command, stdout=f)
  

