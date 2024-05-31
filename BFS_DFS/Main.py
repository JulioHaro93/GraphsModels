import graphs as grafo
from queue import Queue as que
from graphs import Grafo as Grafo
import dijkstra as dk

grafoMalla30 = Grafo.grafoMalla(Grafo,30,2)
dk.dijkstra(grafoMalla30)