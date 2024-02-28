# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:10:32 2024

@author: 21.00422-6
"""

import cmath

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def raiz_quadrada(a):
    return cmath.sqrt(a)

def exibir_menu():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz Quadrada")
    print("6. Sair")

def main():
    while True:
        exibir_menu()
        escolha = input("Digite sua escolha (1/2/3/4/5/6): ")

        if escolha in ['1', '2', '3', '4']:
            
            
            num1 = complex(input("Digite o primeiro número: "))
            num2 = complex(input("Digite o segundo número: "))
        
            
            if escolha == '1':
                resultado = soma(num1, num2)
                if (resultado.imag == 0):
                    resultado = resultado.real
                print("Resultado:", resultado)
            elif escolha == '2':
                resultado = subtracao(num1, num2)
                 if (resultado.imag == 0):
                    resultado = resultado.real
                print("Resultado:", resultado)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
                 if (resultado.imag == 0):
                    resultado = resultado.real
                print("Resultado:", resultado)
            elif escolha == '4':
                if num2 != 0:
                    resultado = divisao(num1, num2)
                     if (resultado.imag == 0):
                    resultado = resultado.real
                    print("Resultado:", resultado)
                else:
                    print("Erro: Divisão por zero!")

        elif escolha == '5':
            num = complex(input("Digite o número para calcular a raiz quadrada: "))
            resultado = raiz_quadrada(num)
            print("Resultado:", resultado)
        
        elif escolha == '6':
            print("Saindo...")
            break
        
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
