import subprocess

source_directory = "/media/sf_Share/SHM/5_sam2bam/"
result_directory = "/media/sf_Share/SHM/6_indel_realignment/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ref_file = '/media/sf_Share/SHM/Ref/ref.fasta'
# make picard dictionary
picard_dict = ref_file.split('.')[0] + '.dict'
command = ['java',
           '-jar',
           '/usr/local/bin/picard.jar',
           'CreateSequenceDictionary',
           'R=' + ref_file,
           'O=' + picard_dict]
subprocess.call(command) 

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    input_file = source_directory + str(sample_id) + '.sorted.bam'
    # add read-group information to bam file    
    new_input_file = result_directory + str(sample_id) + '.withRG.sorted.bam'
    command = ['java',
               '-jar',
               '/usr/local/bin/picard.jar',
               'AddOrReplaceReadGroups',
               'I=' + input_file,
               'O=' + new_input_file,
               'LB=' + str(sample_id)+ 'lib',
               'PL=illumina',
               'PU=_',
               'SM=' + str(sample_id)]
    subprocess.call(command)
    # index bam file
    command = ['samtools',
              'index',
              new_input_file]
    subprocess.call(command)
    # GATK Indel Alignment
    interval_file = result_directory + str(sample_id) + '.intervals'
    command = ['java',
              '-jar', 
              '-Xmx2g',
              '/usr/local/bin/GenomeAnalysisTK.jar',
              '-T', 'RealignerTargetCreator',
              '-R', ref_file,
              '-I', new_input_file,
              '-o', interval_file]
    subprocess.call(command)
    final_output = result_directory + str(sample_id) + '.realigned.bam'
    command = ['java', 
               '-jar',
               '-Xmx2g',
               '/usr/local/bin/GenomeAnalysisTK.jar',
               '-T', 'IndelRealigner',
               '-R', ref_file,
               '-I', new_input_file,
               '-targetIntervals', interval_file,
               '-o', final_output]
    subprocess.call(command)

   

