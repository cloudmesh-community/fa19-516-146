
# E.Cloudmesh.Common.2
## Develop a program that demonstartes the use of dotdict.

from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.debug import VERBOSE

data = {
    "first": "Kenneth",
    "last": "Jones",
    "campuses":[
        "Bloomington",
        "Indianapolis",
    ]
}
data = dotdict(data)

VERBOSE(data)
VERBOSE(data.first)
VERBOSE(data.last)
VERBOSE(data.campuses)