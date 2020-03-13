import subprocess

source_directory = "/media/sf_Share/SHM/4_mapping/"
result_directory = "/media/sf_Share/SHM/5_sam2bam/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    input_file = source_directory + str(sample_id) + '.sam'
    bam_file = result_directory + str(sample_id) + '.bam'
    sorted_bam_file = result_directory + str(sample_id) + '.sorted.bam'   
    with open(bam_file, 'w') as f:
        command = ['samtools',
                   'view',
                   '-S',
                   '-b',
                   input_file]
        subprocess.call(command, stdout=f)
    with open(sorted_bam_file, 'w') as f:
        command = ['samtools',
                   'sort',
                   bam_file]
        subprocess.call(command, stdout=f)
   

