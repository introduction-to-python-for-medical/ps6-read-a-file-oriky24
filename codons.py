def create_codon_dict(file_path):
    path = "data/codons.txt"
    with open(path, 'r') as file:
         rows = file.readlines()
    
    amino_acids_dict = {}
    for row in rows:
        codon_row = row.strip().split('\t')
        codon = codon_row[0]
        amino_acid = codon_row[2]
        amino_acids_dict[codon] = amino_acid
    return amino_acids_dict
