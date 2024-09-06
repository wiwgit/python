def CalculoNota(media):
    if media >= 6:
        print(f"Aprovado com media {media}")
        return "aprovado"
    elif media < 6 and media >= 4:
        print(f"recuperação com media {media}")
        return "recuperação"
    else: 
        print(f"Reprovado com media {media}")
        return "reprovado"

n1 = float(input("Digita a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2) / 2
situacao = CalculoNota(media)
if situacao == "recuperação":
    recuperacao = float(input("Digite a nota da recuperação: "))
    if (recuperacao + media) >= 12:
        print("Aprovado")
    else: 
        print("Reprovado")