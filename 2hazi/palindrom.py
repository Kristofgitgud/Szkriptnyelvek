def isPalindrom(szo):
    if szo == szo[len(szo)-1::-1]:
        return True
    else:
        return False

def main():
    szo = "aha"
    print("Az " + szo + " palindrom-e?")
    print (isPalindrom(szo))

if __name__ == "__main__":
    main()