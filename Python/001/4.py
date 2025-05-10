# Type Conversion

# Implicit Type Conversion
# Converting Int to float

integer =  123
float = 1.23

new = integer + float

# print("Value:",new)
# print("Data Type:",type(new))

# -------------------------------------------------------------------------------
# Explicit Type Conversion
# adding string and integer

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


# Key Points to Remember
# Type Conversion is the conversion of an object from one data type to another data type.
# Implicit Type Conversion is automatically performed by the Python interpreter.
# Python avoids the loss of data in Implicit Type Conversion.
# Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.
# In Type Casting, loss of data may occur as we enforce the object to a specific data type.