import json
import pymongo
import codecs
#json.load(codecs.open('sample.json', 'r', 'utf-8-sig'))
con=pymongo.MongoClient()
db=con.pp
#rec=db.collection
rec=db.social_feeds
#page=open("filename.json","r")
#parsed=json.loads(page.read())   
parsed=json.load(codecs.open('codebeautify9.json', 'r', 'utf-8-sig'))
print(parsed["rss"]["channel"]["item"])
for item in parsed["rss"]["channel"]["item"]:
    #print(item)
    rec.insert(item)


