letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[::-1]

#print(backwards)

# Create a slice that produces the characters qpo
sliceqpo = letters[16:13:-1]
print(sliceqpo)
# Slice the string to produce edcba
print(letters[4::-1])
# Slice the string to produce the last 8 characters, in reverse order
print(letters[25:17:-1])
print(letters[:-9:-1])
