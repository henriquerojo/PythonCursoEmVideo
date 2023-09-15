while True:
    termo = 1296

    for i in range(1, 7):
        if i % 2 == 0:
            base = 2
            termo = base ** (i // 2)
        else:
            base = i + 1
            termo = base ** 2

        print(termo, end=", ")

    print()  # Nova linha

    continuar = input("Deseja continuar gerando a sequência?  (S/N): ")
    if continuar.upper() != 'S':
        break
