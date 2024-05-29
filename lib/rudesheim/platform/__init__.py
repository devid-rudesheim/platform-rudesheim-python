from . import basic as rb
import platform as pf
from . import linux
from . import mac
from . import windows

OS = rb.OS.os_by_name( pf.system() ) 
