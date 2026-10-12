def ezernelk():
    """1000-nél kisebb számok összege amelyek 3 és 5 többszörösei
    
    Végigmegy 1-től ezerig a 3 és 5 többszörösein és veszi a szummájukat"""
    return sum([i for i in range(1,1000) if i%3==0 or i%5==0])

def main():
    print(ezernelk())

if __name__ == "__main__":
    main()