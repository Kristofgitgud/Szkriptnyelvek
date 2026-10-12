def munch(n):
    """Megkeresi az összes Munchausen szamot 0-tol n-ig
    
    brute force-olva megnézi az összes számot és azon belül számjegyet, ha Munchausen kiírja."""
    print("0")
    for i in range(0, n):
        s = str(i)
        ossz = 0
        for j in s:
            ossz += pow(int(j), int(j))
        if ossz == i:
            print(i)

def powaah(n, e):
    szorzat = 1
    for i in range(0, e):
        szorzat *= n
    return szorzat




def main():
    munch(10000)

if __name__ == "__main__":
    main()