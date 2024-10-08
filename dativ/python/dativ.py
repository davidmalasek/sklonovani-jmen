# Komu, čemu?


def dativ(input_jmena):
    output = []
    if " " in input_jmena:
        jmena = input_jmena.split(" ")
    else:
        jmena = [input_jmena]

    for jmeno in jmena:
        if jmeno[-1] == "a":
            if jmeno[-2] == "d" or jmeno[-2] == "n":  # Anna, Linda
                if (
                    jmeno[-3] == "o"
                    and jmeno[-4] == "b"
                    or jmeno[-3] == "i"
                    and jmeno[-4] == "l"
                    or jmeno[-3] == "a"
                    and jmeno[-4] == "t"
                ):  # Svoboda, Kalina, Smetana
                    output.append(jmeno[0:-1] + "ovi")
                else:
                    output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "ď" or (
                jmeno[-2] == "l" and jmeno[-3] == "a"
            ):  # Láďa, Fiala
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "g":  # Olga
                output.append(jmeno[0:-2] + "ze")
            elif jmeno[-2] == "i":  # Olivia
                output.append(jmeno[0:-1] + "i")
            elif jmeno[-2] == "k":  # Eliška
                if (
                    jmeno[-3] == "z"
                    or jmeno[-3] == "r"
                    and jmeno[-4] == "k"
                    or jmeno[-3] == "č"
                    or jmeno[-3] == "j"
                    or jmeno[-3] == "b"
                    or jmeno[-3] == "p"
                ):  # Procházka, Jirka, Růžička, Matějka, Rybka
                    output.append(jmeno[0:-1] + "ovi")
                else:
                    output.append(jmeno[0:-2] + "ce")
            elif jmeno[-2] == "l" and jmeno[-3] == "v":  # Pavla
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "ň":  # Soňa
                output.append(jmeno[0:-2] + "ně")
            elif jmeno[-2] == "o":  # Figueroa
                output.append(jmeno)
            elif jmeno[-2] == "r":  # Klára
                if jmeno[-3] == "í":
                    if jmeno[-5] == "o":  # Drahomíra
                        output.append(jmeno[0:-2] + "ře")
                    else:  # Míra
                        output.append(jmeno[0:-1] + "ovi")
                elif jmeno[-3] == "d" or jmeno[-3] == "e":  # Jindra, Kučera
                    output.append(jmeno[0:-1] + "ovi")
                else:
                    output.append(jmeno[0:-2] + "ře")
            elif jmeno[-2] == "t":
                if jmeno[-3] == "n" or jmeno[-3] == "j":  # Franta, Vojta
                    output.append(jmeno[0:-1] + "ovi")
                else:  # Agáta
                    output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "v":  # Eva
                output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "z":  # Honza
                if jmeno[-3] == "e":  # Tereza
                    output.append(jmeno[0:-1] + "e")
                else:
                    output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-3] == "c" or jmeno[-2] == "h":  # Průcha
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] in ["e", "š"]:  # Nataša, Andrea, Lea
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] in ["č", "j", "l"]:  # Ivča, Kája, Nikola
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-3] == "o":  #  Kučera
                output.append(jmeno[0:-1] + "ovi")
            else:
                output.append(jmeno)
        elif jmeno[-1] == "á":
            output.append(jmeno[0:-1] + "é")
        elif jmeno[-1] == "e":
            if jmeno[-2] == "g":  # George
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "e":  # Lee
                output.append(jmeno)
            else:
                output.append(jmeno[0:-1] + "i")
        elif jmeno[-1] == "h" or jmeno[-1] == "i":
            if jmeno[-2] == "c":  # Bedřich, Vojtěch
                output.append(jmeno + "ovi")
            else:  # Sarah, Niki
                output.append(jmeno)
        elif jmeno[-1] == "k":
            if jmeno[-2] == "e":  # Malášek
                output.append(jmeno[0:-2] + "kovi")
            elif jmeno[-2] == "ě":
                if jmeno[-3] == "n":  # Zbyněk
                    output.append(jmeno[0:-3] + "ňkovi")
                elif jmeno[-3] == "d":  # Luděk
                    output.append(jmeno[0:-3] + "ďkovi")
                elif jmeno[-3] == "n":  # Vaněk
                    output.append(jmeno[0:-3] + "ňkovi")
            else:  # Novák
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "l":
            if jmeno[-2] == "e":
                if jmeno[-3] in ["c", "i", "u"]:  # Marcel, Samuel, Gabriel
                    output.append(jmeno + "ovi")
                else:  # Karel
                    output.append(jmeno[0:-2] + "lovi")
            elif jmeno[-2] in ["a", "i", "o"]:  # Michal, Bohumil, Anatol
                output.append(jmeno + "ovi")
            else:  # Král
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "o":  # Ronaldo, Santiago
            output.append(jmeno + "vi")
        elif jmeno[-1] == "r":
            if jmeno[-2] == "a":  # Dagmar
                if jmeno[-3] == "k":  # Otakar
                    output.append(jmeno + "ovi")
                else:
                    output.append(jmeno)
            else:
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "y" or jmeno[-1] == "í" or jmeno[-1] == "é":
            if jmeno[-2] == "l":  # Emily
                output.append(jmeno)
            else:  # Harry, Jiří, René
                output.append(jmeno + "mu")
        elif jmeno[-1] == "ý":
            output.append(jmeno[0:-1] + "ému")
        elif jmeno[-1] == "ů":  # Petrů
            output.append(jmeno)
        else:
            output.append(jmeno + "ovi")
    return " ".join(output)
