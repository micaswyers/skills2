"""Write a function that takes an iterable 
(something you can loop through, ie: string, list, or tuple) 
and produces a dictionary with all distinct elements as the keys, 
and the number of each element as the value"""

def count_unique(some_iterable):
    if isinstance(some_iterable,str):
        unique_elements = some_iterable.lower().split(" ")
    else:
        unique_elements = some_iterable

    elements_count = {}
    for element in unique_elements:
        elements_count[element] = elements_count.get(element, 0) +1

    return elements_count

print "Dictionary of all distinct values from iterable:", count_unique([1,2,3,3,3,3,4,5])

"""Given two lists, (without using the keyword 'in' or the method 'index') 
return a list of all common items shared between both lists"""
def common_items(list1, list2):
    list3 = []
    i=0

    while i <= len(list1)-1:
        j = 0
        while j <= len(list2)-1:
            if list1[i] == list2[j]:
                list3.append(list1[i])
                break
            j+=1

        i+=1

    return list3


list1 = [1,2,3,4,5,2]
list2 = [2,3,4,5,6]

print "Common items from both lists:", common_items(list1,list2)
    

"""Given two lists, (without using the keyword 'in' or the method 'index') 
return a list of all common items shared between both lists. 
This time, use a dictionary as part of your solution."""
def common_items2(list1, list2):
    d=count_unique(list1)
    list3 = []

    i = 0
    while i <= len(list2)-1:
        d[list2[i]] = d.get(list2[i],0) 
        if d[list2[i]] != 0:
            list3.append(list2[i])
        i+=1
    return list3

list1 = [1,2,3,4,5,2]
list2 = [2,3,4,5,6]

print "Now using dictionaries:", common_items2(list1,list2)



