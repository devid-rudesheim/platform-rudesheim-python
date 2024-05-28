import platform as pf
from . import linux
from . import mac
from . import windows
from . import basic

OS = basic.OS.os_by_name( pf.system() ) 
