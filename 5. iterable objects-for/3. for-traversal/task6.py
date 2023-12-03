symbol = input().lower()
sentence = list(input().split())
g = len(sentence)
for i in range(g):
    if symbol in sentence[i].lower():
        print(sentence[i])
