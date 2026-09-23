import sys

def main():
    if len(sys.argv) != 3:
        print("Hiba! Adj meg két egész számot!")
        exit
    else:
            print(int(sys.argv[1]) + int(sys.argv[2]))

if __name__ == "__main__":
    main()