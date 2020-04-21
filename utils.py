import pickle as pkl

def save(obj, name):
    with open(name, "wb") as f:
        pkl.dump(obj, f)

def load(name):
    with open(name, "rb") as f:
        return pkl.load(f)
