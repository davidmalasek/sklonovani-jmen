# O kom, o čem?


def lokativ(input_jmena):
    output = []
    if " " in input_jmena:
        jmena = input_jmena.split(" ")
    else:
        jmena = [input_jmena.lower()]

    for jmeno in jmena:
        jmeno = jmeno.lower()
        if jmeno[-1] == "a":
            if jmeno[-2] in ["d", "n"]:
                if jmeno[-3] == "o":  # Svoboda
                    output.append(jmeno[0:-1] + "ovi")
                else:  # Anna, Linda
                    output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] in ["č", "j", "c"]:  # Ivča, Kája, Danica
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "ď":
                if jmeno[-3] == "a":  # Naďa
                    output.append(jmeno[0:-2] + "dě")
                else:  # Láďa
                    output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "g":  # Olga
                output.append(jmeno[0:-2] + "ze")
            elif jmeno[-2] == "i":  # Olivia
                output.append(jmeno[0:-1] + "i")
            elif jmeno[-2] == "m":  # Ema
                output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "k":
                if (
                    jmeno[-3] == "z"
                    or jmeno[-3] == "č"
                    or jmeno[-3] == "n"
                    or jmeno[-3] == "j"
                ):  # Procházka, Růžička, Červenka, Matějka
                    output.append(jmeno[0:-2] + "kovi")
                else:  # Eliška
                    output.append(jmeno[0:-2] + "ce")
            elif jmeno[-2] == "l" and jmeno[-3] == "v":  # Pavla
                output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "l":  # Fiala, Nikola
                if jmeno[-3] == "a":
                    output.append(jmeno[0:-1] + "ovi")
                else:
                    output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "o":  # Figueroa
                output.append(jmeno)
            elif jmeno[-2] == "r":
                if (
                    jmeno[-3] == "e" or jmeno[-3] == "d" or jmeno[-3] == "o"
                ):  # Kučera, Sýkora
                    output.append(jmeno[0:-1] + "ovi")
                else:  # Klára
                    output.append(jmeno[0:-2] + "ře")
            elif jmeno[-2] == "t":
                if (
                    jmeno[-3] == "j" or jmeno[-3] == "n" or jmeno[-3] == "r"
                ):  # Vojta, Valenta, Bárta
                    output.append(jmeno[0:-1] + "ovi")
                else:  # Alžběta
                    output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "v":  # Eva
                output.append(jmeno[0:-1] + "ě")
            elif jmeno[-2] == "z":
                if jmeno[-3] == "n":  # Honza
                    output.append(jmeno[0:-1] + "ovi")
                else:  # Tereza
                    output.append(jmeno[0:-1] + "e")
            elif jmeno[-2] == "ň":  # Soňa
                output.append(jmeno[0:-2] + "ně")
            elif jmeno[-3] == "c" or jmeno[-2] == "h":  # Průcha
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] in ["e", "š"]:  # Nataša, Andrea, Lea
                output.append(jmeno[0:-1] + "e")
            else:
                output.append(jmeno[0:-1] + "e")
        elif jmeno[-1] == "á":
            output.append(jmeno[0:-1] + "é")
        elif jmeno[-1] == "e":
            if jmeno[-2] == "g":  # George
                output.append(jmeno[0:-1] + "ovi")
            elif jmeno[-2] == "e" or jmeno[-2] == "o":  # Lee, Zoe
                output.append(jmeno)
            elif (
                jmeno[-2] == "i" or jmeno[-2] == "c" or jmeno[-2] == "š"
            ):  # Lucie, Alice, Danuše
                output.append(jmeno[0:-1] + "i")
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
                if jmeno[-3] in ["c", "i", "u", "a"]:  # Marcel, Samuel, Gabriel
                    output.append(jmeno + "ovi")
                else:  # Karel
                    output.append(jmeno[0:-2] + "lovi")
            elif jmeno[-2] == "o" and jmeno[-3] == "k":  # Nikol
                output.append(jmeno)
            elif jmeno[-2] in ["a", "i", "o", "s"]:  # Michal, Bohumil, Anatol, Přemysl
                output.append(jmeno + "ovi")
            else:  # Král
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "m":
            if jmeno[-2] == "a":
                if jmeno[-3] == "d":  # Adam
                    output.append(jmeno + "ovi")
                else:  # Miriam
                    output.append(jmeno)
            else:  # Maxim
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "o":
            if jmeno[-2] == "t":  # Oto
                output.append(jmeno + "vi")
            else:  # Ronaldo, Santiago
                output.append(jmeno + "vi")
        elif jmeno[-1] == "r":
            if jmeno[-2] == "a" or jmeno[-2] == "e":  # Dagmar, Ester
                if (
                    jmeno[-3] == "k"
                    or jmeno[-3] == "m"
                    and (jmeno[-4] == "t" or jmeno[-4] == "e")
                    or jmeno[-3] == "p"
                    or jmeno[-3] == "l"
                    or jmeno[-3] == "v"
                    or jmeno[-3] == "t"
                ):  # Otakar, Otmar, Kašpar, Oliver, Peter
                    output.append(jmeno + "ovi")
                else:
                    output.append(jmeno)
            else:
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "y" or jmeno[-1] == "í" or jmeno[-1] == "é":
            if jmeno[-2] == "l":  # Emily
                output.append(jmeno)
            else:  # Harry, Jiří, René
                output.append(jmeno + "m")
        elif jmeno[-1] == "ý":
            output.append(jmeno[0:-1] + "ém")
        elif jmeno[-1] == "d":
            if jmeno[-2] == "i" and jmeno[-3] == "r":  # Ingrid
                output.append(jmeno)
            else:
                output.append(jmeno + "ovi")
        elif jmeno[-1] == "c":
            if jmeno[-2] == "n":  # Vincenc
                output.append(jmeno + "ovi")
            else:
                if jmeno[-2] == "l" or jmeno[-2] == "á":  # Šolc, Bonifác
                    output.append(jmeno + "ovi")
                else:  # Vavřinec
                    output.append(jmeno[0:-2] + "covi")
        elif jmeno[-1] == "ž":  # Ambrož
            output.append(jmeno + "ovi")
        elif jmeno[-1] == "t":
            if jmeno[-2] == "ů":  # Růt
                output.append(jmeno)
            else:  # Růt
                output.append(jmeno + "ovi")

        elif jmeno[-1] == "ů":  # Petrů
            output.append(jmeno)
        elif jmeno[-1] in ["c", "j", "ř", "š"]:  # Tomáš, Ondřej, Kadlec
            output.append(jmeno + "ovi")
        elif jmeno[-1] == "x" or jmeno[-1] == "s":  # Max, Nikolas
            output.append(jmeno + "ovi")
        else:
            output.append(jmeno + "ovi")
    output = [item.capitalize() for item in output]
    return " ".join(output)
