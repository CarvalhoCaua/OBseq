import pandas as pd

seq = str(input('Sequência: '))

seqcomplementar = ""
for i in seq:
    if i == "A":
        seqcomplementar += "T"
    elif i == "T":
        seqcomplementar += "A"
    elif i == "C":
        seqcomplementar += "G"
    elif i == "G":
        seqcomplementar += "C"
seqRNA = seq.replace('T', 'U')
data = {
    'A': ['Sequência',
          'Tamanho',
          'A', 'T', 'G', 'C',
          'Três Primeiras Bases', 'Três Últimas Bases',
          'Sequência Complementar',
          'Sequência de RNA'],
    'B': [seq,
          len(seq),
          seq.count('A'), seq.count('T'), seq.count('G'), seq.count('C'),
          seq[:3],
          seq[-3:],
          seqcomplementar,
          seqRNA]
}


resultado = pd.DataFrame(data)
resultado.to_csv('resultado.csv')
resultado.to_csv('resultado.txt', sep='\t', index=False)
print(resultado)

