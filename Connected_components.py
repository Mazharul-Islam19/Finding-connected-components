file = 'testcomp.graph'
adj_list = {}
data = []
with open(file) as f:
    for line in f:
        line = line.strip("\n")
        data.append(line)
    num_of_vertices = int(data[0].split()[0])
    num_of_edges = int(data[0].split()[1])
    if data[0].split()[2] == '0':
        Weighted = False
    data.pop(0)
    data = data[:num_of_vertices]
    for i in range(1,len(data)+1):
        adj_list[i] = data[i-1].split()

Visited = {}
for i in adj_list:
    Visited[i] = False

Comp = {}

i = 0
for v in adj_list:
    if Visited[int(v)] == False:
        i += 1
        Comp[i] = []
        def DFS(v):
            Visited[int(v)] = True
            Comp[i].append(v)
            for e in adj_list[int(v)]:
                if Visited[int(e)] == False:
                    DFS(e)
            return Comp
        DFS(v)

Output = open('Components.csv','w+')
for i,j in Comp.items():
    k = str([int(k) for k in j]).lstrip("[").rstrip("]")
    c = str(i) + " : " + k + "\n"
    Output.write(c)
Output.close()