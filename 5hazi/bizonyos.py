def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """Megadunk egy szöveget, és a szövegből visszaadja azokat a karaktereket
    amelyeket chars is tartalmaz.
    
    ciklussal végigmegyünk, és hozzáadjuk s-hez, ha benne van chars-ban."""
    s = ""
    for i in text:
        if chars.__contains__(i):
            s = s + i
    return s


def main():
    print(valid("KecskeAttila0606", "0123"))


if __name__ == "__main__":
    main()