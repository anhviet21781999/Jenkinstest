"""
for loop : definite interation - the number of repetitions is specified explicitly in advance

while loop : Indefinite iteration - the number of repetitions isn't specified explicily in advance
"""
#list of aws services
aws_services = ['S3','Lambda','Ec2','RDS','SQS']
print (f"AWS services list is : {aws_services}")

# use for loop to interate through the list 
print("\nUsing the for loop to iterate through the list : ")
for service in aws_services:
    print(service)


#use a while loop to iterate through the list in reverse order
print("\nuse a while loop to iterate through the list in reverse order :")
index = len(aws_services) 
while index >0:
    print(aws_services[index])
    index -=1


#using enumerate() with a for lôp to get botyh index and value
print("\n using enumerate() with a for lôp to get botyh index and value : ")
for index, service in enumerate(aws_services):
    print(f"service #{index}: {service}")


index = len(aws_services) -1
print(index)