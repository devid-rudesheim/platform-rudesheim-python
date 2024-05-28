import pathlib as pl

class OS:
	@classmethod
	def name( this ):
		return "Linux"

	@classmethod
	def os_by_name( this, system_name ):
		os_dicitionary = {}
		for i in OS.__subclasses__():
			os_dicitionary[ i.name() ] = i

		return os_dicitionary.get( system_name, OS )

	@classmethod
	def path( this ):
		return pl.PosixPath
