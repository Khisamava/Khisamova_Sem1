def freq_analys(text):
    freq = {}
    for a in text:
        if freq.get(a) is None:
            freq[a] = 1
        else:
            freq[a] += 1
    return freq


def start():
    text = input("Введите текст: ")
    symbols_to_remove = ",!?-. /:;…«»—\xa0"
    for symbol in symbols_to_remove:
        text = text.replace(symbol, "")
    text_low = text.lower()
    freq = freq_analys(text_low)
    print(freq)
    print()
    print(len(text_low))




start()