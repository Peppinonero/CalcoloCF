import re

def calc_cognome(cognome):
    cons = [x for x in cognome if x not in vocali]
    voc = [x for x in cognome if x in vocali]
    cod_cognome = "".join(cons + voc + ['x'] * 2)[:3].upper()
    return cod_cognome

def calc_nome(nome):
    cons = [x for x in nome if x not in vocali]
    voc = [x for x in nome if x in vocali]
    if len(cons) > 3:
        cons = cons[:1] + cons[2:]
    cod_nome = "".join(cons + voc + ['x'] * 2)[:3].upper()
    return cod_nome

def data(data_nascita, sesso):
    anno = data_nascita[2][2:]
    mese = mesi[data_nascita[1]]
    giorno = str(int(data_nascita[0]) + 40) if sesso != "M" else data_nascita[0]
    return anno + mese + giorno

def calc_cod_comune(comune):
    codice_comune = ""
    with open("codici_catastali.txt", "r") as codici:
        for linea in codici:
            parentesi_inizio = linea.find("(")
            if parentesi_inizio != -1:
                codice = linea[:parentesi_inizio].strip().split(" ")[0]
                com = linea[:parentesi_inizio].strip().split(" ")[1]
                if com.upper() == comune.upper():
                    codice_comune = codice
                    break
    return codice_comune

def codice_controllo(cod_fisc):
    somma = 0
    for i, carattere in enumerate(cod_fisc):
        if i % 2 == 0:  
            somma += dispari[carattere]
        else:  
            somma += pari[carattere]
    resto = somma % 26
    return controllo[resto] 

cognome = input("Inserire il cognome: ")
nome = input("Inserire il nome: ")
sesso = input("inserire sesso (F o M): ")
data_nascita = input("inserire data di nascita (gg/mm/anno): ").split('/')
comune = input("inserire comune di nascita: ")

vocali = "aeiouAEIOU"

mesi = {'01': 'A', '02': 'B', '03': 'C', '04': 'D',
        '05': 'E', '06': 'H', '07': 'L', '08': 'M',
        '09': 'P', '10': 'R', '11': 'S', '12': 'T'}

controllo = {i: chr(65 + i) for i in range(26)}
controllo[14] = 'P'

dispari = {'0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13,
           '6': 15, '7': 17, '8': 19, '9': 21, 'A': 1, 'B': 0,
           'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17,
           'I': 19, 'J': 21, 'K': 2, 'L': 4, 'M': 18, 'N': 20,
           'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
           'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23}

pari = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 0, 'B': 1,
        'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
        'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
        'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

cod_fisc = calc_cognome(cognome) + calc_nome(nome) + data(data_nascita, sesso) + calc_cod_comune(comune)
print(cod_fisc + codice_controllo(cod_fisc))
