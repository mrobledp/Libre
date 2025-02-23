# Perform bitwise operations
a = 0b1010  # 10 in decimal
b = 0b0101  # 5 in decimal

print('a', a)
print('b', b)

# Bitwise AND
and_result = a & b  # 0b0000
print(f'AND Result: {bin(and_result)}')

# Bitwise OR
or_result = a | b  # 0b1111
print(f'OR Result: {bin(or_result)}')

# Bitwise XOR
xor_result = a ^ b  # 0b1111
print(f'XOR Result: {bin(xor_result)}')

# Bitwise NOT
not_result = ~a  # -0b1011 (Two's complement)
print(f'NOT Result: {bin(not_result)}')

# Left Shift
shift_left = a << 1  # 0b10100
print(f'Left Shift: {bin(shift_left)}')

# Right Shift
shift_right = a >> 1  # 0b0101
print(f'Right Shift: {bin(shift_right)}')

### Example 2: Handling Bytes

# Create a bytes object
byte_data = bytes([65, 66, 67])  # Equivalent to b'ABC'
print(f'Bytes Data: {byte_data}')

# Convert bytes to an integer
integer_value = int.from_bytes(byte_data, byteorder='big')
print(f'Integer Value from Bytes: {integer_value}')

# Convert integer to bytes
new_byte_data = integer_value.to_bytes(3, byteorder='big')
print(f'Converted Back to Bytes: {new_byte_data}')
print(str(new_byte_data))
