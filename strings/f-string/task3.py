from Bio import SeqIO
import time

start = time.time()

seen = []
records = []

for record in SeqIO.parse("fasta.fas", "fasta"):
    if str(record.seq) not in seen:
        seen.append(str(record.seq))
        records.append(record)


# writing to a fasta file
SeqIO.write(records, "new_fasta.fas", "fasta")
end = time.time()

print(f"Run time is {(end - start)/60}")
