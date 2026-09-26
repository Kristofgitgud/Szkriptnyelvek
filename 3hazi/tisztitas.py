def tisztit(szoveg):
    tiszta = ""
    for e in szoveg:
        if e != '\n' and e != ' ':
            tiszta = tiszta + e
    return tiszta

def main():
    url = "192.20.246.138:\n 6666"
    print(tisztit(url))

if __name__ == "__main__":
    main()