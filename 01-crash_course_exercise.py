"""
This is a crash course exercise for data science and ML bootcamp
This is a very easy exercise for me, but still important nontheless to refresh my mind
"""

# 1: what is 7 to the power of 4? (answer: 2401)
print(7**4)

# 2: Split this string into a list: "Hi there Anggi!"
s = "Hi there Anggi!"
print(s.split())

# 3: Use .format() to print "The diameter of Earth is 12742 kilometers" given these variables:
planet = "Earth"
diameter = 12742

print("The diameter of {} is {} kilometers".format(planet,diameter))
#or
# print("The diameter of {x} is {y} kilometers".format(y=diameter,x=planet))
#or
# print("The diameter of "+planet+" is "+str(diameter)+" kilometers")

# 4: Use indexing to grab the word "hello" (without list bracket) in the following nested list:
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

print(lst[3][1][2][0])

# 5: Similarly to question 4, but instead use this nested dictionary:
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

p = d['k1'][3]['tricky'][3]['target'][3]
print(p)

# 6: What is the main difference between tuple and a list?
#   ANS:
#   Tuple is immutable (i.e., cannot change the item inside) while list is mutable

# 7: Create a function that grabs the email website domain from a string in the form: user@domain.com
def domainGet(surel):
    domain = surel.split('@')[1]
    return domain

grab = domainGet('user@domain.com')
print(grab)

# 8: Create a basic function that returns True if the word 'dog' is contained in the input string. 
# # Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def findDog(dog):
    # lst = dog.lower().split() # lowercase all letters then make a string list from sentence
    # state = [print('True') for inu in lst if inu == 'dog']
    # return state
    return 'dog' in dog.lower().split()

print(findDog('Is there a dog here?'))

# 9: Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.

def countDog(dogs):
    # lst2 = dogs.lower().split() # lowercase all letters then make a string list from sentence
    i = 0
    # for inu2 in lst2:
    #     if inu2 == 'dog': i=i+1
    for inu in dogs.lower().split():
        if inu == 'dog': i += 1
        
    return i

print(countDog('This dog runs faster than the other dog dude!'))

# 10: Use lambda expressions and the filter() function to filter out words 
# from a list that don't start with the letter 's'. For example:
seq = ['soup','dog','salad','cat','great']
# should be filtered down to: ['soup','salad']

f = filter(lambda menu: menu[0] == 's', seq)
print(list(f))

# FINAL: You are driving a little too fast, and a police officer stops you. 
# Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
# If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, 
# the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday 
# (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    if is_birthday: speed = speed - 5 # birthday=true, so the reading speed is x-5
    if speed > 80:
        return 'Big Ticket'
    elif speed > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

    return

print(caught_speeding(81,True))    # 'Small Ticket'
print(caught_speeding(81,False))   # 'Big Ticket'
print(caught_speeding(64,True))    # 'No Ticket'