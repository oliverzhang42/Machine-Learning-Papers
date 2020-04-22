#
# 1. Simple pruning using citation counts
#
# 2. Pruning using percentages
#    a. Calculate the total number of nodes
#    b. Get the citation numbers
#    c. Build a map from percentage to citation pruning and use #1.
#
# 3. Be sure that this is all reversible and able to be applied to both the
#    citations as well as the references.
#

def prune_by_number(dag, threshold, forward=True):
    '''
    prunes a DAG by removing all elements which don't satisfy a certain
    threshold of citations/references.

    (Paper) dag: the start of the DAG which you want to prune.
    (int) threshold: the threshold value of citations/references
    (bool) forward: if true, then pruning based on citations, if false, then 
                    pruning based on references. 
    
    returns: (Paper) dag, the DAG after pruning.
    '''

    if forward:
        children = dag.outputs
    else:
        children = dag.inputs

    remaining = []

    for paper in children:
        if forward:
            if len(paper.outputs) >= threshold:
                remaining.append(paper)
        else:
            if len(paper.inputs) >= threshold:
                remaining.append(paper)

    for i in range(len(remaining)):
        p = prune_by_number(remaining[i], threshold, forward=forward)
        remaining[i] = p

    if forward:
        dag.outputs = remaining
    else:
        dag.inputs = remaining

    return dag


def prune_by_percentage(dag, keep_percent, forward=True):
    '''
    prunes a DAG by keeping only keep_percent of the nodes.
    '''
    pass
