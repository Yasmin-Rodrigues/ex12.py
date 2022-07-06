#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o valor da hipotenusa
import math
from math import sqrt
o =float(input('Comprimento do cateto oposto:'))
a =float(input('Comprimento do cateto adjacente:'))
s =(o**2) + (a**2)
h =math.sqrt(s)
print('A hipotenusa é igual a soma dos catetos ao quadrado, nesse caso: \nh²= cateto op. + cateto adj.\nh²={}² + {}² \nh²= {} \nh²={:.2f}' .format(o, a, s, h))