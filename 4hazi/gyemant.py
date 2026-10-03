def diamond(n):
    if n % 2 == 0:
        print("Hiba! a metódus csak páratlan egész pozitívakat fogad el.")
        exit()
    mennyi = 1
    for i in range(1, n + 1):
        
        print(('*' * mennyi).center(n))
        if i < n/2:
            mennyi += 2
        else:
            mennyi -= 2




def main():
    diamond(11)


if __name__ == "__main__":
    main()