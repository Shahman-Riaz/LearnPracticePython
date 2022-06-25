## PROBLEM::: *Given a String S, reverse the string without reversing its individual words.* 
sentence = input('Enter your sentence: ')
splited_list =  sentence.split(' ')
reverse_sentence = " ".join(reversed(splited_list))
print(reverse_sentence)