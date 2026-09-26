def iterativ(szoveg):
    i = 0
    j = len(szoveg) - 1
    while (i < len(szoveg) / 2):
        if (szoveg[i] != szoveg[j]):
            return False
        i += 1
        j -= 1
    return True

def rekurziv(szoveg, kezd, veg):
    if (szoveg[kezd] != szoveg[veg]):
        return False
    if kezd < len(szoveg) / 2:
        rekurziv(szoveg, kezd+1, veg-1)
    return True

    

def main():
    szo = "abba"
    if (iterativ(szo)):
        print("Iterativ: igaz")
    else:
        print("Iterativ: hamis")
    if (rekurziv(szo, 0, len(szo) -1)):
        print("Rekurziv: igaz")
    else:
        print("Rekurziv: hamis")

if __name__ == "__main__":
    main()