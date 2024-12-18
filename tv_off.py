# primarily a test to practice git-merge conflict resolution

def tv_off(n):

    import time

    def gnx(n):
        if n < 1:
            n = 1
        for i in range(round(n)):
            yield 'A'

    ui = 0.64
    sfx = "DUN!"

    for i in range(13):
        print(sfx); time.sleep(ui)
    print("DUN-\n")

    while True:
        try:
            n = float(input("Somebody gotta do it... but how many times?? "))
        except ValueError:
            print("A numeric entry is required...")
            continue
        else:
            break

    print(f"MUST{''.join(gnx(n))}RD{'!' * round(n/10)}")

tv_off()