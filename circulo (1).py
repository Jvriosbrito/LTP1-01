import math

diametro_circulo=float(input("Qual o diâmetro do círculo? "))

raio = diametro_circulo
raio /= 2
# É o mesmo que raio = raio / 2

quadrado = raio
quadrado **= 2
# É o mesmo que quadrado = quadrado ** 2

area = quadrado
area *= math.pi

# area = math.pi * ((diametro_circulo/2) ** 2)

print ("A área de um círculo com diâmetro", diametro_circulo, "é", "%.3f" % area)
# %.3f formatar com três casas decimais
