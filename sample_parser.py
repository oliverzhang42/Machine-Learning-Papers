import json

if __name__ == '__main__':
    with open("sample-S2-records") as f:
        str_ = f.read().replace("\n", "")
        str_ = str_.replace("}{", "}\n{")
        a = str_.split("\n")
    
    a2 = []

    for s in a:
        d = json.loads(s)
        a2.append(d)

    import pudb; pudb.set_trace()

