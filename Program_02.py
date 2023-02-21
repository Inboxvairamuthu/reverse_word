#Write a Python program that accepts a word from the user and reverse it.

#def keyword
def reverse(string):
    reversed_string = ""
    #for loop
    for i in string:
        reversed_string = i+reversed_string
    #print statement for reversed string
    print("reversed string is:",reversed_string)

#get input from user
string = input("enter a string:")
#print statement for user input string
print("entered string",string)
reverse(string)