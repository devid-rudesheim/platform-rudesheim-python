#!/opt/homebrew/bin/python3

import rudesheim.platform as pf
import unittest as ut


class PlatformTests( ut.TestCase ):


	def test_0_0( this ):
		os = pf.linux.OS
		this.assertEqual( os, pf.OS.os_by_name( os.name() ) )

	def test_0_1( this ):
		os = pf.mac.OS
		this.assertEqual( os, pf.OS.os_by_name( os.name() ) )

	def test_0_2( this ):
		os = pf.windows.OS
		this.assertEqual( os, pf.OS.os_by_name( os.name() ) )

	def test_1( this ):
		this.assertEqual( "file.name", pf.OS.path()( "/file.name" ).name )

ut.main()
