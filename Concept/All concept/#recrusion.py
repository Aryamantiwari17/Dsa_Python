#recrusion
def find_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum


def find_sum_recur(n):
    if n==1:
        return 1
    
    return n+find_sum_recur(n-1)
    

def fibco(n):
    if n==0 or n==1:
        return 1
    
    return fibco(n-1)+fibco(n-2)
     


if __name__=="__main__":
    print(find_sum(5))
    print(find_sum_recur(5))
    print(fibco(5))
