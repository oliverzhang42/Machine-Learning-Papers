import argparse
from query import Query


if __name__ == '__main__':
    parser = argparse.ArgumentParser()     
    parser.add_argument('--forward', type=bool, default=True,                     
                        help='Whether to build the tree forwards or backwards')    
                                                                                
    args = parser.parse_args()

    import pudb; pudb.set_trace()

    q = Query()
    doi = "10.1080/00224490902775827"
    starting_node = q.query_semantic_scholar(doi, 2, forward=False)
    
    starting_node.display(0, 2, forward=False)
