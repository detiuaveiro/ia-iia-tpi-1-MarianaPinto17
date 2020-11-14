# Mariana Pinto, 84792
# Discuti com os meus colegas: 90327, 85088, 93023, 89194
# acedi aos seguintes sites: https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
# 

from tree_search import *
from cidades import *
from strips import *

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth'): 
        super().__init__(problem,strategy)

    def hybrid1_add_to_open(self,lnewnodes):
        for a in lnewnodes:
            #se for par adiciona no inicio da lista
           if(lnewnodes.index(a) % 2 == 0):
               self.open_nodes.insert(0,a)
           else:
                #caso contrário no fim da lista
                self.open_nodes.append(a)

    def hybrid2_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        self.open_nodes += lnewnodes
        self.open_nodes.sort(key=lambda x: x.depth-x.offset)
        #self.open_nodes = sorted(lnewnodes, key=lambda a: a.depth-a.offset) NAO FUNCIONA ASSIM NAO SEI PORQUE :(
    def search2(self):
        # lista por depth, em cada posição adiciona o numero de nos por cada nivel para depois saber o offset de cada um
        # começa com um porque é o do root que tem um no nível, que é ele próprio ()
        nchildren = [1]
        self.root.depth=0
        self.root.offset=0
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                self.terminal = len(self.open_nodes)+1
                self.solution = node
                return self.get_path(node)
            self.non_terminal+=1
            node.children = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate,node)
                    newnode.depth=node.depth+1
                    node.children.append(newnode)
                    # Guarda em cada posicao da lista o numero de filhos existentes nesse nivel
                    # se não existe nenhum valor na posicao depth+1
                    if len(nchildren) < newnode.depth+1:
                        #fazemos append de um filho
                        nchildren.append(1)
                    #se existir
                    else:
                        # ao valor anterior adicionamos o nó que foi criado
                        nchildren[newnode.depth-1] += 1
                    #o nosso offset é igual ao número de filhos que já existem mais
                    newnode.offset = nchildren[newnode.depth-1] 
                    
            self.add_to_open(node.children)
            #print(newnode.offset)
        return None

    def search_from_middle(self):
        #IMPLEMENT HERE
        mid = MinhasCidades.middle(self.problem.initial, self.problem.goal)
        print(mid)
        

class MinhasCidades(Cidades):
    # state that minimizes heuristic(state1,middle)+heuristic(middle,state2)
    def middle(self,city1,city2):
        rs = []
        for m in self.coordinates:
            if(m!= city1 and m!=city2):
                rs.append((self.heuristic(city1,m) + self.heuristic(city2,m),m))
        #print(rs)
        lista = sorted(rs,key=lambda tup: tup[0])
        #print(lista)
        return lista[0][1]

class MySTRIPS(STRIPS):
    
    def result(self, state, action):
        #para cada precondicao
        for pc in action.pc:
            # se a pre condicao nao esta no state
            if pc not in state:
                return None
        #cria os novos newstates
        newstate = []

        for st in state:
            newstate.append(st)
            #tira-se os negativos
            if st in action.neg:
                newstate.remove(st) 
        for st in action.pos:
            #coloca-se os positivos
            newstate.append(st)
        return newstate

    #state é uma lista de actions
    def sort(self,state):
        #faz sorted da lista de actions e devolve a lista
        sorted(state, key=lambda x: x.args)
        return state        


