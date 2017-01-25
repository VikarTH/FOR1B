#Dæmi 3
#Búið til forrit sem spyr notanda um texta.
#Forritið svarar hversu margir hástafir og hversu margir lágstafir eru í textanum, og hversu oft
#lágstafur kemur strax á eftir hástaf.
m = []
j = []

#Til að telja lágstafi
def count_lower(x):
  for i in x:
      if i.islower():
        j.append(x)
  b = len(j)
  return(b)


#Til að telja hástafi
def count_capitals(x):
  for i in x:
      if i.isupper():
        m.append(x)
  n = len(m)
  return(n)

#Fær textann frá notanda
print("Sláðu inn einhvern texta")
texti = input("=")

#Prentar texta
print("Textinn er")
print(": ", texti)

#Þetta telur
hastafurLagstafur = 0
for x in range(len(texti)):
    if texti[x].isupper():
        i = x+1
        if texti[i].islower():
            hastafurLagstafur = hastafurLagstafur + 1

print("Í þessum texta eru ", count_capitals(texti), " Hástafir,", count_lower(texti), "Lágstafir og", hastafurLagstafur , "lágstafir koma strax eftir hástaf.")
