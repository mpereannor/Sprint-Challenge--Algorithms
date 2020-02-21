'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  #base case 
  if len(word) < 2 and word != 'th':
    return 0
  
  if len(word) == 2 and word == 'th': 
    return 1
  
  elif word[0:2] == 'th':
    return 1 + count_th(word[1:])
  
  else: 
    return count_th(word[1:])
  
  
  

  #second unsuccessful attempt
  # def th_count(strings):
  #   if strings == 0:
  #     return 0
  #   elif strings == 'th': 
  #     return 1 + count_th(strings)
  # if len(word) == 1: 
  #   return th_count(word.count())
  
  # return  count_th(word -1) + th_count(word[- 1])
  
  #first unsuccessful attempt
  # count_length = 0
  # chosen_string = 'th'
  # def th(char, length = 0):
  #   if char == 0:
  #     count_length =+ length
  #     return 
  #   if chosen_string:
  #     th( char - 1, length + chosen_string)   
  # th(word) 
  # return count_length
  
