TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""

def dekodolas(szoveg):
    megfejtes = ""
    for e in szoveg:
        aszki = ord(e)
        if (aszki >= 65 and aszki <= 90) or (aszki >= 97 and aszki <= 122):
            if ((aszki + 2) > 90 and (aszki + 2) <= 92) or ((aszki + 2) > 122 and (aszki + 2) <= 124):
                megfejtes = megfejtes + chr(aszki - 24)
            else:   
                megfejtes = megfejtes + chr(aszki + 2)
        else:
            megfejtes += e
    return megfejtes

def main():
    #print(TEXT) 
    #print("------------------------------------------")
    print(dekodolas(TEXT))

if __name__ == "__main__":
    main()