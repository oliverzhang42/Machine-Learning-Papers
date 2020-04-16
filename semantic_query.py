# FIRST SCRIPT!
#
# 1. Input a paper doi or arXiv thing as well as a depth (Done)
# 2. Write a function which builds a tree and a library (Done)
#    a. The tree contains the connections between the IDs
#    b. The library is a dictionary which goes from IDs to dictionary.
# 3. Build helper commands like get_name_tree which gets the tree (Done)
#    but the names instead of the IDs.
# 4. Find a way to deal with repeats. (Kinda Done?)

from copy import deepcopy
import json
import urllib.request


def display_name_tree(tree, library, starting):
    import pudb; pudb.set_trace()
    
    stack = [starting]
    indents = ""

    while(len(stack) > 0):
        elt = stack.pop()
        if elt == "endIndent":
            indents = indents[0:-4]
        else:
            print(indents + library[elt])
            
            if elt in tree and len(indents) < 8:
                indents = indents + "    "
                stack.append("endIndent")
                for p in tree[elt]:
                    stack.append(p)



start = input("Input a paper!\n")
depth = int(input("Input a depth!\n"))

base = "https://api.semanticscholar.org/v1/paper/{}"

library = {}
tree = {}

leaf = [start]
new_leaf = []

start_id = ""

import pudb; pudb.set_trace()

for i in range(depth):
    for l in leaf:
        # Load the paper
        url = base.format(l)
        data = urllib.request.urlopen(url).read()
        paper = json.loads(data)

        # Log the title and identity in "library"
        identity = paper['paperId']
        if len(start_id) == 0:
            start_id = identity
        title = paper['title']
        library[identity] = title

        # Log the ref graph in "tree" and add all ref to "new_leaf"
        # Also, add all identities to the library.
        tree[identity] = []
        references = paper['references']
        for r in references:
            ref_id = r['paperId']
            tree[identity].append(ref_id)
            new_leaf.append(ref_id)

            library[ref_id] = r['title']
    
    leaf = deepcopy(new_leaf)
    new_leaf = []

display_name_tree(tree, library, start_id)
