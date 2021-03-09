line = '(()[[]])([])'




def value(line):
    words = list(line)
    for i in range(len(line)-1):
        if line[i] =='(' and line[i+1] ==')':
            words.pop(i)
            words[i] = 2
        if line[i] =='[' and line[i+1] ==']':
            words.pop(i)
            words[i] = 2
    return words

print(value(line))

