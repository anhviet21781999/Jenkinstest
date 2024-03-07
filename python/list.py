"""
what are lists and why use them?
An ordered collection of items 
Especially useful when you need to work with a collection of related items
Contianers that help you store and manage multiple pieces  of data that can be of different data types
Think of a list as a procery shopping list 
"""

'''
Create a list of aws service and modify the list appropriately
'''

def main():

    #Create a list of aws service 
    aws_service = ['S3', 'lambda', 'EC2', 'RDS' , 'DynamoDB']
    #print
    print (f"aws servioce list : {aws_service}")
    
    #access the first service
    first_item = aws_service[0]
    print(f"first item is : {first_item}")
    
    #access the last item 
    last_item = aws_service[-1]
    print(f"last_item  is : {last_item}")
    
    #modify the last item
    aws_service[-1] = 'SNS'
    print(f"aws service after modify is : {aws_service}")

    #add the new service to list 
    aws_service.append('SQS')
    print(aws_service)

    #remove the second service from the list 
    aws_service.pop(1)
    print(f"aws service list : {aws_service}")
    

    #slice the list to get services from index 1 to 3 (inclusive of 1 and excluxive of 3)
    slice_service = aws_service[1:5]
    print(f"aws service list : {slice_service}")

    #find the length of the list 
    list_length = len(aws_service)
    print(f"list len is : {list_length}")



if __name__ == '__main__':
    main()