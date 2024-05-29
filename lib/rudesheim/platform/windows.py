from . import basic as rb
import pathlib as pl

class OS( rb.OS ):
	@classmethod
	def name( this ):
		return "Windows"

	@classmethod
	def path( this ):
		return pl.WindowsPath
