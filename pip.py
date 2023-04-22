
fruits=["Apple","Banana","Grapes","Lemon"]
if("Lemon" in fruits):
    print("Yes there is Lemon in fruits")




# Write a program that takes two lists of integers 
# and returns a new list that contains only the common 
# elements between the two lists.
def function(list1,list2):
    return list((set(list1)& set(list2)))

list1 =[30,80,90,48,67]
list2 =[80,71,23,43,67]
print(function(list1,list2))
        

#  Write a program that takes a list of 
# integers and returns a new list that 
# contains the cumulative sum of the original list.
def cumulativenum(numbers):
    answer =[]
    sum=0
    for num in numbers:
        sum+=num
        answer.append(sum)

        return answer
    
numbers =[40,90,80,60,50]   
print(cumulativenum(numbers))

# Write a program that takes two lists of integers 
# and returns a new list that contains the elements 
# from both lists in sorted order.       
def arrangelist(listA,listB):
    both=listA+listB
    both.sort()

    return both
    
listA=["Ann","Wakah","Muyale"]  
listB=["Charles","Zan","Abriella"]
print(arrangelist(listA,listB))

# Write a Python program that squares each 
# element of a given list using list comprehension.
# python
numersas =[40,57,71,89,59,70]
multiply= (x**2 for x in numersas)
print(multiply)

# Write a Python program that filters out
# all negative numbers from a given list 
# using list comprehension.
digits= [20,-4,78,90,-4,-78]
positivenos=[x for x in digits if x>=0]
print(positivenos)

# Write a Python program that concatenates two
# lists using list comprehension .
compress= [80,90,50,60]
compress1=[30,80,60,70]
listcomp=[i for i in compress]+[i for i in compress1]
print(listcomp)




