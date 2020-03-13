from Bio import SeqIO

ref = [seq for seq in SeqIO.parse('/media/sf_Share/SHM/Ref/NGS-Ref-1.TXT', 'fasta')]
with open('/media/sf_Share/SHM/Ref/ref.fasta', 'w') as f:
    SeqIO.write(ref[0], f, 'fasta')
