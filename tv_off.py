def tv_off(n):

    def gnx(n):
        if n < 1:
            n = 1
        for i in range(round(n)):
            yield 'A'
    
    print(f"MUST{''.join(gnx(n))}RD{'!' * round(n/10)}")

n = input("Somebody gotta do it... but how many times?? ")

tv_off(int(n))