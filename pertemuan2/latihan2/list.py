angka = [10, 20, 30, 40, 50]
angka.append(60)

angka.remove(20)

for x in angka:
    print(x)

total = 0
for x in angka:
    total += x
rata_rata = total / 5
print(rata_rata)
