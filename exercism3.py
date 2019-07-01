#RNA transcription
#https://exercism.io/my/solutions/cee92938549d43bba671e397c14ad0d0

'''Given a DNA strand, return its RNA complement.

DNA -> RNA
G -> C
C -> G
T -> A
A -> U'''

#assume arrays

def transcription(strand):
    complement = [] #instantiate empty list
    for nucleotide in strand:
        if nucleotide == 'G':
            complement.append('C')
        elif nucleotide == 'C':
            complement.append('G')
        elif nucleotide == 'T':
            complement.append('A')
        elif nucleotide == 'A':
            complement.append('U')
        else:
            raise KeyError('huh that does not look like a DNA nucleotide to me')
    return complement

if __name__ == '__main__':
    print(transcription(['A','A','A']))
    print(transcription(['G','C','T','A']))