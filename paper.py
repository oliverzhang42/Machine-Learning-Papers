

class Paper:
    def __init__(self, paper_id, title, inputs=[], outputs=[]):
        self.id = paper_id
        self.title = title

        assert type(inputs) == list, "Inputs must be a list of papers!"
        assert len(inputs) == 0 or type(inputs[0]) == Paper, "Inputs must be a\
                                                              list of papers!"

        self.inputs = inputs

        assert type(outputs) == list, "Outputs must be a list of papers!"
        assert len(outputs) == 0 or type(outputs[0]) == Paper, "Outputs must \
                                                          be a list of papers!"
        self.outputs = outputs

    def set_inputs(self, inputs):
        self.inputs = inputs

    def set_outputs(self, outputs):
        self.outputs = outputs

    def display(self, current_depth, max_depth, forward=True):
        '''
        Default is to display the papers which have cited you (outputs).
        '''
        if current_depth <= max_depth:
            indent = '    '
            print(current_depth * indent + self.title)
            
            if forward:
                for p in self.outputs:
                    p.display(current_depth+1, max_depth, forward=True)
            else:
                for p in self.inputs:
                    p.display(current_depth+1, max_depth, forward=False)
