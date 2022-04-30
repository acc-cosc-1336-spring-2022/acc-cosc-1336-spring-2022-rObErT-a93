def get_hamming_distance(dna1, dna2):
    list_dna1 = list(dna1)
    list_dna2 = list(dna2)
    counter = 0

    for i in range(16):
        if list_dna1[i] != list_dna2[i]:
            counter += 1
    return counter

def get_dna_complement(dna):
    reverse = reverse_string(dna)
    new_string = list(reverse)
    for i in range(10):
        if new_string[i] == "T":
            new_string[i] = "A"
        elif new_string[i] == "A":
            new_string[i] = "T"
        elif new_string[i] == "G":
            new_string[i] = "C"
        elif new_string[i] == "C":
            new_string[i] = "G"
            i += 1

    new_string1 = list_to_string(new_string)
    return new_string1

def reverse_string(string):
    rstr1 = ""
    indx = len(string)
    while indx > 0:
        rstr1 += string[ indx -1 ]
        indx = indx - 1
    return rstr1

def list_to_string(s):
    str1 = ""
    for ltr in s:
        str1 += ltr
    return str1