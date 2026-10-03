def osszn(n):
    osszeg = 0
    for i in range(1, n + 1):
        osszeg += i
    return osszeg * osszeg


def nossz(n):
    osszeg = 0
    for i in range(1, n + 1):
        osszeg += (i * i)
    return osszeg

def main():
    print("Első 10 szam osszegenek negyzete: " + str(osszn(10)))
    print("Első 10 szam negyzetenek osszege: " + str(nossz(10)))

    print("Elso 100 kulonbseg: " + str(abs(nossz(100) - osszn(100))))
    


if __name__ == "__main__":
    main()