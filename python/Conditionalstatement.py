"""
A piece of code that executes instructions based on a particular state 
useful for 
Controlling the flow of a program
executing different code based on different conditions 
In a python program, the if statement is how you perform this sort of decision-making 

"""
"""
weather = 'cold'
if weather == 'cold':
    drink = "a hot coffee"
else:
    drink = "a cold coffee"
print (f"i want {drink} please")
"""

'''
determine the appropriate AWS service based on the user's requirement 
'''

def main():
    # define the user's requirement : file_storage, serverless_computing, virutal_server, other

    user_requirement = 'file storage'


    if user_requirement == 'file storage':
        aws_service = 's3'
    elif user_requirement == 'virutal_server':
        aws_service = 'EC2'
    elif user_requirement == 'serverless_computing':
        aws_service = 'Lambda'
    else:
        aws_service = 'unknown'



    #print the recommended AWS service based on the user's requirement
    #check if the service is not 'unknown'
    if aws_service != 'unknown':
        print(f"aws service is {aws_service}")
    else:    
        print("unknow service")

if __name__ == '__main__':
    main()