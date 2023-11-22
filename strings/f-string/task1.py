import re


def clean_mas_file(file_path, output_file_path):
    species_names = []  # Список для хранения названий видов
    cleaned_lines = []  # Список для хранения очищенных строк

    # Открываем файл для чтения
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                # Извлекаем название вида
                species_name = line[1:]  # Игнорируем символ '>'
                species_names.append(species_name)
            else:
                # Очищаем строку от нежелательных символов
                cleaned_line = re.sub(r'[^ATCG]', '', line)
                if cleaned_line:
                    cleaned_lines.append(cleaned_line)

    # Открываем новый файл для записи очищенных строк
    with open(output_file_path, 'w') as output_file:
        # Записываем очищенные строки в новый файл
        output_file.writelines(cleaned_lines)

    return species_names


# Пример использования
input_file_path = 'fasta.mas'
output_file_path = 'example.mas'
species_names = clean_mas_file(input_file_path, output_file_path)

# Выводим список названий видов
for species_name in species_names:
    print(species_name)
