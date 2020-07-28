# Conerstions for richter inputed by user
# July 7, 2020

richter_list = [1,5,9.1,9.2,9.5]
print("Richter \t joules \t\t TNT")
for richter in richter_list:
    joules = 10**((1.5*richter)+4.8)
    tons_tnt = joules/(4.184*(10**9))
    print(richter,"\t", joules, "\t\t", tons_tnt)

user_richter = float(input("\nPlease Enter a Richter scale value: "))
joules = 10**((1.5*user_richter)+4.8)
tons_tnt = joules/(4.184*(10**9))

print("Richter scale value:" , user_richter)
print("Equivalence in jules:", joules)
print("Equivalence in tons of TNT:", tons_tnt)