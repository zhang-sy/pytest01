def read_txt():
    with open('../Data/data02.txt','r',encoding='utf-8') as f:
        arrs = []
        for line in f.readlines():
            arrs.append(tuple(line.strip().split(",")))
            return arrs
