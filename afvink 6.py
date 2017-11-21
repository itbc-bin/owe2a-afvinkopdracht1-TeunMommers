def main():
    bestand = input("Welk bestand wilt u openen: ")
    zoek = input("Op welk woord wilt u zoeken: ")
    headers, seqs = lees_inhoud(bestand)
    x = 1
    for line in headers:
        try:
            if zoek in line:
                print(line)
                print(seqs[x])
                print("Dit is dna", is_dna(seqs[x]))
                print("Knipt", knipt(seqs[x]))
            x += 1
        except:
            print("Onbekend zoekwoord")
          
def lees_inhoud(bestands_naam):
    try: 
        bestand = open(bestands_naam, "r")
    except FileNotFoundError:
        print("Dit bestand is niet gevonden")
        main()

    headers = []
    seqs = []
    dna = ""
    for line in bestand:
        if ">" in line:
            headers.append(line.strip())
            dna += " "
        else:
            line = line.replace("\n","")
            dna += line
    seqs = dna.split(" ")
    return headers, seqs

def is_dna(seqs):
    ja_nee = True
    for i in seqs:
        if i != "A" and i != "C" and i != "G" and i != "T":
            ja_nee = False
    return ja_nee

def knipt(seq):
    bestand = open("enzymen.txt")
    bestand = bestand.readlines()
    enzymen = []
    for line in bestand:
        line = line.replace("\n","").replace("^","").split()
        enzymen.append(line)

    knippend = ""
    knip = False
    for regel in enzymen:
        if regel[1] in seq:
            knip = True
            knippend += regel[0]
            knippend += " "

            
    return knip, knippend
main()
