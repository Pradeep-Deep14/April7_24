#Nested List to Flattened List

def Flattened_List(Lst):
    Flattened=[]
    for i in Lst:
        if isinstance(i,list):
            Flattened.extend(i)
        else:
            Flattened.append(i)
    return Flattened


L=[1,2,3,[4,5],[6,7],8]
print(Flattened_List(L))