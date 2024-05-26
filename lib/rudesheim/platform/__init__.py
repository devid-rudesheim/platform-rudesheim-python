import pathlib as pl
import platform as pf

class OS:
	@classmethod
	def current( this ):
		return this.implement_

	@classmethod
	def update( this, system_name ):
		os_dicitionary = {}
		for i in OS.__subclasses__():
			os_dicitionary[ i.name() ] = i

		this.implement_ = os_dicitionary.get( system_name, Linux )

	@classmethod
	def name( this ):
		return "Linux"

	@classmethod
	def path( this ):
		return pl.PosixPath

class Linux( OS ):
	pass

class Mac( OS ):
	@classmethod
	def name( this ):
		return "Darwin"

class Windows( OS ):
	@classmethod
	def name( this ):
		return "Windows"

	@classmethod
	def path( this ):
		return pl.WindowsPath

OS.update( pf.system() )
