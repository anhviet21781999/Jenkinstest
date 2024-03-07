"""
what are dictionaries and why use them?
An unordered collection of key -value pairs
Think of a python dictionary as a real world dictionary
each key is unique
"""

def main():
    #create a dictionayr of aws service and their decriptions
    aws_service = {
        'S3' : " simple storeage service for object storage",
        'lambda' : "Serverless compute service",
        'EC2' :   "Elastic compute cloud"      
    }
    # print the dic
    print(" simple storeage service for object storage")
    print(aws_service)
    
    #access the decription of an item in the dictionary
    lambda_decription = aws_service['lambda']
    print (f"lambda decription is : {lambda_decription}")

    #modify the decription
    aws_service['lambda'] = "AWS Serverless compute service "
    print(f"New decription of Lambda service is : {aws_service}")

    #add a new service to list 
    aws_service['SNS'] = "AWS Simple notification service "
    print (f"Added new service :  {aws_service['SNS']}   ")
    

    #remote the service from the library
    del aws_service['lambda']
    print (f"remove aws service : {aws_service} ")

    # use the key , value , item methods to display different aspects of the dictionary
    print(aws_service.keys())
    print(aws_service.values())
    print(aws_service.items())
    #modify the dictionary to add a nested stutrcture with additional information (launch_year)
    aws_service['EC2'] = {
        'decription' : "Elastic compute cloud",
        'launch_year' : 2006
    }
    print ("\nModified dictionary with nested structure:")
    print(aws_service)
if __name__ == '__main__':
    main()