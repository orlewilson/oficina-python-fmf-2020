'''

	Oficinas da Semana - Python: Por Onde Começar e Quais Suas Aplicações?
	Facilitador:    Orlewilson Bentes Maia
	Data:           17/11/2020
	Nome:           Seu nome
	Descrição:      exemplo de teste em python usando Selenium
	Fonte:			https://selenium-python.readthedocs.io/getting-started.html
					https://chromedriver.chromium.org/downloads
					https://github.com/mozilla/geckodriver/releases/


'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

	# seleciona o navegador
	def setUp(self):
		#self.driver = webdriver.Firefox() # firefox
		self.driver = webdriver.Chrome() # chome

	# caso de teste
	def test_search_in_python_org(self):
		driver = self.driver
		driver.get("http://www.python.org")
		# verifica se há a palavra Python no título da página
		self.assertIn("Python", driver.title)
	
	# fecha o navegador
	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()

# execução do código
# python ex-selenium.py -v