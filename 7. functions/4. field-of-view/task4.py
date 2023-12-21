def get_word_indices(strings: list[str]) -> dict:
  '''Функция возвращает словарь, где ключи — это уникальные слова из
  списка строк в нижнем регистре, а значения —
  это списки индексов строк, в которых эти слова встречаются'''
  dct = {j: 0 for i in strings for j in i.lower().split()}
  for i in dct:
    z = []
    for j in range(len(strings)):
      if i in strings[j].lower():
        z.append(j)
    dct[i] = (z)
  return dct