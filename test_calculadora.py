#	test_calculadora.py	
import	unittest	
from	calculadora	import	sumar,	restar,	dividir	
class	TestCalculadora(unittest.TestCase):	
def	test_sumar(self):	
self.assertEqual(sumar(2,	3),	5)	
self.assertEqual(sumar(-1,	1),	0)	
def	test_restar(self):	
self.assertEqual(restar(5,	2),	3)	
self.assertEqual(restar(0,	0),	0)	
def	test_dividir(self):	
self.assertEqual(dividir(10,	2),	5)	
with	self.assertRaises(ValueError):	
dividir(5,	0)	
if	__name__	==	'__main__':	
unittest.main()	