# E.Cloudmesh.Common.5
## Develop a program that demonstartes the use of cloudmesh.common.StopWatch.

from cloudmesh.common.StopWatch import StopWatch
from time import sleep
import sys

StopWatch.start("1")
for _ in range(0,10):
    sleep(0.3)
    sys.stdout.write('.')
print('done')
StopWatch.stop("1")

print (StopWatch.get("1"))
StopWatch.benchmark()