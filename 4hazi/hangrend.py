def hangrendje(s):
    mely = {'a', 'á', 'o', 'ó', 'u', 'ú'}
    magas = {'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'}
    voltMely = False
    voltMagas = False
    for e in s:
        if e in mely:
            voltMely = True
        if e in magas:
            voltMagas = True
    if (voltMagas and voltMely):
        return "vegyes"
    if (not(voltMely) and not(voltMagas)):
        return "semmilyen"
    if (voltMagas and not(voltMely)):
        return "magas"
    else:
        return "mely"



def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély"]
    #print(hangrendje("kacsa"))
    for word in words:
        print(hangrendje(word))


if __name__ == "__main__":
    main()