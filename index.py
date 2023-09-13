import time

class Usuario:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.rg = rg
        self.horaCadastro = time.strftime("%Y-%m-%d %H:%M:%S")

    def dados(self):
        print("\nDados do Usuário:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"RG: {self.rg}")
        print(f"Horário do Cadastro: {self.horaCadastro}")
    

def dadosUsuario():
    nome = input("Digite seu nome aqui! ")
    idade = validarIdade()
    cpf = validarCpf()
    rg = validarRg()
    return Usuario(nome, idade, cpf, rg)

def validarIdade():
    while True:
        try:
            idade = int(input("digite sua idade aqui!"))
            if idade >= 18:
                return idade
            else:
                print("desculpe idade minima, não correspondida!!")
                exit()
        except ValueError:
            print("Idade inválida.")

def validarCpf():
    while True:
        try:
            cpf = input("Digite seu CPF! (Apenas Números)! ")
            if len(cpf) == 11 and cpf.isdigit():
                return cpf
            else:
                print("CPF Invalido! (CPF deve conter 11 digitos)!")
        except ValueError:
            print("CPF invalido!!")

def validarRg():
    while True:
        rg = input("Digite seu RG aqui!! ")
        if len(rg) == 8 and rg.isdigit():
            return rg
        else:
            print("RG invalido! (RG deve conter 8 digitos)")


def main():
    usuario = dadosUsuario()
    usuario.dados()

if __name__ == "__main__":
    main()