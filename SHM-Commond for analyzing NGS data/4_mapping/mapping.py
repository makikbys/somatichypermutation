import subprocess

source_directory = "/media/sf_Share/SHM/3_pairend_merge/"
result_directory = "/media/sf_Share/SHM/4_mapping/"

ref_file = '/media/sf_Share/SHM/Ref/NGS-Ref-1.TXT'

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    input_file = source_directory + str(sample_id) + '_.merged.assembled.fastq'
    output_file = result_directory + str(sample_id) + '.sam'   
    with open(output_file, 'w') as f:
        command = ['bwa',
                   'mem',
                   '-t', '2',
                   ref_file,
                   input_file]
        subprocess.call(command, stdout=f)
   

