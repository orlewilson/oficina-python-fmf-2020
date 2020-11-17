'''

	Oficinas da Semana - Python: Por Onde Começar e Quais Suas Aplicações?
	Facilitador:    Orlewilson Bentes Maia
	Data:           17/11/2020
	Nome:           Seu nome
	Descrição:      exemplo de teste em python usando UnitTest
	Fonte:			https://python-guide-pt-br.readthedocs.io/pt_BR/latest/writing/tests.html


'''
import unittest

def quadrado(x):
    return x**2

class MyTest(unittest.TestCase):
	def test1(self):
		self.assertEqual(quadrado(3), 9)

	def test2(self):
		self.assertEqual(quadrado(-2), 4)

if __name__ == '__main__':
    unittest.main()

# execução do código
# python ex-unit-test.py -v