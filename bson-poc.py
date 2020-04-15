import bson
import json

i = open ('./zips.bson','rb')
data = bson.decode_all(i.read())
i.close()

o = open ('./zips.json','w')
o.write(json.dumps(data))
o.close()


