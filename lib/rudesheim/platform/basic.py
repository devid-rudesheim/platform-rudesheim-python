import pathlib as pl

class OS:
	@classmethod
	def name( this ):
		return "Linux"

	@classmethod
	def os_by_name( this, system_name ):
		return { i.name() : i for i in OS.__subclasses__() }.get( system_name, OS )

	@classmethod
	def path( this ):
		return pl.PosixPath
