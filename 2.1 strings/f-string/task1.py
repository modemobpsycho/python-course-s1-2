from Bio import SeqIO


def remove_duplicate_sequences(file_path, output_file_path):
    species_sequences = {}

    for record in SeqIO.parse(file_path, 'fasta'):
        species_name = record.description.split("|")[1]

        if species_name in species_sequences:
            if sequence not in species_sequences[species_name]:
                species_sequences[species_name].append(sequence)
        else:
            species_sequences[species_name] = [sequence]

    with open(output_file_path, 'w') as output_file:
        for species_name, sequences in species_sequences.items():
            for index, sequence in enumerate(sequences):
                record_id = f"{species_name}_{index+1}"
                record_description = f">{record_id}"
                output_file.write(f"{record_description}\n{sequence}\n")

    print("Удаление дубликатов завершено.")


# Пример использования
input_file_path = ''
output_file_path = ''
remove_duplicate_sequences(input_file_path, output_file_path)
