# Koho, co?


def akuzativ(input_jmena):
    output = []
    if " " in input_jmena:
        jmena = input_jmena.split(" ")
    else:
        jmena = [input_jmena.lower()]

    for jmeno in jmena:
        jmeno = jmeno.lower()
        if jmeno[-1] == "a":
            if jmeno[-2] == "d" or jmeno[-2] == "n":  # Anna, Linda
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "ď" or (
                jmeno[-2] == "l" and jmeno[-3] == "a"
            ):  # Láďa, Fiala
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "g" or jmeno[-2] == "s":  # Olga, Denisa
                output.append(jmeno[0:-1] + "u")
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
                    or jmeno[-3] == "i"
                ):  # Procházka, Jirka, Růžička, Matějka, Rybka, Veronika
                    output.append(jmeno[0:-1] + "u")
                else:
                    output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "l" and jmeno[-3] == "v":  # Pavla
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "ň":  # Soňa
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "o":  # Figueroa
                output.append(jmeno)
            elif (
                jmeno[-2] == "c" or jmeno[-2] == "m" or jmeno[-2] == "p"
            ):  # Danica, Ema, Chalupa
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "r":  # Klára
                if jmeno[-3] == "í":  # Míra, Drahomíra
                    output.append(jmeno[0:-1] + "u")
                elif (
                    jmeno[-3] == "d" or jmeno[-3] == "e" or jmeno[-3] == "o"
                ):  # Jindra, Kučera
                    output.append(jmeno[0:-1] + "u")
                else:
                    output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "t":
                if jmeno[-3] == "n":  # Franta
                    output.append(jmeno[0:-1] + "u")
                else:  # Agáta
                    output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "v":  # Eva
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] == "z":  # Honza
                if jmeno[-3] == "e":  # Tereza
                    output.append(jmeno[0:-1] + "u")
                else:
                    output.append(jmeno[0:-1] + "u")
            elif jmeno[-3] == "c" or jmeno[-2] == "h":  # Průcha
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] in ["e", "š"]:  # Nataša, Andrea, Lea
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-2] in ["č", "j", "l"]:  # Ivča, Kája, Nikola
                output.append(jmeno[0:-1] + "u")
            elif jmeno[-3] == "o":  #  Kučera
                output.append(jmeno[0:-1] + "u")
            else:
                output.append(jmeno)
        elif jmeno[-1] == "c":  # Kadlec
            if jmeno[-2] == "e" and (
                jmeno[-3] == "n" or jmeno[-3] == "m"
            ):  # Vavřinec, Adamec
                output.append(jmeno[0:-2] + "ce")
            else:
                output.append(jmeno + "e")
        elif jmeno[-1] == "á":
            output.append(jmeno[0:-1] + "ou")
        elif jmeno[-1] == "š":  # Tomáš
            output.append(jmeno + "e")
        elif jmeno[-1] == "e":
            if jmeno[-2] == "g":  # George
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "e" or jmeno[-2] == "o":  # Zoe
                output.append(jmeno)
            else:
                output.append(jmeno[0:-1] + "i")
        elif jmeno[-1] == "h" or jmeno[-1] == "i":
            if jmeno[-2] == "c":  # Bedřich, Vojtěch
                output.append(jmeno + "a")
            else:  # Sarah, Niki
                output.append(jmeno)
        elif jmeno[-1] == "j":
            output.append(jmeno + "e")
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
                if jmeno[-3] in [
                    "c",
                    "i",
                    "u",
                    "a",
                ]:  # Marcel, Samuel, Gabriel, Michael
                    output.append(jmeno + "a")
                else:  # Karel
                    output.append(jmeno[0:-2] + "la")
            elif jmeno[-2] == "o" and jmeno[-3] == "k":  # Nikol
                output.append(jmeno)
            elif jmeno[-2] in ["a", "i", "o", "s"]:  # Michal, Bohumil, Anatol, Přemysl
                output.append(jmeno + "a")
            else:  # Král
                output.append(jmeno + "e")
        elif jmeno[-1] == "o":
            if jmeno[-2] == "t":  # Oto
                output.append(jmeno[0:-1] + "u")
            else:  # Ronaldo, Santiago
                output.append(jmeno[0:-1] + "a")
        elif jmeno[-1] == "d":
            if (
                jmeno[-2] == "l"
                or jmeno[-2] == "r"
                or jmeno[-2] == "n"
                or jmeno[-2] == "d"
            ):  # Leopold, Richard, Roland, Strnad
                output.append(jmeno + "a")
            else:  # Ingrid
                output.append(jmeno)
        elif jmeno[-1] == "r":
            if jmeno[-2] == "a" or jmeno[-2] == "e":  # Dagmar, Ester
                if (
                    jmeno[-3] == "k"
                    or jmeno[-3] == "v"
                    or jmeno[-3] == "m"
                    or jmeno[-3] == "t"
                    or jmeno[-3] == "p"
                    or jmeno[-3] == "l"
                    or jmeno[-3] == "g"
                ):  # Otakar, Oliver, Otmar, Peter, Kašpar, Müller, Langer
                    output.append(jmeno + "a")
                else:
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
        elif jmeno[-1] == "ř" or jmeno[-1] == "ž":  # Kovář, Ambrož
            output.append(jmeno + "e")
        elif jmeno[-1] == "ů":  # Petrů
            output.append(jmeno)
        elif jmeno[-1] == "z":  # Radůz
            output.append(jmeno + "e")
        elif jmeno[-1] == "t":  # Růt
            output.append(jmeno)
        elif jmeno[-1] == "s" or jmeno[-1] == "x":  # Nikolas, Max
            if jmeno[-2] == "e":  # Pes
                output.append(jmeno[0:-2] + "sa")
            else:
                output.append(jmeno + "e")
        else:
            output.append(jmeno + "a")
    output = [item.capitalize() for item in output]
    return " ".join(output)
