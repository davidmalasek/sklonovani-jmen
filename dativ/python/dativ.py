# Komu, čemu?

def dativ(input_jmena):
    output = []
    if " " in input_jmena:
        jmena = input_jmena.split(" ")
    else:
        jmena = [input_jmena]

    for jmeno in jmena:
        if jmeno[-1] == "y" or jmeno[-1] == "í" or jmeno[-1] == "é":
            if jmeno[-2] == "l":  # Emily
                output.append(jmeno)
            else: # Harry, Jiří, René
                output.append(jmeno + "mu")
        elif jmeno[-1] == "l":
            if jmeno[-2] == "e":  
                if jmeno[-3] == "c" or jmeno[-3] == "u" or jmeno[-3] == "i": # Marcel, Samuel, Gabriel
                    output.append(jmeno + "ovi")
                else: # Karel
                    output.append(jmeno[0:-2] + "lovi")
            elif jmeno[-2] == "a" or jmeno[-2] == "i" or jmeno[-2] == "á" or jmeno[-2] == "o":  # Michal, Bohumil, Král, Anatol
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "k":
            if jmeno[-2] == "e": # Malášek
                output.append(jmeno[0:-2] + "kovi")
            elif jmeno[-2] == "ě": 
                if jmeno[-3] == "n": # Zbyněk
                    output.append(jmeno[0:-3] + "ňkovi")
                elif jmeno[-3] == "d": # Luděk
                    output.append(jmeno[0:-3] + "ďkovi")
                elif jmeno[-3] == "n": # Vaněk
                    output.append(jmeno[0:-3] + "ňkovi")
            else: # Novák
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "h" or jmeno[-1] == "i":  # Sarah, Niki
            if jmeno[-2] == "c": # Bedřich, Vojtěch
                output.append(jmeno + "ovi")
            else:
                output.append(jmeno)
        elif jmeno[-1] == "a":
            if jmeno[-2] == "k":  # Eliška
                if jmeno[-3] == "z" or jmeno[-3] == "r" and jmeno[-4] == "i"  or jmeno[-3] == "č": # Procházka, Jirka, Růžička
                    output.append(jmeno[0:-1] + "ovi")
                else:
                    output.append(jmeno[0:-2] + "ce")
            elif jmeno[-2] == "z":  # Honza
                if jmeno[-3] == "e":  # Tereza
                    output.append(jmeno[0:-1] + "e")
                else:
                    output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "v":  # Eva
                output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "l":  # Pavla
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "ď" or jmeno[-2] == "l":  # Láďa, Fiala
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "č" or jmeno[-2] == "j" or jmeno[-2] == "l":  # Ivča, Kája, Nikola
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "d" and jmeno[-3] == "o" or jmeno[-2] == "r" and jmeno[-3] == "e":  # Svoboda, Kučera
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "r":  # Klára
                if jmeno[-3] == "í": 
                    if jmeno[-5] == "o": # Drahomíra
                        output.append(jmeno[0:-2] + "ře")
                    else: # Míra
                        output.append(jmeno[0:-1] + "ovi")
                elif jmeno[-3] == "d": # Jindra
                    output.append(jmeno[0:-1] + "ovi")
                else:
                    output.append(jmeno[0:-2] + "ře")
            elif jmeno[-2] == "i":  # Olivia
                output.append(jmeno[0:-1] + "i")
                output.append(jmeno[0:-1] + "i")
            elif jmeno[-2] == "o":  # Olivia
                output.append(jmeno)
            elif jmeno[-2] == "t":
                if jmeno[-3] == "n": # Franta
                    output.append(jmeno[0:-1] + "ovi")
                else: # Agáta
                    output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "n" or jmeno[-2] == "d":  # Anna, Linda
                output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "ň":  # Soňa
                output.append(jmeno[0:-2] + "ně")
            elif jmeno[-3] == "c" or jmeno[-2] == "h": # Průcha
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "š" or jmeno[-2] == "e": # Nataša, Andrea, Lea
                output.append(jmeno[0:-1] + "e")
            else:
                output.append(jmeno)
        elif jmeno[-1] == "á":
            output.append(jmeno[0:-1] + "é")
        elif jmeno[-1] == "ý":
            output.append(jmeno[0:-1] + "ému")
        elif jmeno[-1] == "r":
            if jmeno[-2] == "a": # Dagmar
                if jmeno[-3] == "k": # Otakar
                    output.append(jmeno + "ovi")
                else:
                    output.append(jmeno)
            else:
                output.append(jmeno+ "ovi")
        elif jmeno[-1] == "e":
            if jmeno[-2] == "g": # George
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "e": # Lee
                output.append(jmeno)
            else:
                output.append(jmeno[0:-1] + "i")
        elif jmeno[-1] == "o": # Ronaldo, Santiago
            output.append(jmeno + "vi")
        elif jmeno[-1] == "ů": # Petrů
            output.append(jmeno)
        else:
            output.append(jmeno + "ovi")
    return " ".join(output)