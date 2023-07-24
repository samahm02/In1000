from node import Node

class Rack:
	def __init__(self):
		self._liste=[]

	def settInn(self, node):
		self._liste.append(node)

	def getAntNoder(self):
		return len(self._liste)

	def antProsessorer(self):
		total=0
		for node in self._liste:
			prosessorer=node.antProsessorer()
			total+=prosessorer
		return total

	def noderMedNokMinne(self, paakrevdMinne):
		antallGode=0
		for node in self._liste:
			if node.nokMinne(paakrevdMinne) == True:
				antallGode +=1
		return antallGode
