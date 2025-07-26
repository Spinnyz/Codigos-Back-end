user = {}

quan_user = int(input("Digite a quantidade de usuários:"))

for i in range (quan_user):
    entrada = input("Digite o nome e a profissão: ").strip().capitalize()
    usua, prof = entrada.split(",") #separa com o split

    if "," not in entrada:
        print ("Formato invalido faça com o formato (nome,profissão)")
        continue

    if prof not in user: 
        user[prof] = []
        user[prof].append(usua)

for prof, nome in user.items():
    print(f"{prof}: {', '.join(nome)}")