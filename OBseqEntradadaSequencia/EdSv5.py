formato = input(str("Digitar ou Arquivo: "))
if formato == "Digitar":
    sequencia = input(str("Digite a Sequência: "))
    print(sequencia)
else:
    sequencia = input(str("Digite o Nome do Arquivo: "))
    sequencia = open(sequencia)
    sequencia = sequencia.read()
    print(sequencia)

