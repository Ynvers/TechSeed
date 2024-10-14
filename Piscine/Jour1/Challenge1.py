import datetime

age = int(input("Entrez votre age s'il vous plait : "))

def quand_aura_tu_100_ans(age):
    return 100 - age 

def annee_des_100_ans(age):
    return datetime.date.today().year + quand_aura_tu_100_ans(age)

result = f"""
Vous aurez 100 ans dans {quand_aura_tu_100_ans(age)}ans.
Soit en {annee_des_100_ans(age)}.
Veillissez bien
"""
print(result)