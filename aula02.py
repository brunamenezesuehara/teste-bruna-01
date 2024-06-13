def calcular_salario():
    ganho_hora = float(input("Quanto você ganha por hora? "))
    horas_trabalhadas = float(input("Número de horas trabalhadas no mês: "))
    salario_bruto = ganho_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    sindicato = salario_bruto * 0.05
    descontos = ir + inss + sindicato # type: ignore
    salario_liquido = salario_bruto - descontos
    print(f"+ Salário Bruto : R$ {salario_bruto:.2f}")
    print(f"- IR (11%) : R$ {ir:.2f}")
    print(f"- INSS (8%) : R$ {inss:.2f}") # type: ignore
    print(f"- Sindicato (5%) : R$ {sindicato:.2f}")
    print(f"= Salário Líquido : R$ {salario_liquido:.2f}")

def calcular_tempo_download():
    tamanho_arquivo = float(input("Tamanho do arquivo para download (em MB): "))
    velocidade_internet = float(input("Velocidade do link de Internet (em Mbps): "))
    velocidade_internet_MBps = velocidade_internet * 0.125
    tempo_segundos = tamanho_arquivo / velocidade_internet_MBps
    tempo_minutos = tempo_segundos / 60
    print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos")

def main():
    print("Selecione uma opção:")
    print("1. Calcular Salário")
    print("2. Calcular Tempo de Download")
    opcao = input("Opção (1 ou 2): ")
    if opcao == "1":
        calcular_salario()
    elif opcao == "2":
        calcular_tempo_download()
    else:
        print("Opção inválida")
    if __name__ == "__main__":
        main()