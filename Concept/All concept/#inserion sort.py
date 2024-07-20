#inserion sort
def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor=elements[i]#assign anchor
        j=i-1#assign j
        while j>=0 and anchor<elements[j]:
            elements[j+1]=elements[j]
            j=j-1
            elements[j+1]=anchor






if __name__=="__main__":
    elements=[11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)