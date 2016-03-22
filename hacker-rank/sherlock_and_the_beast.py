

d = f + t
f % 3 == 0
t % 5 == 0


d = f + t


#  tmp number of five values is the number of digits
ftmp = d
# decrease the number of fives (by the number of threes in a batch)
#  until both the rules f % 3 == 0 and t % 5 == 0 are satisfied
while ftmp % 3 != 0 : ftmp -= 5

# check the ftmp is a valid value
if ftmp % 3 != 0 : return -1;

f = ftmp;
t = d - f

return "5" x f + "3" x t