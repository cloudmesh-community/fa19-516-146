# E.Cloudmesh.Common.1
## Develop a program that demonstartes the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

class Homework:
    def showBanner(self, msg):
        banner(msg)
    def showHeader(self, msg=None):
        HEADING(msg)
    def printDebug(self):
        VERBOSE(self)


homework = Homework()

homework.showBanner("This is my banner")
homework.showHeader()
homework.showHeader("Here is a header with a message")

homework.printDebug()

VERBOSE(homework)
VERBOSE({"title":"Printing a map"})