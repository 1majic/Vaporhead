import codecs

text = ''
with codecs.open('test.txt', 'rb+', encoding='utf-8') as f:
    text = f.read()
    text = text.replace('.\n', '.')
    text = text.replace('.\n', '...')
    text = text.replace('?\n', '?')
    text = text.replace('!\n', '!')

with codecs.open('test.txt', 'w', encoding='utf-8') as f:
    f.write(text)
    f.close()
# import os
#
# directory = 'C:/Users/79964/Desktop/0/VaporHead/Davit Rada'
# files = os.listdir(directory)
# print(files)