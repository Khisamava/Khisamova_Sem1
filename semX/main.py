text = input("Enter text: ")
text_low = text.lower()
cipher = "егпжонщюэбчмяхыцилдшарсйзвьёктф"
rus = "шифрвженаткдльйоячёспгмзыхбцэую"
for i in range(len(text_low)):
    for j in range(len(cipher)):
        if text_low[i] == cipher[j]:
            print(rus[j], end="")
    if text_low[i] not in cipher:
        print(text_low[i], end="")
    