
from node import Node
from rack import Rack

class Regneklynge:
	def __init__(self, noderPerRack):
		self._regneklynge= []
		self._noderPerRack=noderPerRack


	def settInnNode(self, node):
		ikke_lagt_til=True
		if not self._regneklynge:
			nyRaq=Rack()
			self._regneklynge.append(nyRaq)
		for raq in self._regneklynge:
			if int(raq.getAntNoder())<int(self._noderPerRack):
				raq.settInn(node)
				ikke_lagt_til=False

		if ikke_lagt_til:
			nyRack=Rack()
			nyRack.settInn(node)
			self._regneklynge.append(nyRack)
			ikke_lagt_til=True

	def antProsessorer(self):
		total=0
		for regne in self._regneklynge:
			antallen=regne.antProsessorer()
			total+=antallen
		return total


	def noderMedNokMinne(self, paakrevdMinne):
		totalen=0
		for regne in self._regneklynge:
			intervaller=regne.noderMedNokMinne(paakrevdMinne)
			totalen+=intervaller
		return totalen


	def antRacks(self):
		return len(self._regneklynge)
