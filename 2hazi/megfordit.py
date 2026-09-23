def megfordit(n):
    temp = str(n)
    forditott = temp[len(temp)-1::-1]
    return int(forditott)


def main():
    szam = 1234
    print(megfordit(szam))

if __name__ == "__main__":
    main()