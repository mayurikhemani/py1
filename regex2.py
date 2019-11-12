#=========compile with findall=========
import re

p=re.compile('[a-e]')
print(p.findall("Baby shark do do do do do"))
#=======find if staring contain certain set of characters===========
p=re.compile('[a-zA-Z0-9]')
print(p.findall("Baby shark do2 do do do do3"))
#===========

#==============compile int=========
# \d is equivalent to [0-9].
p=re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))


# \d+ will match a group on [0-9], group of one or greater size 
p = re.compile('\d+') 
print(p.findall("I went to him at 11 A.M. on 4th July 1886")) 
#==========all characters in str==================
# \w is equivalent to [a-zA-Z0-9_]. 
p = re.compile('\w') 
print(p.findall("He said * in some_lang.")) 
  
# \w+ matches to group of alphanumeric character. 
p = re.compile('\w+') 
print(p.findall("I went to him at 11 A.M., he said *** in some_language.")) 
  
# \W matches to non alphanumeric characters. 
p = re.compile('\W') 
print(p.findall("he said *** in some_language.")) 

#==============findall============

str="how are you, how is everything"

matches=re.findall("how",str)

matches1=re.findall("Mayuri",str)

print(type(matches))

print(matches)
print(matches1)


#================match==========

matches=re.search("how",str)

print(type(matches))

print(matches)
# search for white space
y = re.search("\s",str)
print("the first white space is at ", y.start())

#===============span() group() string()============

matches=re.search("how",str)
print(matches.span())

print(matches.group())

print(matches.string)
# ========sub() putting @ at the place of white space===========

z=re.sub("\s","@",str)
print(z)
'''You can control the number of replacements by specifying the count parameter:
Example

Replace the first 2 occurrences:'''

t=re.sub("\s","@",str,2)
print(t)
#===============Regex==========
'''. 	Any character (except newline character) 	"he..o" 	
^ 	Starts with 	"^hello" 	
$ 	Ends with 	"world$" 	
* 	Zero or more occurrences'''
#to find string which starts with The and ends with spain

str1="Th rain in spain"

x=re.search("^The.*spain$",str1)
print(x)

#==============split=============

from re import split 
  
# '\W+' denotes Non-Alphanumeric Characters or group of characters 
# Upon finding ',' or whitespace ' ', the split(), splits the string from that point 
print(split('\W+', 'Words, words , Words')) 
print(split('\W+', "Word's words Words")) 
  
# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs 
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM')) 
  
# '\d+' denotes Numeric Characters or group of characters 
# Spliting occurs at '12', '2016', '11', '02' only 
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM')) 

#=============sub witj ignore=========
import re 

# Regular Expression pattern 'ub' matches the string at "Subject" and "Uber". 
# As the CASE has been ignored, using Flag, 'ub' should match twice with the string 
# Upon matching, 'ub' is replaced by '~*' in "Subject", and in "Uber", 'Ub' is replaced. 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', flags = re.IGNORECASE)) 

# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced. 
print(re.sub('ub', '~*' , 'Subject has Uber booked already')) 

# As count has been given value 1, the maximum times replacement occurs is 1 
print(re.sub('ub', '~*' , 'Subject has Uber booked already', count=1, flags =
             re.IGNORECASE)) 

# 'r' before the patter denotes RE, \s is for start and end of a String. 
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)) 
