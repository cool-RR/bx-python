from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext

scripts = open( "scripts.list" ).read().split()
all_packages = open( "packages.list" ).read().split()
py_packages = [ p[:-3] for p in all_packages if p.endswith( ".py" ) ]
packages = [ p for p in all_packages if not p.endswith( ".py" ) ]

UCSC_CVS="/home/james/projects/ucsc-genome-cvs/"
JK_LIB= UCSC_CVS + "kent/src/lib/"
JK_INC= UCSC_CVS + "kent/src/inc/"

bitset_deps = 'bits.c', 'common.c', 'memalloc.c', 'dlist.c', 'errabort.c', 'osunix.c', 'wildcmp.c'

setup(  name = "python-bio-tools",
        py_modules = py_packages,
        packages = packages,
        scripts = open( "scripts.list" ).read().split(),
        ext_modules=[ Extension( "bx.bitset", [ "bx/bitset.pyx", "src/binBits.c" ] + [ JK_LIB + f for f in bitset_deps ], include_dirs=[JK_INC, "src"] ) ],
        cmdclass = {'build_ext': build_ext}
     )
