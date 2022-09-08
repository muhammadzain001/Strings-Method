#  .upper and .lower functions of strings

low = "no caps"
print(low.upper())
print(low)

caps = "LOWS"
print(caps.lower())
print(caps)

# .isupper() and .islower()
var = "hellow"
print(var.isupper())
print(var.islower())

var2 = "HELLOW"
print(var2.islower())
print(var2.isupper())

# Multiple String Methods
print("SHOUT!".lower().isupper())

# .isalpha(): only letter
# .isalnum(): numbers and letters
# .isdecimal(): numbers
# .isspace(): only spaces
# .istitle(): title case
print("Batman".isalpha())
print("Hellow123".isalnum())
print("2".isdecimal()) # This only supports integers , if decimal then false
print(" ".isspace())
print("Hellow , How Are You".istitle())

print("hello , how are you".title()) # Makes first letters of words capital

# .startwith() and .endswith()
print("hellow, what r u doing".startswith("hellow"))
print("hellow, what r u doing?".endswith("?"))

# .join()
print("".join(["one", "two", "three"]))
print(" ".join(["one", "two", "three"]))
print(",".join(["one", "two", "three"]))
print(", ".join(["one", "two", "three"]))
print("...".join(["one", "two", "three"]))
print("'".join(["one", "two", "three"]))

# .split()
print("Eggs , Milk , Waffles , Bacon".split(","))

# Exercise
mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))

word = mixed_case.split()
print(word)

print("".join(word).isalpha())

# .rjust() and .ljust()
print("hello world".rjust(15))
print("hello world".ljust(15) + "4 years later")

# Second Arguments
print("hello world".rjust(15, "_"))
print("hello world".ljust(15, "_") + "what?")

# .center()
print("hello world".center(15))
print("hello world".center(15, ":"))

# .strip() , .rstrip() , .lstrip()
print("the trip was amazing!!!!!!!1111111111".strip("1"))
print("the trip was amazing!!!!!!!1111111111".rstrip("1"))
print("the trip was amazing!!!!!!!1111111111".lstrip("1"))

print("juice, bread, cheese, beef, bread".rstrip(", bread"))
print("juice, bread, cheese, beef, bread".rstrip(", ed arb"))

# .replace
print("hellow".replace("hellow", "bye"))

# len() length
print(len("hellow how are you"))

# Word Reverser

user_input = input("Write a string ")
reversed = ""

for item in range (len(user_input) -1 , -1 , -1):
      reversed += user_input[item]

print(reversed)

# .format()
name = input("What is the applicant's name?")
degree = input("What major did they take at college")
job = input("What is their current occupation")
experience = input("How many years have they worked in their field")

print("{} majored in {}, works as a {}, and has {} years of experience".format(name, degree, job, experience))

