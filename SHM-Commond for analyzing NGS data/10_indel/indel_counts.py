import re
import collections

source_directory = "/media/sf_Share/SHM/7_pileup/"
result_directory = "/media/sf_Share/SHM/10_indel/"

sample_IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

indel_pattern = re.compile(r"[+-]\w+")

for sample_id in sample_IDs:
    print('Now processing Sample', sample_id)
    input_file = source_directory + str(sample_id) + '.pileup'
    output_file = result_directory + str(sample_id) + '_indels.csv'
    with open(output_file, 'w') as f:
       f.write('Position,IndelPattern,Count\n')
       for line in open(input_file):
           elements = line.rstrip().split('\t')
           position = elements[1] 
           pileup_string = elements[4]
           indel_list = indel_pattern.findall(pileup_string)
           indel_counts = collections.Counter(indel_list)
           for indel, indel_count in indel_counts.items():
               f.write(position + ',' + indel + ',' + str(indel_count) + '\n')
            

