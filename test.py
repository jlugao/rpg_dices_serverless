from unittest import TestCase, main
from collections import Counter
from dices import lanca_d4, lanca_d6, lanca_d8, lanca_d10, lanca_d12, lanca_d20


class TestRPGDices(TestCase):
    '''
        Testa o lançamento de dados de RPG
        ex
    '''
    def _test_dx(self,value, func):
        valores = []
        limite_inferior = 1
        limite_superior = value
        for i in range(1000):
            result = func()
            valores.append(result)
            with self.subTest(f'abaixo de {limite_superior}'):
                self.assertTrue( limite_inferior <= result <= limite_superior )
        with self.subTest('todos os numeros contemplados'):
            expected = [i for i in range(limite_inferior,limite_superior+1)]
            counter = Counter(valores)
            self.assertEqual(sorted(list(counter)), expected)
 
    def test_d4(self):
        self._test_dx(4, lanca_d4)
 
    def test_d6(self):
        self._test_dx(6, lanca_d6)
 
    def test_d8(self):
        self._test_dx(8, lanca_d8)
 
    def test_d10(self):
        self._test_dx(10, lanca_d10)
 
    def test_d12(self):
        self._test_dx(12, lanca_d12)
 
    def test_d20(self):
        self._test_dx(20, lanca_d20)

    # def test_d4(self):
    #     valores = []
    #     limite_inferior = 1
    #     limite_superior = 4
    #     for i in range(1000):
    #         result = lanca_d4()
    #         valores.append(result)
    #         with self.subTest('abaixo de ' + limite_superior):
    #             self.assertTrue( limite_inferior <= result <= limite_superior )
    #     with self.subTest('todos os numeros contemplados'):
    #         expected = [i for i in range(limite_inferior,limite_superior)]
    #         counter = Counter(valores)
    #         self.assertEqual(sorted(list(counter)), expected)




if __name__ == '__main__':
    main()