#!/opt/homebrew/bin/python3

import rudesheim.platform as pf
import unittest as ut


class PlatformTests( ut.TestCase ):

	def test_0( this ):
		this.assertEqual( "file.name", pf.OS.current().path()( "/file.name" ).name )

	def test_1( this ):
		os = pf.Linux
		pf.OS.update( os.name() )
		this.assertEqual( os, pf.OS.current() )

	def test_2( this ):
		os = pf.Mac
		pf.OS.update( os.name() )
		this.assertEqual( os, pf.OS.current() )

	def test_3( this ):
		os = pf.Mac
		pf.OS.update( os.name() )
		this.assertEqual( os, pf.OS.current() )

ut.main()
