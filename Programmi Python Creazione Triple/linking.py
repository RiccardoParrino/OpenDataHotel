import re, math
from collections import Counter
import json
import os
path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)) )

def text_to_vector(text):
    text = text.lower();
    words =  re.compile(r'\w+').findall(text)
    return Counter(words)

def get_cosine(text1, text2):
    vec1 = text_to_vector(text1)
    vec2 = text_to_vector(text2)
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    
    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator;

def link ( label ):
    data = json.load( open( path + "/Sparql-OpenStreetMap Query/queryLocation.json", "r" ) );
    maxCosine = 0;
    uriMax = "";
    for result in data["results"]["bindings"]:
        uriQuery = result["thing"]["value"];
        labelQuery = result["label"]["value"];
        cosine = get_cosine( label, labelQuery );
        #print(cosine)
        if ( cosine > maxCosine and cosine > 0.7 ):
            maxCosine = cosine;
            uriMax = uriQuery;
    
    data = json.load( open( path + "/Sparql-OpenStreetMap Query/queryPosition.json", "r" ) );
    for result in data["results"]["bindings"]:
        uriQuery = result["resource"]["value"];
        labelQuery = result["label"]["value"];
        cosine = get_cosine( label, labelQuery );
        if ( cosine > maxCosine and cosine > 0.7 ):
            maxCosine = cosine;
            uriMax = uriQuery;
        
    return uriMax;




