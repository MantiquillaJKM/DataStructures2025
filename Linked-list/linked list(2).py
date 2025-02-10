Body_Parts1 = {'data': "head", 'next': None}
Body_Parts2 = {'data': "shoulders", 'next': None}
Body_Parts3 = {'data': "knees", 'next': None}
Body_Parts4 = {'data': "toes", 'next': None}

Body_Parts1['next'] = Body_Parts2
Body_Parts2['next'] = Body_Parts3
Body_Parts3['next'] = Body_Parts4

current = Body_Parts1
while current:
    print(current['data'], end= ">")
    current = current['next']
print("None")

