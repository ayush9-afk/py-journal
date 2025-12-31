def https_status(status):
    match status:
        case 200:
            return"Ok"
        case 401:
            return"Not Found"
        case 500:
           return "Internal Server Error" 
        case _: 
            return "Unknown status" 
        
#Usage
print(https_status(200))
print(https_status(401))
print(https_status(500))


# dict1 = {'a' : 1 , 'b' : 2}
# dict2 = {'b' : 3 , 'c' : 4}

# merged = dict1|dict2
# print(merged)


# usage of with we open multiple Files

#with (
#    open('files.txt') as f1,
#    open('files.txt') as f2
#):
    #process files