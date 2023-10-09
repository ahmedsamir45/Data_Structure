def add_node(v):

    global node_count

    if v in nodes:
        print(v,'is already pressent in the graph' )

    else:
        node_count = node_count+1
        nodes.append(v)

        for n in graph:
            n.append(0)

            
        temp = []

        for i in range(node_count):
            temp.append(0)

            
        graph.append(temp)



def add_edge(v1,v2):
    if v1 not in nodes :
        print(v1,'is not pressent in the graph')
    elif  v2 not in nodes:
        print(v2,'is not pressent in the graph')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1




def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=' ')
        print()

nodes = []
graph = []

node_count = 0

add_node('el maadi')
add_node('dar el salam')
add_node('helwan')
add_node('el basaten')

add_edge('el maadi','dar el salam')
add_edge('el maadi','helwan')
add_edge('helwan','dar el salam')
add_edge('helwan','el basaten')
add_edge('el basaten','dar el salam')
print(graph)
print_graph()
















            

            
