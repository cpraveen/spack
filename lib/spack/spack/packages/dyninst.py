from spack import *

class Dyninst(Package):
    homepage = "https://paradyn.org"
    url      = "http://www.dyninst.org/sites/default/files/downloads/dyninst/8.1.2/DyninstAPI-8.1.2.tgz"
    md5      = "bf03b33375afa66fe0efa46ce3f4b17a"
    list_url = "http://www.dyninst.org/downloads/dyninst-8.x"

    depends_on("libelf")
    depends_on("libdwarf")

    def install(self, prefix):
        configure("--prefix=%s" % prefix)
        make()
        make("install")
