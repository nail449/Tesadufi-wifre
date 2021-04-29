from random import choice

simvollar = ["a","b","c","d","e","f",1,2,3,4,5,6,7,8,9,0]

print("Sifrenizin uzunlugu nece simvol olsun ?")
sifreuzunluq = int(input())

sifre = ""

for i in range(sifreuzunluq):
    sifre +=str(choice(simvollar))

print(sifre)