import pandas as pd

seq1 = 'ATCG'
seq2 = 'TCGA'

seqcomplementar1 = ""
for i in seq1:
    if i == "A":
        seqcomplementar1 += "T"
    elif i == "T":
        seqcomplementar1 += "A"
    elif i == "C":
        seqcomplementar1 += "G"
    elif i == "G":
        seqcomplementar1 += "C"
seqRNA1 = seq1.replace('T', 'U')
data1 = {
    'A': ['Sequência',
          'Tamanho',
          'A', 'T', 'G', 'C',
          'Três Primeiras Bases', 'Três Últimas Bases',
          'Sequência Complementar',
          'Sequência de RNA'],
    'B': [seq1,
          len(seq1),
          seq1.count('A'), seq1.count('T'), seq1.count('G'), seq1.count('C'),
          seq1[:3],
          seq1[-3:],
          seqcomplementar1,
          seqRNA1]
}

seqcomplementar2 = ""
for i in seq2:
    if i == "A":
        seqcomplementar2 += "T"
    elif i == "T":
        seqcomplementar2 += "A"
    elif i == "C":
        seqcomplementar2 += "G"
    elif i == "G":
        seqcomplementar2 += "C"
seqRNA2 = seq2.replace('T', 'U')
data2 = {
    'A': ['Sequência',
          'Tamanho',
          'A', 'T', 'G', 'C',
          'Três Primeiras Bases', 'Três Últimas Bases',
          'Sequência Complementar',
          'Sequência de RNA'],
    'B': [seq2,
          len(seq2),
          seq2.count('A'), seq2.count('T'), seq2.count('G'), seq2.count('C'),
          seq2[:3],
          seq2[-3:],
          seqcomplementar2,
          seqRNA2]
}

resultado1 = pd.DataFrame(data1)
resultado1.to_csv('resultado1.csv')
resultado1.to_csv('resultado1.txt', sep='\t', index=False)

resultado2 = pd.DataFrame(data2)
resultado2.to_csv('resultado2.csv')
resultado2.to_csv('resultado2.txt', sep='\t', index=False)