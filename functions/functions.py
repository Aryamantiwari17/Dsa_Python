str_num=['1','2','3','4','5']
int_num=list(map(int,str_num))

words=["apple","banana","cheery"]

upper_word=list(map(str.upper,words))
print(upper_word)


def get_name(person):
    return person['name']
people=[
        {"name":"John","age":30},
        {"name":"Joh","age":25}
        
        
    ]
x= list(map(get_name,people))
print(x)