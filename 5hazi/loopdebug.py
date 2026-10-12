def loop(n, debug=False):
    """Kiírja a számokat 1-től n-ig
    
    Ciklussal számonként kiírja 1-től n-ig"""
    if debug:
        print("Ciklus kezdete")
    for i in range(1, n + 1):
        print(i, end=" ")
    print("")
    if debug:
        print("Ciklus vége")


def main():
    loop(5)
    loop(5, debug=True)

if __name__ == "__main__":
    main()