# E.Cloudmesh.Common.4
## Develop a program that demonstartes the use of cloudmesh.common.Shell.

from cloudmesh.common.Shell import Shell

class Homework:
    def getCurrentDirectory(self):
        return Shell.execute('pwd')


homework = Homework()

directory = homework.getCurrentDirectory()

print(directory)
