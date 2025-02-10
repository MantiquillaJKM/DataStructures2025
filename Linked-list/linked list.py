node1 = {'data': 10, 'next': None}
node2 = {'data': 20, 'next': None}
node3 = {'data': 30, 'next': None}
node4 = {'data': 40, 'next': None}

node1['next'] = node2
node2['next'] = node3
node3['next'] = node4

current = node1
while current:
    print(current['data'], end=" -> ")
    current = current['next']
print("None")