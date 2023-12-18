
# Каждый тест состоит из нескольких наборов входных данных. В первой строке находится одно целое число
# t(1≤t≤100) — количество наборов входных данных. Далее следует описание наборов входных данных. Единственная строка каждого набора входных данных #содержит одну непустую строку из больших латинских букв длиной не более 20 символов — привезённый набор букв.

from collections import Counter


def can_form_word(word, letters):
    word_counter = Counter(word)
    letters_counter = Counter(letters)

    for char in word_counter:
        if word_counter[char] > letters_counter[char]:
            return "No"

    return "Yes"


num_sets = int(input())

for _ in range(num_sets):
    word = "TINKOFF"
    letters = input()
    result = can_form_word(word, letters)
    print(result)
