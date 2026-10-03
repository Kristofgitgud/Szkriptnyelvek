def main():
    print("5. feladat")
    l5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
    print("".join(l5))

    print("6. feladat")
    sz6 = "1234567"
    l6 = []
    for e in sz6:
        l6.append(e)
    print(l6)

    print("7. feladat")
    sz7 = 'The quick brown fox jumps over the lazy dog'
    l7 = sz7.split(' ')
    eredmeny7 = []
    for e in l7:
        eredmeny7.append(len(e))
    print(eredmeny7)

    print("8. feladat")
    sz8 = "python is an awesome language"
    l8 = sz8.split(" ") 
    eredmeny8 = []
    for e in l8:
        eredmeny8.append(e[:1])
    print(eredmeny8)

    print("9. feladat")
    sz9 = 'The quick brown fox jumps over the lazy dog'
    l9 = sz9.split(" ")
    eredmeny9 = []
    for e in l9:
        eredmeny9.append((e, len(e)))
    print(eredmeny9)

    print("10. feladat")
    l10 = [i for i in range(0, 10) if i%2==0]
    print(l10)

    print("11. feladat")
    l11 = [i*i for i in range(0,20) if i%2==0]
    print(l11)

    print("12. feladat")
    l12 = [i*i for i in range(0,20) if (i*i)%10==4]
    print(l12)

    print("13. feladat")
    l13 = [chr(i) for i in range(65,91)]
    eredmeny13 = "".join(l13)
    print(eredmeny13)

    print("14. feladat")
    l14 = [' apple ', ' banana ', ' kiwi']
    eredmeny14 = [e.strip() for e in l14]
    print(eredmeny14)

    print("15. feladat")
    l15 = [1, 0, 1, 1, 0, 1, 0, 0]
    eredmeny15 = "".join([str(e) for e in l15])
    print(eredmeny15)








if __name__ == "__main__":
    main()