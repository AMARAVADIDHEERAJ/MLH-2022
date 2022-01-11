def reversing_string(string):
    str1 = ""
    for i in string:
        str1 = i + str1
    return str1
string = "MLH LHD_2"
print("The original string is: ", string)
print("The reversed string is:", reversing_string(string))

## Output:
#The original string is:  MLH LHD_2
#The reversed string is: 2_DHL HLM
##
