
list = ['apple', 'rat',2,'fizzbomb', 'fizzy', 'mango']

def max_length_string(word_list, max_len):
    
    """
    returns the maximum length string from the word_list with 
    maximum length as max_len
    """
    new_list =[]
    try :
        
      for value in word_list:
        #print(index,value)
    
           if len(value) == max_len:
                new_list.append(value)
    except TypeError:
           print(' List has numeric values. Please provide only string values')
           pass
      
    return new_list    
    
print(max_length_string(list, 5))  