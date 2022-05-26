# Prosty przykładowy liczlnik do 10

# Z bledem:

licznik = 0
while licznik <= 10:
    print(licznik)

# po naprawie

licznik = 0
while licznik <= 10:
    licznik += 1
    if licznik == 11:
        break
    print(licznik)