# 
# The objective of this file is to merge both arxiv_query and semantic_query
# into one file which uses the newly created DAG object.
#
# 1. Semantic Query first.
#    a. Construct forward/backward tree of depth.
#    b. Make sure to not repeat any.
#
# 2. Then try ArXiv.
#
#

import json
from paper import Paper
import urllib.request 

class Query:
    def __init__(self):
        self.tries = 5
        self.semantic_base = "https://api.semanticscholar.org/v1/paper/{}"
        self.arxiv_base = ""

    def query_link(self, url):
        for i in range(self.tries):
            try: 
                data = urllib.request.urlopen(url).read()                               
            except Exception as e:
                print("Something went wrong!")
                print(e)
                print("Trying again...")
                print()  

        if not ('data' in locals()):
            print("After {} tries, it didn't work. \
                   Quitting...".format(self.tries))
            raise Exception("")

        return json.loads(data)
 
    def query_semantic_scholar(self, start, depth, forward=True):
        '''
        paper (str): The DOI, ArXiv ID, S2 Paper ID, Corpus ID, or any other
        ID which semantic scholar uses to identify papers. See
        https://api.semanticscholar.org/ for more details. 

        1. Set up the for loop
        2. In each iteration:
            a. Query to get the json object
            b. Create a DAG object
            c. Add to library
        
        3. Do a second for loop for the connections.
        '''

        start_id = ""
        repeated = []
        library = {}
        connections = {}

        current_layer = [start]                                                                  
        next_layer = []                                                                   
        
        for i in range(depth):                                                          
            for p in current_layer:
                if p not in repeated:                                    
                    repeated.append(p)
                    url = self.semantic_base.format(p)                                                    
                    json_obj = self.query_link(url)                                     
                                                                                        
                    # Log the title and identity in "library"                               
                    identity = json_obj['paperId']                                             
                    if len(start_id) == 0:
                        start_id = identity
                    title = json_obj['title']                                                  
                    library[identity] = Paper(identity, title)
                                                                                            
                    # Log the refs/citations in connections and add all ref to 
                    # "next_layer"             
                    # Also, add all identities to the library.                              
                    connections[identity] = []

                    if forward:
                        citations = json_obj['citations']
                        for cite in citations:
                            cite_id = cite['paperId']
                            connections[identity].append(cite_id)
                            next_layer.append(cite_id)
                            
                            library[cite_id] = Paper(cite_id, cite['title'])
                            connections[cite_id] = []
                    else:
                        references = json_obj['references']                                        
                        for r in references:                                                    
                            ref_id = r['paperId']                                               
                            connections[identity].append(ref_id)                                       
                            next_layer.append(ref_id)                                             
                                                                                                
                            library[ref_id] = Paper(ref_id, r['title'])
                            connections[ref_id] = []                                        
                                                                                            
            current_layer = next_layer                                                   
            next_layer = []
        
        current_layer = [library[start_id]]
        next_layer = []

        # HMM I'm not sure how to do the connections rn...
        for id_ in library:
            c_ = connections[id_]
            new_c = []
            
            for c in c_:
                obj = library[c]
                new_c.append(obj)

            dag_obj = library[id_]
            if forward:
                dag_obj.set_outputs(new_c)
            else:
                dag_obj.set_inputs(new_c)

        return library[start_id]
