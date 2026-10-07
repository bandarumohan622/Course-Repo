str="python"
print(str[0])
print(str[1])
print(str[2])
print(str[-1])


#string sliceing-.............
string="hello world"
print(string[1]) 
print(string[-1])
print(string[1:3])
print(string[1:-1])
print(string[:3])
print(string[:3])
print(string[2:])
print(string[:-1])
print(string[::2])
print(string[1::2])
print(string[::-1])


#string concatenation(you can concatenate strings using the + operator)[string1+string2]
first_name ="john"
last_name ="deo"
full_name =first_name+" "+last_name
print(full_name)

#string length(you cna find the length of a string using the len() function)...
string1 ="my name is mohanraju!"
print(len(string1))


#string methods..................
s="hello. world!"
#convert string in uppercase.
print(s.upper())
#convert string in lowercase.
print(s.lower())
#remove leading and trailing whitespaces from the string
print(s.split())
#replaces all occurrences of 'o' to 'x' in the string
print(s.replace('o', 'mohan'))
#count the number of occurrences ofa' in the string
print('Abracadabra'.count('a'))


#string formatting............
name="mohanraju"
age=30
print(f"my name is {name} and i am {age} years old.")