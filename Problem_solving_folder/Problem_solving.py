# The correct soultion
'''def is_prime(num):
    #
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_nums():
    for i in range(1, 101):
        if is_prime(i):
            print(i)
prime_nums()'''

#return section 
def most_Repeated_Digit(numbers):
  
  
  nums = str(numbers)
   
  empty_dict = {}
  for num in nums:

    if num in empty_dict:

      empty_dict[num]+=1
    elif num not in empty_dict:
      empty_dict.update({num:1})
  # proplem B: 
  List_key = list(empty_dict)
  List_val = list(empty_dict.values())
  most_re = List_val[0]
  
  for i in List_val:
    if  i > most_re:
      
      most_re =i
  print(most_re)
  index=List_val.index(most_re)
  
  return int(List_key[index])
  
print(most_Repeated_Digit())
    
  
    