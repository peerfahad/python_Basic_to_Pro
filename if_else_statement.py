# elephant_weight = 3000
# ant_weight = 0.1

# if elephant_weight > ant_weight:
#      print("Elephant weight is greater then aunt weight")  
# else:
#     print("elephand weight is less then aunt weight")

 
# #  fahad = 'happy'
# #  while fahad ==  happy:
# #      print("Fahad is happy")

# for count in range(5):
#      print("hi")

# Index Slicing
digits = [0,1,2,3,4,5,6,7,8,9]

# print(digits[0:10:3])

# for i in range(len(digits)):
#      print(digits[0:i])
window_size = 4
for i in range(len(digits)-(window_size-1)):
     print(digits[i:i+ window_size])
