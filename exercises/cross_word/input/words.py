path = 'italian.txt'

words = []
with open('../input/italian.txt', 'r') as file:
    for word in file.readlines():
        words.append(word.replace('\n', ''))

