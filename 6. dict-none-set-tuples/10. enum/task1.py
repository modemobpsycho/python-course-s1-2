words = ['feel', 'graduate', 'movie', 'fashionable', 'bacon',
         'drop', 'produce', 'acquisition', 'cheap', 'strength',
         'master', 'perception', 'noise', 'strange', 'am']
words_with_position = []

for i in enumerate(words, start=1):
    words_with_position.append(i[::-1])
print(words_with_position)
