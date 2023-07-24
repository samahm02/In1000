from node import Node
from rack import Rack
from regneklynge import Regneklynge
import os

class Datasenter:

	def __init__(self):
		self._datasenter={}


	def lesInnRegneklynge(self, filnavn):
		filnavnet = os.path.basename(filnavn)
		filnavna = filnavnet.split(".")
		filen = open(filnavn)
		interasjon = 0
		raqListe = []
		for linjer in filen:
			if interasjon == 0:
				noder_i_rack = linjer
			else:
				linjene = linjer.split()
				raqListe.append(linjene)
			interasjon += 1
		self._datasenter[filnavna[0]]=Regneklynge(noder_i_rack)
		verdi_a = 0
		verdi_b = 0
		for x in raqListe:
			while int(verdi_a) < int(raqListe[verdi_b][0]):
				nyNode = Node(int(raqListe[verdi_b][1]), int(raqListe[verdi_b][2]))
				self._datasenter[filnavna[0]].settInnNode(nyNode)
				verdi_a +=1
			verdi_a = 0
			verdi_b +=1


	def skrivUtAlleRegneklynger(self):
		for x in self._datasenter:
			self.skrivUtRegneklynge(x)
			print()

	def skrivUtRegneklynge(self, navn):
		print("Informasjon om regneklyngen " + navn)
		print("Antall rack: " + str(self._datasenter[navn].antRacks()))
		print("Antall prosessorer: " + str(self._datasenter[navn].antProsessorer()))
		print("Noder med minst 32 GB: " + str(self._datasenter[navn].noderMedNokMinne(32)))
		print("Noder med minst 64 GB: " + str(self._datasenter[navn].noderMedNokMinne(64)))
		print("Noder med minst 128 GB: " + str(self._datasenter[navn].noderMedNokMinne(128)))

def hovedprogram():
	datasenterert = Datasenter()
	datasenterert.lesInnRegneklynge("saga.txt")
	datasenterert.lesInnRegneklynge("abel.txt")
	datasenterert.skrivUtAlleRegneklynger()

hovedprogram()
