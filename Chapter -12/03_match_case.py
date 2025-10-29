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