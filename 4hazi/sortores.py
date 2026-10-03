import sys
import random as r

UPTO = 100


def main():
    n = 0
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
        n += 1
        if (n == 10):
            n = 0
            print()
    
    print()
    


if __name__ == "__main__":
    main()