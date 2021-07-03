import numpy
import string
from os import listdir
import os
import pandas as pd 
import math

raw_dir = "./dataSet/Train_Full"
csv_path = "./dataSet/exportCSV"



def read_file(dir):
    lable = dir.split("/")[-1]
    lable = "_".join(lable.lower().split())
    data=[]
    file_paths = os.listdir(dir)
    if file_paths and len(file_paths):
        for file in file_paths:
            with open(f"{dir}/{file}", mode = "rb") as f:
                text = f.read()
                data.append(text.decode("utf16").strip())
    return lable, data

def split_sentence(str):
    arr = str.split('.')
    return arr

def create_dict(str):
    inChar = "-/"
    outChar= "  "
    str = str.translate(str.maketrans(inChar,outChar))
    str = str.translate(str.maketrans("","",string.punctuation))
    str=str.replace("\n"," ")
    str=str.replace("\r"," ")
    str=str.lower()
    arr = str.split(" ") 
    dict_word = {}
    j=0
    for i in arr:
        if len(i)!=0:
            j +=1
            if i in dict_word:
                dict_word[i] +=1
            else: 
                dict_word[i] = 1
    dict_sort = sorted(dict_word.items(), key= lambda x:x[1], reverse=True)
    return  dict_word,j

def save_filecsv(folder, filename, data):
    df = pd.DataFrame(data) 
    df.to_csv(f"{csv_path}/{folder}/{filename}.csv",encoding="utf-16")

def computeTF(wordDict, total_word):
    tfDict = {}
    for word in wordDict:
        tfDict[word] = wordDict[word]/total_word
    return tfDict

def count_sentences(text):
    j=0
    for i in text:
        if len(i)!=0:
            j +=1
    return j

def check_sentences(sentences, word):
    if sentences[word]:
        return True
    return False

def computeIDF(text):
    idfDict = {}
    list_sentences = split_sentence(text)
    dict_words, total_words = create_dict(text.replace(".", " "))
    total_sentences = 0
    idfDict = dict.fromkeys(dict_words, 0)
    for sentences in list_sentences:
        if len(sentences)==0:
            list_sentences.remove(sentences)
        else:
            total_sentences += 1
            wordDict, total_word = create_dict(sentences)   
            for word in wordDict:
                if wordDict[word] > 0:
                    idfDict[word] += 1
                else:
                    break
    for word in idfDict:
        try:
            idfDict[word] = math.log10(total_sentences / idfDict[word])
        except ZeroDivisionError:
            idfDict[word] = 0
    return idfDict

def computeTFIDF(tfDocs, idfs):
    tfidf = {}
    for word, val in tfDocs.items():
        tfidf[word] = val*idfs[word]
    return tfidf 

def create_folder(path):
    try:
        if not os.path.exists(path):
            os.mkdir(path) 
    except OSError as error: 
        print(error)  

if __name__=='__main__':
    folders = os.listdir(raw_dir)
    for folder in folders:
        create_folder(csv_path +"/"+folder)
        label, data = read_file(raw_dir +"/"+folder)
        j=0
        for text in data:
            j= j+1
            list_sentences = create_dict(text)
            arr = split_sentence(text)
            total_sentences = 0
            list_tfidfs = []
            for i in arr:
                if len(i)==0:
                    arr.remove(i)
                else:
                    total_sentences += 1
                    wordDict, total_word = create_dict(i)
                    tfidf = computeTFIDF(computeTF(wordDict, total_word),computeIDF(text)) 
                    list_tfidfs.append(tfidf)
            df = pd.DataFrame(list_tfidfs)
            df.to_csv(f"{csv_path}/{folder}/"+str(j)+".csv", encoding="'utf-8-sig")
            # export 100 file and break, each file is each txt file
            if(j==100):
                break
    
    
    

