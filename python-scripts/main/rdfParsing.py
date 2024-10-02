import rdflib

class thesaurusRdf():     
    def __init__(self, thesaurus, format='xml'): 
        self.myfile = thesaurus
        self.g = rdflib.Graph()
        self.format=format
        self.g.parse(self.myfile, self.format)    
    def findPrefLabel(self,uri,language):#language codé en ISO 2
        self.uri=uri
        self.prefLabel = None 
        self.language=language
        self.req2="""
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    SELECT ?label
                    WHERE {
                       ?uri skos:prefLabel ?label .
                       FILTER (lang(?label) = "{}")
                    }
                    """.replace('{}',self.language)

        self.look4uri = rdflib.URIRef(self.uri)


        self.qres2 = self.g.query(self.req2, initBindings={"uri": self.look4uri})
        for row in self.qres2:
            self.prefLabel=row.label
            
    def findURI(self, prefLabel, language):#language codé en ISO 2
        self.prefLabel=prefLabel
        self.language=language
        self.req2="""
                    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
                    SELECT ?uri
                    WHERE {
                       ?uri skos:prefLabel ?label .
                       FILTER (lang(?label) = "{}")
                    }
                    """.replace('{}',self.language)

        self.look4uri = rdflib.URIRef(self.uri)


        self.qres2 = self.g.query(self.req2, initBindings={"uri": self.look4uri})
            
    
    

