def megfordit(szam):
    szoveg = str(szam)
    i = 1
    a = list(range(len(szoveg)))
    for e in szoveg:
        a[len(szoveg) - i] = e
        i += 1
    return ''.join(a)



def main():
    szam = 1234
    print(megfordit(szam))

if __name__ == "__main__":
    main()