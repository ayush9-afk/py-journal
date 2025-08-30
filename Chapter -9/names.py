# names = open('names.txt', mode = 'r', encoding='utf-8').read()
# print(names)

with open('names.txt', mode = 'a') as f:
    f.write("\nBhoomi Hirwani")