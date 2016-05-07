import sys
import math
import time

def is_dna(dnaString):
    for ch in dnaString:
        if ch not in complements:
            return False
    return True

def length_dna(dnaString):
    if is_dna(dnaString):
        return len(dnaString)
    return 'Not a valid sequence'

def complementary(dnaString):
    complementDna = ''
    for ch in dnaString:
        complementDna += complements[ch]
    return complementDna

def transcription(dnaString):
    transriptDna = ''
    #comp = complementary(dnaString)
    for ch in dnaString:
        transriptDna += transcriptions[ch]
    return transriptDna

def translation(dnaString):
    if is_dna(dnaString):
        translation = ''
        trans = transcription(dnaString)
        for i in range(0,len(trans),3):
            str = codonTable[trans[i:i+3]]
            if len(str) == 1:
                translation += str
        return translation
    return 'Not a valid sequence'

def getMass(dnaString):
    if is_dna(dnaString):
        trans = transcription(dnaString)
        sum = 0
        for i in range(0,len(trans),3):
            str = codonTable[trans[i:i+3]]
            if len(str) == 1:
                sum += massTable[str]
        return sum
    return 'Not a valid sequence'

def getProteins(translation):
    proteins = []
    for ch in translation:
        proteins.append(aminoCodes[ch])
    return proteins

complements = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
transcriptions = {'A':'U', 'G':'C', 'C':'G', 'T':'A'}

massTable = {
'A':   71.03711,
'C':   103.00919,
'D':   115.02694,
'E':   129.04259,
'F':   147.06841,
'G':   57.02146,
'H':   137.05891,
'I':   113.08406,
'K':   128.09496,
'L':   113.08406,
'M':   131.04049,
'N':   114.04293,
'P':   97.05276,
'Q':   128.05858,
'R':   156.10111,
'S':   87.03203,
'T':   101.04768,
'V':   99.06841,
'W':   186.07931,
'Y':   163.06333 
}

codonTable = {
'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G', 
}

aminoCodes = {
'A' : 'Alanine',
'G' : 'Glycine',
'M' : 'Methionine', 
'S' : 'Serine',
'C' : 'Cysteine', 
'H' : 'Hisitidine', 
'N' : 'Asparagine',
'T' : 'Threonine',
'D' : 'Aspartic Acid', 
'I' : 'Isoleucine', 
'P' : 'Proline', 
'V' : 'Valine',
'E' : 'Glutamic acid', 
'K' : 'Lysine', 
'Q' : 'Glutamine', 
'W' : 'Tryptophan',
'F' : 'Phenylalanine', 
'L' : 'Leucine', 
'R' : 'Arginine', 
'Y' : 'Tyrosine',
}

testString = ''
with open('TestData.txt') as f:
    for line in f.readlines():
        testString += line
testString = testString.replace('\n', '')

#print('1. Is Dna - ', is_dna(testString))
#print('2. Length - ', length_dna(testString))
#print('3. Complementary - ', complementary(testString))
#print('4. Transription - ', transcription(testString))
#trans = translation(testString)
#print('5. Translation - ', trans)
print('7. Mass - ', getMass(testString))
#print('8. Proteins - ', getProteins(trans))