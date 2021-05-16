import string
f = open('paper.txt', 'r',encoding="utf-8")
fout = open('dictionary_fr_ques2.txt', 'w+',encoding="utf-8")
str = f.read()
inChar = "-/"
outChar= "  "
str = str.translate(str.maketrans(inChar,outChar))
str = str.translate(str.maketrans("","",string.punctuation))
str=str.replace("\n"," ")
str=str.lower();
arr = str.split(" ")   
dict_word = {}
for i in arr:
    if i in dict_word:
        dict_word[i] +=1
    else: 
        dict_word[i] = 1
dict_sort = sorted(dict_word, key= dict_word.get, reverse=True)
print(f"\nThe word that appears the most is : '{dict_sort[0]}'")
print("\n Dictionary: ", dict_word)
set_word = set(arr)
print("\n Bộ từ điển: ", set_word)
values_sorted = sorted(set_word)
for i in values_sorted:
    fout.writelines(i +"\n")
f.close()
fout.close()