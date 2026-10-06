# DNA Sequence Analysis

dna = input("Enter DNA sequence: ").upper()

# Validate sequence
if not all(base in "ATGC" for base in dna):
    print("Invalid DNA sequence")
    exit()

print("\nSequence:", dna)
print("Length:", len(dna))

# GC Content
gc = (dna.count("G") + dna.count("C")) / len(dna) * 100
print("GC Content: {:.2f}%".format(gc))

# Motif search
motif = input("Enter motif to search: ").upper()
positions = []

for i in range(len(dna) - len(motif) + 1):
    if dna[i:i + len(motif)] == motif:
        positions.append(i + 1)

print("Motif:", motif)
print("Occurrences:", len(positions))
print("Positions:", positions)

# Reverse Complement
complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
reverse_complement = "".join(complement[b] for b in reversed(dna))

print("Reverse Complement:", reverse_complement)

# Simple coding region / ORF detection
start = dna.find("ATG")

if start != -1:
    stop_codons = ["TAA", "TAG", "TGA"]
    stop = -1

    for i in range(start + 3, len(dna) - 2, 3):
        if dna[i:i + 3] in stop_codons:
            stop = i
            break

    if stop != -1:
        print("Coding Region:", dna[start:stop + 3])
        print("ORF Length:", stop + 3 - start, "bp")
    else:
        print("No complete coding region found")
else:
    print("No start codon found")