def product(numbers):
    szorzat = 1
    for e in numbers:
        szorzat *= e
    return szorzat

def main():
    szamok = [1, 2, 3, 1, 1]
    print(product(szamok))

if __name__ == "__main__":
    main()