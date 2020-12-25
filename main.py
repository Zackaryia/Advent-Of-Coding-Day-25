"""
First attempt
def transform_number(subject_number, mod_by, value=1, loop_size=1):
	if loop_size > 1:
		for _ in range(loop_size):
			value = transform_number(subject_number, mod_by, value)
		return value
	else:
		value = pow(value, subject_number, mod_by)  #does  x ** y % z
		return value

print(transform_number(3704642, 20201227, loop_size=3463328))

card_public = 2084668
door_public = 3704642
value = 1
for x in range(100000000):
	value = transform_number(11, 20201227, value)

	if x == 3:
		print('kul')
	if value == 2084668:
		print("Door public key loop size is", x)
	if value == 3704642:
		print("Card public key loop size is", x)
"""

#Second Attempt



def get_loop_size_of_key(subject_number, key):
	value = 1
	loop_size = 0
	while value != key and loop_size < 50000000:
		loop_size += 1
		value *= subject_number
		value = value % 20201227
	
	return loop_size

def encryption_key(subject_number, loop_size):
	value = 1

	for _ in range(loop_size):
		value *= subject_number
		value = value % 20201227

	return value

print(get_loop_size_of_key(7, 5764801)) #test example
print(get_loop_size_of_key(7, 17807724)) #test example

#My inputs

card_loop_size = (get_loop_size_of_key(7, 2084668)) #test example
door_loop_size = (get_loop_size_of_key(7, 3704642)) #test example

print(card_loop_size, door_loop_size)

print(encryption_key(3704642, card_loop_size))

#Solved part 1

# No part two for this puzzle.