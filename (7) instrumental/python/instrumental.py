# S kým, s čím?


def instrumental(input_jmena):
    output = []
    if " " in input_jmena:
        jmena = input_jmena.split(" ")
    else:
        jmena = [input_jmena.lower()]

    for jmeno in jmena:
        jmeno = jmeno.lower()
        if jmeno[-1] == "a":
            if jmeno[-2] == "i":  # Olivia
                output.append(jmeno[0:-1] + "í")
            elif jmeno[-2] == "o":  # Figueroa
                output.append(jmeno)
            else:
                output.append(jmeno[0:-1] + "ou")
        elif jmeno[-1] == "c":  # Kadlec
            if jmeno[-2] == "e" and (
                jmeno[-3] == "n" or jmeno[-3] == "m"
            ):  # Vavřinec, Adamec
                output.append(jmeno[0:-2] + "cem")
            else:
                output.append(jmeno + "em")
        elif jmeno[-1] == "á":
            output.append(jmeno[0:-1] + "ou")
        elif jmeno[-1] == "š":  # Tomáš
            output.append(jmeno + "em")
        elif jmeno[-1] == "e":
            if jmeno[-2] == "g":  # George
                output.append(jmeno[0:-1] + "m")
            elif (
                jmeno[-2] == "c" or jmeno[-2] == "i" or jmeno[-2] == "š"
            ):  # Alice, Amálie, Miluše
                output.append(jmeno[0:-1] + "í")
            else:
                output.append(jmeno)
        elif jmeno[-1] == "h" or jmeno[-1] == "i":
            if jmeno[-2] == "c":  # Bedřich, Vojtěch
                output.append(jmeno + "em")
            else:  # Sarah, Niki
                output.append(jmeno)
        elif (
            jmeno[-1] == "j"
            or (jmeno[-1] == "m" and jmeno[-2] != "a")
            or jmeno[-1] == "f"
            or jmeno[-1] == "n"
            or (jmeno[-1] == "t" and jmeno[-2] != "ů")
            or jmeno[-1] == "p"
            or jmeno[-1] == "b"
            or jmeno[-1] == "g"
            or jmeno[-1] == "v"
        ):
            output.append(jmeno + "em")
        elif jmeno[-1] == "m" and jmeno[-2] == "a":  # Miriam
            output.append(jmeno)
        elif jmeno[-1] == "k":
            if jmeno[-2] == "e":  # Malášek
                output.append(jmeno[0:-2] + "kem")
            elif jmeno[-2] == "ě":
                if jmeno[-3] == "n":  # Zbyněk
                    output.append(jmeno[0:-3] + "ňkem")
                elif jmeno[-3] == "d":  # Luděk
                    output.append(jmeno[0:-3] + "ďkem")
                elif jmeno[-3] == "n":  # Vaněk
                    output.append(jmeno[0:-3] + "ňkem")
            else:  # Novák
                output.append(jmeno + "em")
        elif jmeno[-1] == "l":
            if jmeno[-2] == "e":
                if jmeno[-3] in [
                    "c",
                    "i",
                    "u",
                    "a",
                ]:  # Marcel, Samuel, Gabriel, Michael
                    output.append(jmeno + "em")
                else:  # Karel
                    output.append(jmeno[0:-2] + "lem")
            elif jmeno[-2] == "o" and jmeno[-3] == "k":  # Nikol
                output.append(jmeno)
            else:  # Král, Michal, Bohumil, Anatol, Přemysl
                output.append(jmeno + "em")
        elif jmeno[-1] == "o":
            if jmeno[-2] == "t":  # Oto
                output.append(jmeno[0:-1] + "ou")
            else:  # Ronaldo, Santiago
                output.append(jmeno[0:-1] + "em")
        elif jmeno[-1] == "d":
            if (
                jmeno[-2] == "l"
                or jmeno[-2] == "r"
                or jmeno[-2] == "n"
                or (jmeno[-2] == "i" and jmeno[-3] == "v")
            ):  # Leopold, Richard, Roland, Strnad, David
                output.append(jmeno + "em")
            else:  # Ingrid
                output.append(jmeno)
        elif jmeno[-1] == "r":
            if (
                jmeno[-2] == "a"
                or jmeno[-2] == "e"
                or jmeno[-2] == "d"
                or jmeno[-2] == "u"
                or jmeno[-2] == "í"
                or jmeno[-2] == "o"
                or jmeno[-2] == "t"
            ):  # Dagmar, Ester, Alexandr, Artur, Bohumíř, Ctibor
                if (
                    jmeno[-3] == "k"
                    or jmeno[-3] == "v"
                    or (jmeno[-3] == "m" and jmeno[-4] != "g")
                    or jmeno[-3] == "n"
                    or (jmeno[-3] == "t" and jmeno[-4] != "s")
                    or jmeno[-3] == "p"
                    or jmeno[-3] == "l"
                    or jmeno[-3] == "g"
                    or jmeno[-3] == "b"
                    or jmeno[-3] == "d"
                    or jmeno[-3] == "e"
                ):  # Otakar, Oliver, Otmar, Peter, Kašpar, Müller, Langer, Lubor, Teodor
                    output.append(jmeno + "em")
                else:
                    output.append(jmeno)
            else:
                output.append(jmeno + "a")
        elif jmeno[-1] == "y" or jmeno[-1] == "í" or jmeno[-1] == "é":
            if jmeno[-2] == "l":  # Emily
                output.append(jmeno)
            else:  # Harry, Jiří, René
                output.append(jmeno + "m")
        elif jmeno[-1] == "ý":
            output.append(jmeno[0:-1] + "m")
        elif jmeno[-1] == "ř" or jmeno[-1] == "ž":  # Kovář, Ambrož
            output.append(jmeno + "em")
        elif jmeno[-1] == "ů":  # Petrů
            output.append(jmeno)
        elif jmeno[-1] == "z":  # Radůz
            output.append(jmeno + "em")
        elif jmeno[-1] == "t":  # Růt
            output.append(jmeno)
        elif jmeno[-1] == "s" or jmeno[-1] == "x":  # Nikolas, Max
            output.append(jmeno + "em")
        else:
            output.append(jmeno + "ou")
    output = [item.capitalize() for item in output]
    return " ".join(output)
