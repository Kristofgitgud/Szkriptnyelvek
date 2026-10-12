import sys

def abc():
    for i in range(0, 26):
        print(chr(ord('a') + i), end="")
    print("")

def cba():
    for i in range(0, 26):
        print(chr(ord('z') - i), end="")
    print("")
    

def main():
    """Ha z-a.py akkor kiírja az abc-t fordítva
    
    Egyébként kiírja az abc-t"""
    if sys.argv[0].endswith("z-a.py"):
        cba()
    else:
        abc()

if __name__ == "__main__":
    main()