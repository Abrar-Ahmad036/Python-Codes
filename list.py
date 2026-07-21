# numbers=[12,45,12,8,90]
# print(len(numbers))
# print(numbers)
# count=(numbers.count(12))
# print("12 present ",count," times")

# list=[5,10,15,20,25,30]
# list.reverse()
# print(list)
# for l in list:
#     if(l>20):
#         print(l)


# print("numbers greater 20 are not present ")



# fruits=["apple","banana","banana","orange","apple"]
# unique_fruits=[]
# for fr in fruits:
#     if fr not in unique_fruits:
#         unique_fruits.append(fr)
# print(unique_fruits)
       

# data=[1,2,3,4,5,6,7,8]
# odd=[]
# even=[]
# for num in data:
#     if(num%2==0):
#         even.append(num)
#     else:
#         odd.append(num)    
# print("Even numbers : ",even)
# print("Odd numbers : ",odd)

values=[42,11,89,3,67,80]
min_values=values[0]
max_values=values[0]
for val in values:
    if(val<min_values):
        min_values=val
for val1 in values:
    if(val1>max_values):
        max_values=val1       
print("Minimum value is : ",min_values)
print("Maximum value is : ",max_values)






