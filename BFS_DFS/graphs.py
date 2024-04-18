#!/usr/bin/env python
# _*_ coding: utf8 _*_

import random
import string
import math
import numpy as np

class Queue:
    tam = None
    tope = None
    datos = None

    def __init__(self, tam):
        self.tam = tam
        self.datos = []

    def push(self, dato):
        if(self.llena()):
            return False
        else:
            self.datos.append(dato)
            return True
    def llena(self):
        if len(self.datos) == self.tam:
            return True
        else:
            return False
    def pop(self):
        if self.vacia():
            return True
        else:
            valor = self.datos.pop()
            return valor
    def vacia(self):
        if len(self.datos) == 0:
            return True
        else:
            return False
    def revisar(self,aristas):
        for arista in aristas:
            if arista.destino.visited == False:
                return True
            else:
                return False

class Nodo:
    
    def __init__(self, idson, pos):
        self.idson = idson
        self.aristas_salientes = []
        self.pos= pos
        self.aristas_posibles = 0
        self.valorEquis = 0
        self.valorYe =0
        self.visited = False

    def agregar_arista_saliente(self, arista):
        self.aristas_salientes.append(arista)
    def toString(self, nodo):
        return f"Nodo(idson={nodo.idson}, pos={nodo.pos}), visited={nodo.visited}"


class Arista:
    def __init__(self, origen, destino, grado = 1):
        self.origen = origen
        self.destino = destino
        self.grado = grado
    def toString(self, arista):
        return f"origen={arista.origen}"+" "+f"destino={arista.destino}"

