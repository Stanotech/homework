list1 = [1, 2, 3, 4, 5, 34, 2, 3]

set1 = {1, 2, 3, 4, 5, 34, 2, 3}
set2 = {3, 4, 5, 8, 77, 54}

dict1 = {
    'apple': 1,
    'banana': 2,
    'orange': 3,
    'grape': 4,
    'watermelon': 5,
    'kiwi': 6,
    'strawberry': 7,
    'blueberry': 8,
    'pineapple': 9,
    'mango': 10
}

dict2 = {
    'apple': 1111,
    'ds': 2,
    'dsa': 3,
    'grape': 4,
    'gfdh': 5,
    'kiwi': 6,
    'fdgsd': 7,
    'blueberry': 8,
    'pineapple': 9,
    'mango': 999
}


tuple1 = (1, 2, 3, 1, 4, 5, 6, 2, 2, 6, 4, 2, 5, 4, 4, 4, 3)


class Set:
    def symmetric_difference(set1, set2):
        return [elem for elem in set1 if elem not in set2] + [elem for elem in set2 if elem not in set1]

    def issubset(set1, set2):
        return set1 in set2
    
    def is_superset(set1, set2):
        return set1.issuperset(set2)
    
    def clear(set):
        return ()
    
    def copy(set):
        return set.copy()

class Dict:
    def key_list(dict1):
        return list(dict1.keys())
    
    def exist(dict1, name):
        return any(["true" for key in dict1.keys() if name == key])
    
    def length(dict):
        return len(dict.keys())
    
    def update(dict1, dict2):
        for key in dict2.keys():           
            dict1[key] = dict2[key]
        return dict1

    def delete(dict, key):
        del dict[key]
        return dict
    
    def delete_return(dict, key):
        value = dict[key]
        del dict[key]
        return value


class Tuple:
    def count(tuple, elem):
        return sum([1 for num in tuple if num == elem])
    
    def index(tuple, elem):
        for num, idx in enumerate(tuple):
            if num == elem: 
                return idx
            
    def slice(tuple, ind1, ind2):
        return tuple[ind1:ind2]
    
    def reverse(tuple):
        return tuple[::-1]
    
    def exist(tuple, elem):
        return elem in tuple
    
    def totuple(list):
        return tuple(list)

    
# print(set1.symmetric_difference(set2))
# print(Set.symmetric_difference(set1, set2))

# print(Dict.key_list(dict1))

# print(Tuple.count(tuple1, 2))
# print(tuple.count(2))

# print(Set.issubset(set1, set2))
# print(set1.issubset(set2))

# print(Tuple.index(tuple1, 6))
# print(tuple.index(6))

# print("mango" in dict1)
# print(Dict.exist(dict1, "mango"))

# print(Tuple.slice(tuple1, 1, 4))

# print(Set.is_superset(set1, set2))

# print(Dict.length(dict1))

# print(Tuple.reverse(tuple1))

# print(Dict.update(dict1, dict2))

# print(Tuple.exist(tuple1, 6))

# print(Set.clear(set1))

# print(Dict.delete(dict1, "apple"))

# print(Tuple.totuple(list1))

# new_set = Set.copy(set1)
# print(new_set)

# print(Dict.delete_return(dict1, "apple"))



# Write a function that takes two sets as input and updates the first set with elements that are also present in the second set.
# Write a function that takes two sets as input and updates the first set with elements that are also present in the second set.