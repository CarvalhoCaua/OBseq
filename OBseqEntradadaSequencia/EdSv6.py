seq = input(str("Sequência: "))
if seq[-4:] == ".txt":
    seq = open(seq)
    seq = seq.read()
    print(seq)
else:
    print(seq)
