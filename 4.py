def ReajusteSalario(s, x):
    reajuste = float(s * (x / 100))
    novoSalario = s + reajuste
    return novoSalario

salario = float(input("Digite seu salario atual: "))
porcentagem = int(input("Digite a porcentagem do reajuste (apenas numeros): "))
novoSalario = ReajusteSalario(salario, porcentagem) 
print(f"Seu salário anterior era {salario} com reajuste de {porcentagem}% fica: {novoSalario:.2f}")

def falarbuceta():
    print("buceta")

falarbuceta()