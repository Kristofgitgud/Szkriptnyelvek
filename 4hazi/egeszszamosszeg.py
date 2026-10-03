def main():
    osszeg = 0
    for i in range(1, 101):
        for e in list(str(i)):

            osszeg += int(e)

    print("Egesz szamok osszege 1-től 100-ig: " + str((1+100)*50))

    print("Egesz szamok szamjegyeinek osszege 1-től 100-ig: " + str(osszeg))


if __name__ == "__main__":
    main()