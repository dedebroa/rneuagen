import math 

############## 25/05 ################

class Valor:
    def __init__(self, data, progenitor=(), operador_mae="", rotulo=""): # só roda quando criamos uma instância
        self.data = data
        self.progenitor = progenitor
        self.operador_mae = operador_mae
        self.rotulo = rotulo
        self.grad = 0

    def __repr__(self):
        return f"Valor(data={self.data})"

    def __add__(self, outro_valor):
        if not isinstance(outro_valor, Valor): # o problema é se não for uma instância 
                                                # condicional chegando se o outro valor é uma instância da classe valor
            outro_valor = Valor(outro_valor) # trannforma a não instância em uma instância então
        data = self.data + outro_valor.data
        progenitor = (self, outro_valor)
        operador_mae = "+"
        saida = Valor(data, progenitor, operador_mae)

        def propagar_adicao():
            self.grad += saida.grad * 1
            outro_valor.grad += saida.grad * 1

        saida.propagar = propagar_adicao

        return saida
    
    def __radd__(self, outro_valor): # outro_valor + self
                                        # correção de erro
        return self + outro_valor # primeiro argumento é sempre self

    def __mul__(self, outro_valor):
        if not isinstance(outro_valor, Valor): 
            outro_valor = Valor(outro_valor) 
        data = self.data * outro_valor.data
        progenitor = (self, outro_valor)
        operador_mae = "*"
        saida = Valor(data, progenitor, operador_mae)

        def propagar_multiplicacao():
            self.grad += saida.grad * outro_valor.data
            outro_valor.grad += saida.grad * self.data

        saida.propagar = propagar_multiplicacao

        return saida
    
    def __rmul__(self, outro_valor): # outro_valor + self
                                        # correção de erro
        return self * outro_valor
    
    def __pow__(self, expoente):
        
        assert isinstance(expoente, (int, float)) # se assegura de que isso é verdadeiro
        
        data = self.data ** expoente
        progenitor = (self, )
        operador_mae = f"**{expoente}" # é so uma string
        saida = Valor(data, progenitor, operador_mae)
        
        def propagar_exponenciacao():
            # gradiente de onde estou é o gradiente vezes o filho
            self.grad += saida.grad * expoente * (self.data ** (expoente - 1))

        saida.propagar = propagar_exponenciacao

        return saida
        

    def __truediv__(self, outro_valor): # self/outro_valor
        return self * outro_valor ** (-1)
    
    def __neg__(self): # - self
        return self * (-1)
    
    def __sub__(self, outro_valor):  # self - outro_valor
        return self + (- outro_valor)
    
    def __rsub__(self, outro_valor): # outro_valor - self
        return self * (-1) + outro_valor
    
    def exp(self): # calcular o exponencial de um número qualquer
        # math é quem calcula exponencias, a biblioteca de matemática
        data = math.exp(self.data)
        progenitor = (self, ) # função unária, o próprio valor # só tem um genitor
        operador_mae = "exp"
        saida = Valor(data, progenitor, operador_mae)

        def propagar_exp():
            self.grad += saida.grad * data

        saida.propagar = propagar_exp

        return saida
    
    def sig(self):
        return self.exp() / (self.exp() + 1)
        
    def propagar(self):
        pass

    def propagar_tudo(self):
        ordem_topologica = []
        visitados = set()

        def constroi_ordem_topologica(v):
            if v not in visitados:
                visitados.add(v)
                for progenitor in v.progenitor:
                    constroi_ordem_topologica(progenitor)
                ordem_topologica.append(v)

        constroi_ordem_topologica(self)

        self.grad = 1  # o gradiente do vértice folha deve ser 1

        for v in reversed(ordem_topologica):
            v.propagar() 
            
            
            
