# Koho, čeho?


def genitiv(input_jmena):
    output = []
    if " " in input_jmena:
        jmena = input_jmena.split(" ")
    else:
        jmena = [input_jmena]

    for jmeno in jmena:
        if jmeno[-1] == "a":
            if jmeno[-2] in ["d", "n"]:  # Anna, Linda
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] in ["č", "j"]:  # Ivča, Kája
                output.append(jmeno[0:-1] + "i")
            elif jmeno[-2] == "ď":  # Láďa
                output.append(jmeno[0:-1] + "i")
            elif jmeno[-2] == "g":  # Olga
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "i":  # Olivia
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "k":  # Eliška
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "l" and jmeno[-3] == "v":  # Pavla
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "l":  # Fiala, Nikola
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "o":  # Figueroa
                output.append(jmeno)
            elif jmeno[-2] == "r":  # Klára, Svoboda, Kučera
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "t":  # Alžběta
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "v":  # Eva
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "z":  # Honza, Tereza
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] == "ň":  # Soňa
                output.append(jmeno[0:-2] + "ni")
            elif jmeno[-3] == "c" or jmeno[-2] == "h":  # Průcha
                output.append(jmeno[0:-1] + "y")
            elif jmeno[-2] in ["e", "š"]:  # Nataša, Andrea, Lea
                if jmeno[-3] == "r":
                    output.append(jmeno[0:-1] + "ji")
                else:
                    output.append(jmeno[0:-1] + "i")
            else:
                output.append(jmeno[0:-1] + "y")
        elif jmeno[-1] == "á":
            output.append(jmeno[0:-1] + "é")
        elif jmeno[-1] == "e":
            if jmeno[-2] == "g":  # George
                output.append(jmeno)
            elif jmeno[-2] == "e":  # Lee
                output.append(jmeno)
            elif jmeno[-2] == "i":  # Lucie
                output.append(jmeno)
            else:
                output.append(jmeno[0:-1] + "i")
        elif jmeno[-1] == "h" or jmeno[-1] == "i":
            if jmeno[-2] == "c":  # Bedřich, Vojtěch
                output.append(jmeno + "a")
            else:  # Sarah, Niki
                output.append(jmeno)
        elif jmeno[-1] == "k":
            if jmeno[-2] == "e":  # Malášek
                output.append(jmeno[0:-2] + "ka")
            elif jmeno[-2] == "ě":
                if jmeno[-3] == "n":  # Zbyněk
                    output.append(jmeno[0:-3] + "ňka")
                elif jmeno[-3] == "d":  # Luděk
                    output.append(jmeno[0:-3] + "ďka")
                elif jmeno[-3] == "n":  # Vaněk
                    output.append(jmeno[0:-3] + "ňka")
            else:  # Novák
                output.append(jmeno + "a")
        elif jmeno[-1] == "l":
            if jmeno[-2] == "e":
                if jmeno[-3] in ["c", "i", "u"]:  # Marcel, Samuel, Gabriel
                    output.append(jmeno + "a")
                else:  # Karel
                    output.append(jmeno[0:-2] + "la")
            elif jmeno[-2] in ["a", "i", "o"]:  # Michal, Bohumil, Anatol
                output.append(jmeno + "a")
            else:  # Král
                output.append(jmeno + "e")
        elif jmeno[-1] == "m":  # Maxim
            output.append(jmeno + "a")
        elif jmeno[-1] == "o":  # Ronaldo, Santiago
            output.append(jmeno[0:-1] + "a")
        elif jmeno[-1] == "r":
            if jmeno[-2] == "a":
                if jmeno[-3] == "k":  # Otakar
                    output.append(jmeno + "a")
                else:  # Dagmar
                    output.append(jmeno)
            else:
                output.append(jmeno + "a")
        elif jmeno[-1] == "y" or jmeno[-1] == "í" or jmeno[-1] == "é":
            if jmeno[-2] == "l":  # Emily
                output.append(jmeno)
            else:  # Harry, Jiří, René
                output.append(jmeno + "ho")
        elif jmeno[-1] == "ý":
            output.append(jmeno[0:-1] + "ého")
        elif jmeno[-1] == "ů":  # Petrů
            output.append(jmeno)
        elif jmeno[-1] in ["c", "j", "ř", "š"]:  # Tomáš, Ondřej, Kadlec
            output.append(jmeno + "e")
        elif jmeno[-1] == "x" or jmeno[-1] == "s":  # Max, Nikolas
            output.append(jmeno + "e")
        else:
            output.append(jmeno + "a")
    return " ".join(output)
