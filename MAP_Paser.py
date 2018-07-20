# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 18:02:03 2018

@author: AJ
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64, json

#expr = "Y=[2010,2012]"
expr = "Composite(J.JN='journal of machine learning research')"
count = 100000
attributes = "Id,Ti,L,Y,D,CC,ECC,AA.AuN,AA.AuId,AA.AfN,AA.AfId,AA.S,F.FN,"\
             "F.FId,J.JN,J.JId,C.CN,C.CId,RId,W,E,DN,S,S.Ty,S.U,VFN,VSN,V,"\
             "BV,BT,PB,I,FP,LP,DOI,CC,IA,IA.IndexLength,IA.InvertedIndex"
body = "expr=%s&count=%i&attributes=%s"% (expr, count, attributes)
headers = {
    # Request headers
    'Content-Type': 'application/x-www-form-urlencoded',
    'Ocp-Apim-Subscription-Key': 'd55c10f35b904c358b9f86a9c0dc10c7',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
    conn.request("POST", "/academic/v1.0/evaluate?%s" % params, body, headers)
    response = conn.getresponse()
    data = json.loads(response.read())
    print(data)
    conn.close()
    #with open('data.json', 'w') as outfile:  
    #    json.dump(data, outfile)
    #f = open("write.json", "w")
    #f.write(data)
    with open("write.json", "w") as f:
        json.dump(data,f,indent=4,sort_keys=True)    
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))