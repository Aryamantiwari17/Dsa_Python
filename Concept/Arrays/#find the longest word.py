#find the longest word

def find_The_larges(string):
    count=0
    maximum=0
    for char in string:
        if char.isalnum():
            count+=1
            
        else:
            maximum=max(maximum,count)
            count=0
    maximum=max(maximum,count)
    return maximum

string="hello thi saryaman"
print(find_The_larges(string))              

