def custom_sort(words):
  # Put each word into the x_list or the other_list.
  e_list = []
  other_list = []
  for word in words:
    if word.startswith('e'):
      e_list.append(word)
    else:
      other_list.append(word)
  return sorted(e_list) + sorted(other_list) 

if  __name__ == '__main__':

   list1 = ['gt','abc','eabc','exxx','def','edef','ebcde']

   # Calling function defined
   list2 = custom_sort(list1)
   print list2 