class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)
        return self.nodos

    def agregarArista(self, origen, destino):
        arista = Arista(origen, destino)
        self.aristas.append(arista)
        origen.aristas_salientes.append(arista)

    def grado_nodo(self, nodo):
        return len(nodo.aristas_salientes)
    def generaId(self):
        idcitoBb= "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(10)
            )
        return idcitoBb
    def limpiaGrafo(self, grafo):
        for arista in grafo.aristas:
            arista.origen.visited = False
            arista.destino.visited = False
        return grafo
    def toString(self, grafo):
        return f"Grafo(nodos={grafo.nodos}, aristas={grafo.aristas})"
    


    def grafoMalla(self,m, n, dirigido=False):
        """
        Genera grafo de malla
        :param m: número de columnas (> 1)
        :param n: número de filas (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t = 0; s = 0
        for x in range(m):
            l = list()
            
            for y in range (n):
                idcito = self.generaId
                pos = f"{t},{s}"
                s+=1
                nodo = Nodo(idcito, pos)
                l.append(nodo)
                
            nodos= self.agregar_nodo(l)
            t+=1;s=0

        i=0
        j=0
        for i in range(len(nodos)):
            for j in range(len(nodos[i])):
                if j<n-1: 
                    
                    if nodos[i][j].idson == nodos[i][j+1].idson:    
                        nodos[i][j+1].idson = self.generaId()
                    
                    arista = Arista(nodos[i][j],nodos[i][j+1])
                    nodos[i][j].aristas_salientes.append(nodos[i][j+1])
                    self.aristas.append(arista)
                    
                if i<m-1:
                    if (nodos[i][j].idson == nodos[i+1][j].idson):
                        nodos[i+1][j].idson = self.generaId()
                    arista = Arista(nodos[i][j], nodos[i+1][j])
                    nodos[i][j].aristas_salientes.append(nodos[i+1][j])
                    self.aristas.append(arista)
                if(i<m-1 and j<n-1):
                    
                    print(str(nodos[i][j].pos)+'--------'+ str(nodos[i][j+1].pos) +'\n|\n|\n|\n|\n'+str(nodos[i+1][j].pos))
                j+=1
            i+=1
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito
    
        
    def grafoErdosRenyi(self,n, m, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Erdos-Renyi
        :param n: número de nodos (> 0)
        :param m: número de aristas (>= n-1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t=0
        for x in range(n):
            for y in range(3):
                l = list()
                idcito = self.generaId()
                nodo = Nodo(idcito, str(t))
                nodos = self.agregar_nodo(nodo)
                t+=1

                if (x >0):
                    numerillo = random.randint(0,x)
                    if(numerillo != [x]):
                        p = 1 - (nodos[x].aristas_posibles/n)
                        if p> random.random():
                            if(nodos[numerillo].aristas_posibles < 4 and nodos[x].aristas_posibles < 4):
                                arista = Arista(nodos[x], nodos[numerillo])
                                self.agregarArista(nodos[x], nodos[numerillo])
                                nodos[numerillo].aristas_posibles +=1
                                nodos[x].aristas_posibles += 1

                if(len(self.aristas) < m-1):
                    break
        grafillo = Grafo()
        grafillo.nodos = self.nodos
        grafillo.aristas = self.aristas
        return grafillo
        
    def grafoGilbert(self,n, p, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Gilbert
        :param n: número de nodos (> 0)
        :param p: probabilidad de crear una arista (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t=0
        for x in range(n):
            l = list()
            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            nodos = self.agregar_nodo(nodo)
            t+=1
        i=0;j=0
        nodos2 = nodos
        for i in range(len(nodos)):
            for j in range(len(nodos2)):
                if(nodos[i].pos != nodos2[j].pos):
                    if(p > random.random()):
                        arista = Arista(nodos[i], nodos2[j])
                        self.agregarArista(nodos[i], nodos2[j])
            j+=1
        i+=1
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito

    def grafoGeografico(self,n, r, dirigido=False):
        """
        Genera grafo aleatorio con el modelo geográfico simple
        :param n: número de nodos (> 0)
        :param r: distancia máxima para crear un nodo (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        #Esta función calcula la probabilidad mediante una función exponencial utilizando la distancia
        #la agrego porque si sólo me baso en la distancia, no va a existir un valor probabilístico real
        
        t=0
        for x in range(n):

            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            numerilloUno= random.random(); numerilloDos = random.random()
            nodo.valorEquis = numerilloUno; nodo.valorYe = numerilloDos
            nodos = self.agregar_nodo(nodo)
            t+=1
        y=0
        for y in range(n):
            
            
            nodoRandom = nodos[random.randint(0,n-1)]
            index = nodos.index(nodoRandom)
            if(nodoRandom.idson != nodos[y].idson):
                euclidesDist = math.sqrt((nodoRandom.valorEquis - nodos[y].valorEquis)**2 + (nodoRandom.valorYe - nodos[y].valorYe)**2)

                if(euclidesDist < r):
                    self.agregarArista(nodos[y], nodos[index])
                    arista = Arista(nodos[y], nodos[index])
        y+=1
        
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito
    
    def grafoBarabasiAlbert(self,n, d, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (> 0)
        :param d: grado máximo esperado por cada nodo (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        t=0; x=0
        for x in range(d):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            nodos = self.agregar_nodo(nodo)
            t+=1
            if(x>0 and x< len(range(d))):
                self.agregarArista(nodos[x], nodos[x-1])
                nodos[x].aristas_posibles +=1
                nodos[x-1].aristas_posibles +=1
                if x == d-1:
                    
                    self.agregarArista(nodos[x], nodos[0])
                    nodos[x].aristas_posibles +=1
                    nodos[0].aristas_posibles +=1
            x+=1
        y=0;s=0;l=d
        for y in range(len(nodos), n):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(l))
            nodos = self.agregar_nodo(nodo)
            l+=1
            
            numerillo =  random.randint(0, y-1)
            if(nodos[y].idson != nodos[numerillo]):
                self.agregarArista(nodos[y], nodos[numerillo])

            y+=1
        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito

    def grafoDorogovtsevMendes(self,n, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (≥ 3)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        d=3
        t=0; x=0
        for x in range(d):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(t))
            nodos = self.agregar_nodo(nodo)
            t+=1
            if(x>0 and x< len(range(d))):
                self.agregarArista(nodos[x], nodos[x-1])
                nodos[x].aristas_posibles +=1
                nodos[x-1].aristas_posibles +=1
                if x == d-1:
                    
                    self.agregarArista(nodos[x], nodos[0])
                    
                    nodos[x].aristas_posibles +=1
                    nodos[0].aristas_posibles +=1
            x+=1
        y=0;l=d
        for y in range(len(nodos), n):
            idcito = self.generaId()
            nodo = Nodo(idcito, str(l))
            nodos = self.agregar_nodo(nodo)
            l+=1
            
            numerillo =  random.randint(0, y-1)
            if(nodos[y].idson != nodos[numerillo]):
                self.agregarArista(nodos[y], nodos[numerillo])

            y+=1

        grafito = Grafo()
        grafito.nodos = self.nodos
        grafito.aristas = self.aristas
        return grafito
    
    def generaGephi(self, grafo, nombre_archivo):
        dot = "graph G {\n"
        
        x=0
        for arista in grafo.aristas:
            dot += f'  {grafo.aristas[x].origen.pos} -- {grafo.aristas[x].destino.pos};\n'
            x+=1
        dot += "}"
        
        with open(nombre_archivo + '.gv', 'w') as archivo_dot:
            archivo_dot.write(dot)
    def bfs(self, grafo, inicio):
        grafitoBFS = Grafo()
        for arista in grafo.aristas:
            arista.destino.visited = False; arista.origen.visited = False
        q = Queue(len(grafo.aristas))
        nodito = grafo.aristas[inicio].origen
        nodo = Nodo(0,0)
        nodito.visited = True
        q.push(nodito)
        while len(q.datos) != 0:
            nodoActual = q.pop()
            destino = nodoActual
            lista = grafo.aristas
            i =0
            if(i < q.tam):
                for arista in grafo.aristas:
                    if(arista.destino.visited == False):
                        u = arista.destino
                        u.visited = True
                        q.push(u)
                        arista = Arista(arista.origen, arista.destino)
                        grafitoBFS.agregarArista(arista.origen, arista.destino)
            else:
                grafo.aristas[i].destino.visited = True
                print("Se ha completado el BFS")
        return grafitoBFS

    def dfs_r(self, grafo, u, v, grafito):
        aristas = grafo.aristas
        
        if(v < len(aristas)):
            aristas[u].origen.visited = True
            
            for arista in aristas:
                if arista.origen == aristas[u].origen and not arista.destino.visited:
                    grafito.agregarArista(arista.origen, arista.destino)
                    u = v
                    self.dfs_r(grafo, u, v+1, grafito)
        return grafito
    
    def dfs_i_malla(self, grafo, inicio):
        stack = [grafo.aristas[inicio]]
        grafillo = Grafo()
        stack = [grafo.aristas[inicio]]
        grafillo = Grafo()
        nodito = Nodo(0,0)
        grafo.aristas[inicio].origen.visited = True
        try:
            while stack:
                nodo_actual = stack.pop()
                if(nodo_actual is not None and nodo_actual != grafo.nodos[len(grafo.nodos)-1][0]):
                    nodo_actual= nodo_actual
                for arista in grafo.aristas:
                    nodo_actual.toString(nodo_actual)
                    if not arista.destino.visited:
                        arista.destino.visited = True
                        stack.append(arista.destino)
                        grafillo.agregarArista(nodo_actual.origen, arista.destino)

            for nodo in grafo.nodos:
                nodo.visited = False
        except:
            print("Se ha leído todo el grafo")
        return grafillo
    def dfs_i(self, grafo, inicio):
        
        grafillo = Grafo()
        nodito = Nodo(0,0)
        grafo.aristas[inicio].origen.visited = True
        nodo = grafo.aristas[inicio].origen
        stack = [nodo]
        while stack:
            nodo_actual = stack.pop()
            if(nodo_actual.visited == True):
                for arista in grafo.aristas:
                    nodo_actual.toString(nodo_actual)
                    if not arista.destino.visited:
                        arista.destino.visited = True
                        stack.append(arista.destino)
                        grafillo.agregarArista(nodo_actual, arista.destino)
            print("intentito")
        return grafillo

  
malla30 = Grafo().grafoMalla(30,1, False)
qMalla30 = Queue(len(malla30.aristas))
dsf_i_chico= Grafo().dfs_i_malla(malla30, 0)
bfs_malla30 = Grafo().bfs(malla30, 0)
grafito = Grafo()
dfsRMalla30 = Grafo().dfs_r(grafito.limpiaGrafo(malla30),0,1, grafito)
Grafo().generaGephi(dsf_i_chico, "mallachicoDSF")
Grafo().generaGephi(bfs_malla30,"mallachicoBFS")
Grafo().generaGephi(dfsRMalla30, "mallaRec30")
malla100 = Grafo().grafoMalla(100,1, False)
dfs_i_malla_mediano = Grafo().dfs_i_malla(malla100,0)
bfs_malla100 = Grafo().bfs(malla100, 0)
grafito = Grafo()
dfsRMalla100 = Grafo().dfs_r(grafito.limpiaGrafo(malla100),0,1, grafito)
Grafo().generaGephi(dfs_i_malla_mediano, "mallamedianoDSF")
Grafo().generaGephi(bfs_malla100,"mallamedianoBFS")
Grafo().generaGephi(dfsRMalla100, "MallaRec100")
malla500 = Grafo().grafoMalla(500,1, False)
dfs_i_malla_grande = Grafo().dfs_i_malla(malla500, 0)
bfs_malla500 = Grafo().bfs(malla500, 0)
grafito = Grafo()
dfsRMalla500 = Grafo().dfs_r(grafito.limpiaGrafo(malla500),0,1, grafito)
Grafo().generaGephi(bfs_malla500,"mallaGrandeBFS")
Grafo().generaGephi(dfsRMalla500, "mallaRec500")
Grafo().generaGephi(dfs_i_malla_grande, "mallaGandeDFS")

erdos30 = Grafo().grafoErdosRenyi(30,4, False)
dfs_i_erdos30 = Grafo().dfs_i_malla(erdos30, 0)
bfs_erdos30 = Grafo().bfs(erdos30, 0)
grafito = Grafo()
dfsRerdos30 = Grafo().dfs_r(grafito.limpiaGrafo(erdos30),0,1, grafito)
Grafo().generaGephi(dfs_i_erdos30, "erdos30DFS")
Grafo().generaGephi(dfsRerdos30,"erdosRec30")
Grafo().generaGephi(bfs_erdos30, "erdosBFS30")

erdos100 = Grafo().grafoErdosRenyi(100,4, False)
dfs_i_erdos100 = Grafo().dfs_i(erdos100,0)
bfs_erdos100 = Grafo().bfs(erdos100, 0)
grafito = Grafo()
dfsRerdos100 = Grafo().dfs_r(grafito.limpiaGrafo(erdos100),0,1, grafito)
Grafo().generaGephi(dfs_i_erdos100, "erdos100DFS")
Grafo().generaGephi(dfsRerdos100,"erdosRec100")
Grafo().generaGephi(bfs_erdos100, "erdosBFS100")

erdos500 = Grafo().grafoErdosRenyi(500,4, False)
dfs_i_erdos500 = Grafo().dfs_i(erdos500,0)
bfs_erdos500 = Grafo().bfs(erdos500, 0)
grafito = Grafo()
dfsRerdos500 = Grafo().dfs_r(grafito.limpiaGrafo(erdos500),0,1, grafito)
Grafo().generaGephi(dfs_i_erdos500, "erdos100DFS")
Grafo().generaGephi(dfsRerdos500,"erdosRec100")
Grafo().generaGephi(bfs_erdos500, "erdosBFS100")

gilbert30 = Grafo().grafoGilbert(30,0.2,False)
dfs_i_gilbert30 = Grafo().dfs_i(gilbert30,0)
Grafo().generaGephi(dfs_i_gilbert30, "gilbertchicoDFS")
gilbert100 = Grafo().grafoGilbert(100,0.2,False)
dfs_i_gilbert100 = Grafo().dfs_i(gilbert100,0)
Grafo().generaGephi(dfs_i_gilbert100, "gilbertmedianoDFS")
gilbert500 = Grafo().grafoGilbert(500,0.2,False)
dfs_i_gilbert500 = Grafo().dfs_i(gilbert500,0)
Grafo().generaGephi(dfs_i_gilbert500, "gilbertgrandeDFS")


geo30 = Grafo().grafoGeografico(30,1, False)
dfs_i_geo30 = Grafo().dfs_i(geo30,0)
bfs_geo30 = Grafo().bfs(geo30, 0)
grafito = Grafo()
dfsRgeo30 = Grafo().dfs_r(grafito.limpiaGrafo(geo30),0,1, grafito)
Grafo().generaGephi(dfs_i_geo30, "geo30DFS")
Grafo().generaGephi(dfsRgeo30,"geoRec30")
Grafo().generaGephi(bfs_geo30, "geoBFS30")

geo100 = Grafo().grafoGeografico(100,1, False)
dfs_i_geo100 = Grafo().dfs_i(geo100,0)
bfs_geo30 = Grafo().bfs(geo30, 0)
grafito = Grafo()
dfsRgeo30 = Grafo().dfs_r(grafito.limpiaGrafo(geo30),0,1, grafito)
Grafo().generaGephi(dfs_i_geo30, "geo30DFS")
Grafo().generaGephi(dfsRgeo30,"geoRec30")
Grafo().generaGephi(bfs_geo30, "geoBFS30")

bfs_geo100 = Grafo().bfs(geo100, 0)
grafito = Grafo()
dfsRgeo100 = Grafo().dfs_r(grafito.limpiaGrafo(geo100),0,1, grafito)
Grafo().generaGephi(dfs_i_geo100, "geo100DFS")
Grafo().generaGephi(dfsRgeo30,"geoRec100")
Grafo().generaGephi(bfs_geo30, "geoBFS100")


geo500 = Grafo().grafoGeografico(500,1, False)
dfs_i_geo500 = Grafo().dfs_i(geo500,0)
bfs_geo500 = Grafo().bfs(geo500, 0)
grafito = Grafo()
dfsRgeo500 = Grafo().dfs_r(grafito.limpiaGrafo(geo500),0,1, grafito)
Grafo().generaGephi(dfs_i_geo500, "geo500DFS")
Grafo().generaGephi(dfsRgeo500,"geoRec500")
Grafo().generaGephi(bfs_geo500, "geoBFS500")

barabasi30 = Grafo().grafoBarabasiAlbert(30, 5, False)
dfs_i_barabasi30 = Grafo().dfs_i(barabasi30,0)
bfs_barabasi30 = Grafo().bfs(barabasi30, 0)
grafito = Grafo()
dfsRbarabasi30 = Grafo().dfs_r(grafito.limpiaGrafo(barabasi30),0,1, grafito)
Grafo().generaGephi(dfs_i_barabasi30, "barabasi30DFS")
Grafo().generaGephi(dfsRbarabasi30,"barabasiRec30")
Grafo().generaGephi(bfs_barabasi30, "barabasiBFS30")

barabasi100 = Grafo().grafoBarabasiAlbert(100, 5, False)
dfs_i_barabasi100 = Grafo().dfs_i(barabasi100,0)
bfs_barabasi100 = Grafo().bfs(barabasi100, 0)
grafito = Grafo()
dfsRbarabasi100 = Grafo().dfs_r(grafito.limpiaGrafo(barabasi100),0,1, grafito)
Grafo().generaGephi(dfs_i_barabasi100, "barabasi100DFS")
Grafo().generaGephi(dfsRbarabasi100,"barabasiRec100")
Grafo().generaGephi(bfs_barabasi100, "barabasiBFS100")

barabasi500 = Grafo().grafoBarabasiAlbert(500, 5, False)
dfs_i_barabasi500 = Grafo().dfs_i(barabasi500,0)
bfs_barabasi500 = Grafo().bfs(barabasi500, 0)
grafito = Grafo()
dfsRbarabasi500 = Grafo().dfs_r(grafito.limpiaGrafo(barabasi500),0,1, grafito)
Grafo().generaGephi(dfs_i_barabasi500, "barabasi500DFS")
Grafo().generaGephi(dfsRbarabasi500,"barabasiRec500")
Grafo().generaGephi(bfs_barabasi500, "barabasiBFS500")

mendes30 = Grafo().grafoDorogovtsevMendes(30, False)
dfs_i_mendes30 = Grafo().dfs_i(mendes30,0)
bfs_mendes30 = Grafo().bfs(mendes30, 0)
grafito = Grafo()
dfsRmendes30 = Grafo().dfs_r(grafito.limpiaGrafo(mendes30),0,1, grafito)
Grafo().generaGephi(dfs_i_mendes30, "mendes30DFS")
Grafo().generaGephi(dfsRmendes30,"mendesRec30")
Grafo().generaGephi(bfs_mendes30, "mendesBFS30")

mendes100 = Grafo().grafoDorogovtsevMendes(100, False)
dfs_i_mendes100 = Grafo().dfs_i(mendes100,0)
bfs_mendes100 = Grafo().bfs(mendes100, 0)
grafito = Grafo()
dfsRmendes100 = Grafo().dfs_r(grafito.limpiaGrafo(mendes100),0,1, grafito)
Grafo().generaGephi(dfs_i_mendes100, "mendes100DFS")
Grafo().generaGephi(dfsRmendes100,"mendesRec100")
Grafo().generaGephi(bfs_mendes100, "mendesBFS100")

mendes500 = Grafo().grafoDorogovtsevMendes(500, False)
dfs_i_mendes500 = Grafo().dfs_i(mendes500,0)
bfs_mendes500 = Grafo().bfs(mendes500, 0)
grafito = Grafo()
dfsRmendes500 = Grafo().dfs_r(grafito.limpiaGrafo(mendes500),0,1, grafito)
Grafo().generaGephi(dfs_i_mendes500, "mendes500DFS")
Grafo().generaGephi(dfsRmendes500,"mendesRec500")
Grafo().generaGephi(bfs_mendes500, "mendesBFS500")


repo = 'https://github.com/JulioHaro93/GraphsModels/BFS_DFS'

print("repositorio", repo)
