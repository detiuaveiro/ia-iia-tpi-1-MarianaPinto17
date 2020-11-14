# Mariana Pinto, 84792
# Discuti com os meus colegas: 90327, 85088, 93023, 89194

from tree_search import *
from cidades import *
from strips import *

class MyNode(SearchNode):
    #extended method
    def __init__(self,state,parent):
        super().__init__(state,parent)
        self.depth = 0
        self.offset = 0

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth'): 
        super().__init__(problem,strategy)

    def hybrid1_add_to_open(self,lnewnodes):
        #for a in lnewnodes:
            #se for par adiciona no inicio da lista
         #   if(lnewnodes.index(a) % 2 == 0):
         #       self.open_nodes.insert(0,a)
         #   else:
                #caso contrário no fim da lista
         #       self.open_nodes.append(a)
        pass
    # depth -> pronfudidade
    # offset -> posicao de cada no no respetivo nivel
    def hybrid2_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        #for a in lnewnodes:
        pass

    def search2(self):
        # lista por depth, em cada posição adiciona o numero de filhos para depois saber o offset de cada um, adicionar o len de children para incrementar
        nchildren = []
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
                    newnode = MyNode(newstate,node)
                    newnode.depth+=1
                    node.children.append(newnode)
                    #newnode.offset=((node.offset+1)*node.offset)
            self.add_to_open(node.children)
            # Guarda em cada posicao da lista o numero de filhos existentes nesse nivel
            # append do numero de filhos de node na posição depth+1
            # se não existe nenhum valor na posicao depth+1
            if len(nchildren) < newnode.depth:
                #fazemos append
                nchildren.append(len(node.children))
            #se existir
            else:
                #ao valor anterior adicionamos o len de node.children
                nchildren[newnode.depth-1] += len(node.children)
            #o nosso offset é igual ao número de filhos que já existem mais 1
            newnode.offset = nchildren[newnode.depth-1] + 1
            #print(newnode.offset)
        return None

    def search_from_middle(self):
        #IMPLEMENT HERE
        pass

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
        for pc in action.pc:
            if pc not in state:
                return None
        newstate = []
        for st in state:
            newstate.append(st)
            if st in action.neg:
                newstate.remove(st) 
        for st in action.pos:
            newstate.append(st)
        return newstate

    #state é uma lista de actions
    def sort(self,state):
        #faz stor da lista de actions e devolta a lista
        sorted(state, key=lambda x: x.args)
        return state        


