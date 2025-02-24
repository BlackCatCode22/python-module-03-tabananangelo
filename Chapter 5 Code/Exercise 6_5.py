str='X-DSPAM-Confidence:0.8475'
colon_pos=str.find(':')
print(colon_pos)
# Gives us colon position
piece=str[colon_pos+1:]
# Instructs the program to make "piece" equal anything after the : in str
print(piece)
str_to_float=float(piece)
# Converts the 0.8475 to a floating-point number, and allows us to use it in equations
print(str_to_float)