n = float(input("Veuillez donner le nombre de kwh: "))
if (n>0 and n<=100):
    m = n * 75
elif (n<=300):
    m = 100*75 + (n - 100) * 200
else:
    m = 100*75 + 200*200 + (n - 300) * 300
if (n>500):
    t = m * 0.05
else:
    t = 0
print("Le montant de la facture est de", m - t,"francs")