#!/usr/bin/env python
# _*_ coding: utf8 _*_

import random
import string
class Nodo:
    
    def __init__(self, idson, pos):
        self.idson = idson
        self.aristas_salientes = []
        self.pos= pos
        self.aristas_posibles = 0
        self.valorEquis = 0
        self.valorYe =0

    def agregar_arista_saliente(self, arista):
        self.aristas_salientes.append(arista)


class Arista:
    def __init__(self, origen, destino, grado = 1):
        self.origen = origen
        self.destino = destino
        self.grado = grado


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
        origen.agregar_arista_saliente(arista)

    def grado_nodo(self, nodo):
        return len(nodo.aristas_salientes)
    def generaId(self):
        idcitoBb= "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(25)
            )
        #print(idcitoBb)
        return idcitoBb

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
                    self.aristas.append(arista)
                    #print(arista)
                    
                if i<m-1:
                    if (nodos[i][j].idson == nodos[i+1][j].idson):
                        nodos[i+1][j].idson = self.generaId()
                    arista = Arista(nodos[i][j], nodos[i+1][j])
                    self.aristas.append(arista)
                if(i<m-2 and j < n-2):
                    if(nodos[i][j].idson==nodos[i+1][j+1]):
                        nodos[i+1][j+1].idson = self.generaId()
                    arista = Arista(nodos[i][j], nodos[i+1][j+1])
                if(i<m-1 and j<n-1):
                    
                    print(str(nodos[i][j].pos)+'--------'+ str(nodos[i][j+1].pos) +'\n|\n|\n|\n|\n'+str(nodos[i+1][j].pos))
                j+=1
            i+=1
        grafito = Grafo()
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
                                print("se enlazó"+ str(nodos[x].pos) +"#######"+ str(nodos[numerillo].pos) )
                                nodos[numerillo].aristas_posibles +=1
                                nodos[x].aristas_posibles += 1
        grafillo = Grafo()
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
            #print(nodo)
        i=0;j=0
        nodos2 = nodos
        for i in range(len(nodos)):
            for j in range(len(nodos2)):
                if(nodos[i].pos != nodos2[j].pos):
                    if(p > random.random()):
                        arista = Arista(nodos[i], nodos2[j])
                        self.agregarArista(nodos[i], nodos2[j])
                        print("se enlazó "+str(arista.origen.pos)+"-------"+ str(arista.destino.pos))
            j+=1
        i+=1
        grafito = Grafo()
        return grafito

        pass

    def grafoGeografico(self,n, r, dirigido=False):
        """
        Genera grafo aleatorio con el modelo geográfico simple
        :param n: número de nodos (> 0)
        :param r: distancia máxima para crear un nodo (0, 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        pass

    def grafoBarabasiAlbert(self,n, d, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (> 0)
        :param d: grado máximo esperado por cada nodo (> 1)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        pass

    def grafoDorogovtsevMendes(self,n, dirigido=False):
        """
        Genera grafo aleatorio con el modelo Barabasi-Albert
        :param n: número de nodos (≥ 3)
        :param dirigido: el grafo es dirigido?
        :return: grafo generado
        """
        pass

Grafo().generaId()

Grafo().grafoMalla(10,4, False)
Grafo().grafoErdosRenyi(30,4, False)
Grafo().grafoGilbert(20,0.2,False)