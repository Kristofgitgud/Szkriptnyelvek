def xor(s1, s2):
    return bool(abs(bool(s1) - bool (s2)))

def main():
    str1 = "asd"
    str2 = None
    str3 = "nansd"
    print(xor(str1, str3))


if __name__ == "__main__":
    main()