import platform as pf
from . import basic

class OS( basic.OS ):
	@classmethod
	def name( this ):
		return "Windows"

	@classmethod
	def path( this ):
		return pl.WindowsPath
