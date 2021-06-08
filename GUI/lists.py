import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
stops = ['%']
stops_s = ['\x02']
def list(text):

    text = "".join([ch for ch in text if ch not in stops_s])   
    new_text = word_tokenize(text, language="russian")
    flag1 = 0

    arr_of_words = [[]]
    i1 = 0
    i2 = 0
    i3 = 0
    for word in new_text: # токенизация по предложениям + токенизация по словам + удаление лишнего
        p = morph.parse(word)
        if {'PNCT'} in p[0].tag:
            
            if word == ']':
               flag1 = 0
            elif word == '[':
               flag1 = 1
            elif word == '.':
               i1 = i1 + 1
               arr_of_words.append([])
            elif word != '[' and flag1 != 1:
               arr_of_words[i1].append(word)
        elif flag1 != 1: arr_of_words[i1].append(word)


    result = [[]]
    k = 0
    for sentence in arr_of_words:
        i = 0
        flag1 = 0 # флаг обнаружения :
        i_f1 = -1 # место обнаружения 1
        i_list = []
        for word in sentence:
            if word == ":" and flag1 == 0:
                i_f1 = i
                flag1 = 1
                i = i + 1
                continue
            if word == ";" and flag1 == 1:
                i_list.append(i)
                i = i + 1
                continue
            i = i + 1

        if len(i_list) < 2 and flag1 == 1:
            i = 0
            flag1 = 0 # флаг обнаружения :
            i_f1 = -1 # место обнаружения 1
            i_list = []
            for word in sentence:
                if word == ":" and flag1 == 0:
                    i_f1 = i
                    flag1 = 1
                    i = i + 1
                    continue
                if word == "," and flag1 == 1:
                    i_list.append(i)
                    i = i + 1
                    continue
                i = i + 1

        res_s = ""
        if len(i_list) > 1 and flag1 == 1: # запись в результат 
            i = 0
            j = 0
            for word in sentence:
               if i == i_f1: 
                   result[k].append(res_s)
                   res_s = ""
                   i = i + 1
                   continue
               if j < len(i_list):
                    if i == i_list[j]: 
                        result[k].append(res_s)
                        res_s = ""
                        i = i + 1
                        j = j + 1
                        continue
               res_s = res_s + " " + word
               if i + 1 == len(sentence):
                  result[k].append(res_s)
                  result.append([])
                  k = k + 1
               i = i + 1
    return result