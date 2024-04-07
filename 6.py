x=[3,6,9,5]
y=[8,0,2,1]

Matching_Elements_1=[x for x in x if x in y]
Matching_Elements_2=[y for y in y if y in x]
print(Matching_Elements_1)
print(Matching_Elements_2)