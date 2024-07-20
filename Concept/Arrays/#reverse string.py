#reverse string

def string_rev(arr):
    new_arr=[]
    for i in range (len(arr)-1,-1,-1):
        new_arr.append(arr[i])
    return ''.join (new_arr)

arr="98494"
print("new array",string_rev(arr))

#reverse string


def swap(string,a,b):
    string=list(string)
    temp=string[a]
    string[a]=string[b]
    string[b]=temp
    return ''.join(string)
def rever(string):
    for i in range (len(string)//2):
        string=swap(string,i,len(string)-i-1)
    return string

string="123"
print(rever(string))

#3approach built in finction using  reverse