text = "X-DSPAM-Confidence:    0.8475"
start=text.find(':')
number= text[start+1:]

print(float(number.strip()))

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)