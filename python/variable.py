#Create first string variable 
name = 'Anh'
profession = 'engineer'

#Create variable containing 'interger'
Books_written = 6 

#Concentrate and print out variables
output = name +' is a ' +  profession + " and he's wirttent " + str(Books_written) + " books."
#voi output 2 xu dung f string nen khong can ep str(Books_written)
output_2 = f"{name} is a {profession} and he is writtent {Books_written} books." 
print(output_2)