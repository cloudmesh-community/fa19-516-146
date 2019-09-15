# E.Cloudmesh.Common.3
# Develop a program that demonstartes the use of FlatDict.

from cloudmesh.common.FlatDict import FlatDict
from pprint import pprint

data = {
    "first": "Kenneth",
    "last": "Jones",
    "location": {
        "campus": "Bloomington"
    }
}

data = FlatDict(data)

pprint(data)
