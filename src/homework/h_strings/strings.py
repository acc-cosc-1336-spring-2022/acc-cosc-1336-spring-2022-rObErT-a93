def get_hamming_distance(dna1, dna2):
    list_dna1 = list(dna1)
    list_dna2 = list(dna2)
    counter = 0

    for i in range(17):
        if list_dna1[i] != list_dna2[i]:
            counter += 1
    return counter

def reverse_string(string):
    rstr1 = ""
    indx = len(string)
    while indx > 0:
        rstr1 += string[ indx -1 ]
        indx = indx - 1
    return rstr1

def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

def get_dna_complement(dna):
    reverse = reverse_string(dna)
    new_reverse = list(reverse)
    for i in range(10):
        if new_reverse[i] == "T":
            new_reverse[i] = "A"
        elif new_reverse[i] == "A":
            new_reverse[i] = "T"
        elif new_reverse[i] == "G":
            new_reverse[i] = "C"
        elif new_reverse[i] == "C":
            new_reverse[i] = "G"
            i += 1

    new_reverse1 = list_to_string(new_reverse)
    return new_reverse1