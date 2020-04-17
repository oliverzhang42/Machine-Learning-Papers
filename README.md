# Machine-Learning-Papers

## Current Status

All work right now can be considered prototyping. A list of files include:

### 1. ArXiv Querying:
Currently have a file, ```arxiv_query.py``` which queries arXiv. Doesn't do 
much beyond that.

### 2. Semantic Scholar Parsing:
The file ```sample_parser.py``` parses the file ```sample-S2-records```, which 
is a sample of the larger Semantic Scholar dataset. Current efforts of parsing
this are very rudimentary, but it's my starting point if I end up trying to 
parse all the data.

### 3. Semantic Scholar Querying:
The file ```semantic_query.py``` queries the Semantic Scholar databases and 
parses the data.

## Planned Structure
The structure of this tool will be divided up into three layers, parsing data, 
pruning the DAG, and displaying papers. To run anything, there should be
```main.py```. (TODO)

### 1. Parsing Data
Objective: get the data and return it as a DAG object. Options include querying
from either ArXiv or Semantic Scholar, loading local files (for debugging), or 
mining Semantic Scholar's datadump.

Files:
```dag.py```: File containing the DAG object. (TODO)
```query.py```: File containing functions which query both Semantic Scholar and
ArXiv. (Also contains a function which loads local files.) (TODO)
(Right now I'm not planning to mine the datadump, but it's always an option.) 

### 2. Pruning DAG
Objective: prune/process the DAG. Could be for limiting the number of papers 
displayed based on importance or for trying to understand clusters of papers
within the knowledge graph.

Files:
```prune.py```: Functions for pruning the DAG based on importance. Depending
on memory, some of this functionality may need to be moved to section 1. I 
envision both pre-pruning to reduce the size of the DAG but also this
post-pruning so the viewer can determine how much detail they want. (TODO)
```process.py```: Algorithms to process the DAG. If doing data analysis, the 
pipeline stops here, as there's nothing to display. (TODO)

### 3. Displaying Papers
Objective: Display the DAG. Should support both a basic printing display as
well as a more complex Tkinter graphics display.

Files:
```print_display.py```: Functions for printing the DAG via commandline. (TODO)
```visual_display.py```: Functions for displaying the DAG via tkinter. 
Eventually, I want this to be a website which uses Javascript for the ability
to interact. However, the prototype should be in tkinter. (TODO)

## Acknowledgements:
The semantic scholar data is from https://www.semanticscholar.org/.
