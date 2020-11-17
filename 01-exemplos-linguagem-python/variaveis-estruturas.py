'''

	Oficinas da Semana - Python: Por Onde Começar e Quais Suas Aplicações?
	Facilitador:    Orlewilson Bentes Maia
	Data:           17/11/2020
	Nome:           Seu nome
	Descrição:      Variáveis, tipos de dados, operações, estruturas, string

'''

a = 3 #número inteiro
print(a)

b = 3.3 #número decial
c = 4 + 5j #número complexo

print(b)
print(c)

#operações matemáticas
print (a + b)
print (a - b)
print (a / b)
print (a * b)
print (a ** b) # exponenciação

a = int(input('Digite um valor: '))

# condição
if a > 10:
	print (f'{a} > 10')
else:
	print (f'{a} <= 10')

# repetição
for x in range(0,10):
	print (x)

x = 0
while (x < 10):
	x += 1
	print(x)

# formas de impressão de dados
print("Conteúdo da variável a: ", a)
print("Conteúdo das variáveis a e b: %d %f" %(a,b))
print("Conteúdo das variáveis a e b: %d %2.2f" %(a,b))
print(f"Conteúdo da variável a: {a}")

# palavras
nome = 'Orlewilson'
nomeAoContrario = nome[::-1]

print(f'Meu nome é {nome} ao contrário é {nomeAoContrario}')
