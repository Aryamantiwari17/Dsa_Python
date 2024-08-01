#ERROR HANDLING
## EXCEPTION TRY ,EXCEPT,BLOCK
try:
    a=b
except:
    print("Error")


try:
    a=b

except NameError as ex:
    print(ex)



try:
    10/0
except ZeroDivisionError as et:
    print(et)



try:
    result=1/2
    a=b
except Exception as ex1:
    print(ex1)

try:
    num=int(input("enter  a no."))
    result=10/num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("denominator")



#try,exceot,else,block

try:
    num=int(input("enter number"))
    result=10/num

except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("denominator")

else:
     
  print(f"the result is {result}")

finally:
    print("this is finally block")


#file handling and exception handling

try:
    file=open("example.txt",'r')
    content=file.read()
    print(content)

except FileNotFoundError:
    print("file doesnot exist")

finally:
    if 'file' in locals() and not file.closed():
        file.close()
        print("file closed")