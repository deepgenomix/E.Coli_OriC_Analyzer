"This program checks where the OriC of E.Coli gene is AT rich or GC rich"
 
dna_oric = input("Enter the DNA sequence of OriC:")
if len(dna_oric) == 0:
    print("Error: DNA sequence cannot be empty.")
    exit()
#takes inpur from the user
DNA_oric = dna_oric.upper()
#coverts into uppercase
for base in DNA_oric:
    if base not in 'ATGC':
        print("Error: Invalid character in DNA sequence. Please enter a valid DNA sequence containing only A, T, G, and C.")
        exit()
        #checks whether the input dna sequence is valid or not
A = DNA_oric.count('A')
T = DNA_oric.count('T')
G = DNA_oric.count('G')
C = DNA_oric.count('C')
#counts the no. of ATGC in the dna seq.
AT_percent = ((A+T)/(len(DNA_oric)))* 100.0
GC_percent = ((G+C)/(len(DNA_oric)))* 100.0
# calculates the percent of AT and GC content
print("The sequence length is:", len(DNA_oric),"bp")
#prints the length of the base pair of given dna sequence
print(f"The AT content in percent is:{AT_percent:.2f}%")
print(f"The GC content in percent is:{GC_percent:.2f}%")
#prints the percent of the AT and GC content
if AT_percent > GC_percent:
    print("The OriC of E.Coli is AT rich, which is essential for the initiation of DNA replication by melting the DNA strands")
elif GC_percent > AT_percent:
    print("The OriC of E.Coli is GC rich, which is not ideal for the initiation of DNA replication")
elif GC_percent == AT_percent and AT_percent!=0.00 and GC_percent!=0.00:
    print("The OriC of E.Coli has equal amount of AT and GC content")
elif AT_percent==0.00 and GC_percent==0.00:
    print("Invalid dna sequence")
#checks whether the OriC of E.Coli is AT rich or GC rich or has equal amount of both
""" This checks the presence of cosensus sequence 5' - TTATCCACA - 3' in the given dna sequence"""
if 'TTATCCACA' in DNA_oric:
    print("The consensus sequence 5' - TTATCCACA - 3' is present in the given dna sequence")
    
else:
    print("The consensus sequence 5' - TTATCCACA - 3' is not present in the given dna sequence")


