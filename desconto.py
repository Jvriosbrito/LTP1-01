valor=float(input("Digite o valor inteiro a ser cobrado:"))
desconto=float(input("Digite o valor do desconto:"))
print()
desconto= desconto/100 * valor
valor_final= valor - desconto
print()
print("o valor sem desconto é:",valor)
print("o desconto é de:",desconto)
print("o valor a ser pago é:",valor_final)
