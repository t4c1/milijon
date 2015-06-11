# distutils: language = c++
import sys
sys.path.append(r"C:\Program Files (x86)\Python26\Lib\site-packages\Cython\Includes")
sys.path.append(r"C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools")
sys.argv.extend(["build_ext","--inplace"])

from distutils.core import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext
from distutils.extension import Extension

print sys.version

ext = [Extension(
            "cMilijon",
            ["cMilijon.pyx"],#, "pathfinding.cpp"],
            language="c++",
            ##extra_compile_args=["-O2"],
            #extra_link_args=["-debug"],
            #include_path=[r"C:\Program Files (x86)\Python26\Lib\site-packages\Cython\Includes\libcpp"],
             )]
"""
ext=cythonize(
            "cPathfinding.pyx",
            sources=["cPathfinding.pyx", "pathfinding.cpp"],
            language="c++",
            extra_compile_args=["-Zi", "/Od"],
            extra_link_args=["-debug"],
            include_path=[r"C:\Program Files (x86)\Python26\Lib\site-packages\Cython\Includes\libcpp"],)
"""

def do_test():
    import render
    render.test()


try:
    setup(
        name = 'cMilijon',
        cmdclass = {'build_ext': build_ext},
        ext_modules = ext
    )
    do_test()
except BaseException,err:
    print type(err),err
    if "mt" in str(err):
        do_test()
finally:
    pass