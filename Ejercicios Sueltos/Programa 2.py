from string import *
def gc(seq):
    nbases = seq.count("N")
    gcpercent = float (seq.count("G") + seq.count("C"))/ (len(seq) - nbases)
    return gcpercent * 100
#seq = "ATGACGATAGGAGANNTATAGAN"
seq = input("Introducir sequencia ")

print ("La secuencia es " + seq)
print ("%GC = " + str(gc(seq)))
input ("Presione enter para terminar")