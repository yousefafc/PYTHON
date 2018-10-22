#var=5
#if var < 10:
 #   print("hello")
#else:
 #   print("world")
myList = [1, 2, 3, 4, 5]
myDictionary = {1: "yousef", 2: "zak", 3: "ibraheem"}

#for keys,values in myDictionary.items():
 #   print(keys)
 # print(values)
# question1
Q1 = [123, 354, 324, 2340, 324, 234, 756, 955]
# iterate through an array of numbers and print out only the largest
print(max(Q1))
# question2
Q2 = [432, 435, "588", "463", 234]
Q2 = list(map(int, Q2))
print(Q2)#integers
Q2_2 = list(map(str, Q2))
print(Q2_2)
# question3
Q3 = {"K1": "V1", "K2": "V2", "K3": "V3"}
# switch each key with its value
Q3_1 = {y:x for x,y in Q3.items()}
print(Q3_1)
# question4
Q4 = (1, 2, 3, 4, 5)
# changing values in the tuple
lst = list(Q4)
lst[0] = 300
Q4 = tuple(lst)
print(Q4)
# question 5
Q5 = [50, 96, 45, 67, 88]
# iterate through a list of exam results and print out how many exams were less than 70
Q5_1 = [i for i in Q5 if i < 70]
print("The number of failed papers:", len(Q5_1))
Q6 = [33, 56, 75, 78, 34, 56]
# for each number print out "FIZZ" if it's divisible by 3, "BUZZ" if its divisble by 5 and "FIZZBUZZ" if its divisible by both
for i in range(0,5):
    if Q6[i] % 3 == 0 and Q6[i] % 5 == 0:
                print(Q6[i],"FIZZBUZZ")
    elif Q6[i] % 3 == 0:
        print(Q6[i], "FIZZ")
    elif Q6[i] % 5 == 0:
        print(Q6[i], "BUZZ")





