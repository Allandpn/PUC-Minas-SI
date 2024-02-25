from collections import deque

vetores = {   
    0:[1,6],
    1:[0,2,6,7],
    2:[1,3],
    3:[2,4,9,10],
    4:[3],
    5:[8,11],
    6:[0,1,7,8],
    7:[1,6,9],
    8:[5,6,9,10],
    9:[3,7,8,10],
    10:[3,8,9,11],
    11:[5,10]
}


class Vetor:
    def __init__(self, v, adj=0):
        self.v = v
        self.adj = adj
        self.L = 0
        self.nv = 0
        self.pai = None  


Saida = []

arestaArvore = []
arestaTio = []
arestaIrmao = []
arestaPrimo = []


def bfs(r):
    Fila = deque([r])
    
    while Fila:
        v = Fila.popleft()
        for w in v.adj:
            if w.nv == 0:
                w.pai = v.v
                w.nv = v.nv + 1
                Fila.append(w)
                arestaArvore.append(f"{v.v}:{w.v}")
            elif w.nv == v.nv + 1 and w.pai != v.v:
                arestaTio.append(f"{v.v}:{w.v}")
            elif w.nv == v.nv and w.pai == v.pai:
                arestaIrmao.append(f"{v.v}:{w.v}")
            elif w.nv == v.nv and w.pai != v.pai:
                arestaPrimo.append(f"{v.v}:{w.v}")                

class Main:
    def __init__(self):
        
        ListaBL = [Vetor(valor,[]) for valor in range(len(vetores))]
        
        for v, adjacencias  in vetores.items():
            ListaBL[v].adj = [ListaBL[adj] for adj in adjacencias ]        
        
        bfs(ListaBL[0])
        
        print(f"arestaArvore: {arestaArvore}")
        print(f"arestaTio: {arestaTio}")
        print(f"arestaIrmao: {arestaIrmao}")
        print(f"arestaPrimo: {arestaPrimo}")

main_instance = Main()
        
        
   