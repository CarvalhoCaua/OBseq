seq = "ATCG"
print(seq)
print(len(seq))
print(seq.count("A"))
print(seq.count("T"))
print(seq.count("C"))
print(seq.count("G"))
print(seq[:3])
print(seq[-3:])
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
print(seqcomplementar)
sequenciaRNA = seq.replace('T', 'U')
print(sequenciaRNA)
