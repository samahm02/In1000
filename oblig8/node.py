
class Node:
	def __init__(self, minne, antPros):
		self._minne=minne
		self._antPros=antPros

	def antProsessorer(self):
		return self._antPros

	def nokMinne(self, paakrevdMinne):
		self._paakrevdMinne=paakrevdMinne
		if self._minne >= self._paakrevdMinne:
			return True
		else:
			return False
