def gnx(n):
    if n < 1:
        n = 1
    for i in range(round(n)):
        yield 'A'

while True:
    try:
        n = float(input("Somebody gotta do it... but how many times?? "))
    except ValueError:
        print("A numeric entry is required...")
        continue
    else:
        break

print(f"MUST{''.join(gnx(n))}RD{'!' * round(n/10)}")