
d = {0: 10, 1:20}
print(d)

# update new kv
d.update({2:30})
print(d)

# update existing value
d.update({1:66})
print(d)

# initiate new dict
square_dict = dict()
square_dict = {}

# generate new dummy dict based on number range
for num in range(7, 22):
    square_dict[num] = num*num
print(d)
print(square_dict)

# initiate new dict for concatenation
concat_dict = dict()
for d in (d, square_dict): 
    concat_dict.update(d)

print(concat_dict)

# check if key is already present in the dict.
def is_key_present(x):
  if x in concat_dict:
      print('Key is present in the dictionary\n')
  else:
      print('Key is not present in the dictionary\n')
is_key_present(5)
is_key_present(9)


# loop over dict to extract kv pairs
for k,v in concat_dict.items():
    print(k,":",v)

ndict = dict()
n = 22
for p in range(11,n+1):
    ndict[p] = p * p
    
print(ndict)

#  print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
n2dict = dict()
for i in range(1,16):
    n2dict[i] = i*i
    
print(n2dict)

n3dict = dict()
for d in (ndict,n2dict):
    n3dict.update(d)
print(n3dict)