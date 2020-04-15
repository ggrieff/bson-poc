# bson-poc
Simple Python project to take a Mongodb dump bson format and produce a json output.

File zips.bson is a dump of a mongo table containing US zipcode information

The code reads in zips.bson and outputs zips.json

Sample output
[
  {
    "_id": "01001",
    "city": "AGAWAM",
    "loc": [
      -72.622739,
      42.070206
    ],
    "pop": 15338,
    "state": "MA"
  },
  {
    "_id": "01002",
    "city": "CUSHMAN",
    "loc": [
      -72.51565,
      42.377017
    ],
    "pop": 36963,
    "state": "MA"
  },
  {
    "_id": "01005",
    "city": "BARRE",
    "loc": [
      -72.108354,
      42.409698
    ],
    "pop": 4546,
    "state": "MA"
  },
