from Bio import SeqIO


def read_fasta_file(file_path):
    species_names = []
    sequences = []

    # Читаем файл FASTA
    for record in SeqIO.parse(file_path, 'fasta'):
        # Извлекаем название вида из описания
        species_name = record.description.split("|")[1]
        sequence = str(record.seq)  # Получаем последовательность нуклеотидов

        species_names.append(species_name)
        sequences.append(sequence)

    return species_names, sequences


# Пример использования
file_path = 'fasta.mas'
species_names, sequences = read_fasta_file(file_path)

# Выводим названия видов и соответствующие им последовательности
for species_name, sequence in zip(species_names, sequences):
    print(f'Species: {species_name}')
    print(f'Sequence: {sequence}')
    print('---')
