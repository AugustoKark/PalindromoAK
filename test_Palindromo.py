import unittest


def palindromos(palabra):
    palabra = palabra.replace('','')
    reverse_string = palabra[::-1]
    if palabra.lower() == reverse_string.lower():
        return True
    return False




class Test_Palindromo(unittest.TestCase):
    def test_Palindromo_1(self):
        es_palindromo = palindromos("OJO")
        self.assertTrue(es_palindromo)

    def test_Palindromo_2(self):
        es_palindromo = palindromos("OsO")
        self.assertTrue(es_palindromo)

    def test_Palindromo_3(self):
        es_palindromo = palindromos("ANa")
        self.assertTrue(es_palindromo)

    def test_Palindromo_4(self):
        es_palindromo = palindromos("neuquen")
        self.assertTrue(es_palindromo)
    

    def test_Palindromo_5(self):
        es_palindromo = palindromos("NeuQuen")
        self.assertTrue(es_palindromo)
    

    def test_Palindromo_6(self):
        es_palindromo = palindromos("salas")
        self.assertTrue(es_palindromo)
    

    
if __name__ == '__main__':
    unittest.main()