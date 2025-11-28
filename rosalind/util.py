def read_file_into_lines(file_path):
    """
    A simple function to read a file into
    a list of lines, removing the newline
    character (\n) at the end.

    Arguments:
    ==========
    file_path: str
        The location of a text file to read.

    Returns:
    ========
    list[str]
        A list that contains all stripped lines
        of the input text file.
    """
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip()
            lines.append(cleaned)
    return lines



def text_to_fasta(fasta_file):
    """
    This function takes an already imported fasta file separated
    in lines (use read_file_into_lines()) and returns a dictionary 
    with unique identifiers as keys and DNA strings as values.
    """
    fasta_dic = {}
    for line in fasta_file:
        if line.startswith('>'): # this is a better convention because sometimes we might have '>' in other lines as well
            key = line[1:]
            fasta_dic[key] = ""
        else:
            fasta_dic[key] += line # more concise way
    return fasta_dic


def reverse_complement(rna):
    # the reverse complement:
    revc = rna[::-1]
    revc = revc.replace('A', 'u')
    revc = revc.replace('U', 'a')
    revc = revc.replace('G', 'c')
    revc = revc.replace('C', 'g')
    revc = revc.upper()
    return revc


def gc_content_count(fasta_dic):
    """
    This function calculates the GC contents of various DNA strings. 
    Takes a dictionary formatted as {"ID" : "DnaString"} and returns
    another dictionary with percentages for each "ID".
    """
    percentages = {}
    for key in fasta_dic.keys():
        value = fasta_dic[key]
        percent = ((value.count('C') + value.count('G'))/len(value))
        percentages[key] = percent * 100
    return percentages


def read_fasta(fasta_file):
    lines = read_file_into_lines(fasta_file)
    fasta = text_to_fasta(lines)
    return fasta
    
# This dictionary might be useful in the future. 
codon_dict = {
'UUU': "F",      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
'UUC': "F",      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
'UUA': "L",      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
'UUG': "L",      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
'UCU': "S",      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': "S",      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': "S",      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': "S",      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': "Y",      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': "Y",      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': "None",   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': "None",   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': "C",      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': "C",      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'UGA': "None",   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': "W",      'CGG': 'R',      'AGG': 'R',      'GGG': 'G'}