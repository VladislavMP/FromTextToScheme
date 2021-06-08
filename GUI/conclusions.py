import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
stops = ['%']
stops_s = ['\x02']
words1_1 = ["если", "когда"]
words1_2 = ["при условии", "так как", "если бы"]
words2_1 = ["то", "значит", "тогда"]
words2_2 = ["в результате", "в итоге", "так что"]
def concl(text):
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
        first_w = ""
        f_and_s_w = ""
        first_w_2 = ""
        flag1 = 0
        flag2 = 0
        flag3 = 0
        i_f1 = -1 # место обнаружения первого слова 
        i_f2 = -1 # место обнаружения запятой
        i_f3 = -1 # место обнаружения второго слова
        for word in sentence:
            word = word.lower()
            if i == 0: 
                first_w = word
                if word in words1_1:
                    flag1 = 1
                    i_f1 = i
            if i == 1:
                f_and_s_w = first_w + " " + word
                if f_and_s_w in words1_2: 
                    flag1 = 1
                    i_f1 = i
            if word == "," and flag1 == 1:
                flag2 = 1
                i_f2 = i
                
            if i_f2 + 1 == i and flag2 == 1: # конец обработки предложния
                if word in words2_1: 
                    flag3 = 1
                    i_f3 = i
                    break
                first_w_2 = word
            elif i_f2 + 2 == i and flag2 == 1:
                if first_w_2 + " " + word in words2_2: 
                    flag3 = 1
                    i_f3 = i
                    break
            elif i_f2 > i + 2 and flag2 == 1: flag2 = 0
            i = i + 1
          
        res_s = ""
        if flag3 == 1: # запись в результат 
            i = 0
            j = 0
            for word in sentence:
               if i <= i_f1: 
                   i = i + 1
                   continue
               if i == i_f2: 
                   result[k].append(res_s)
                   res_s = ""
                   j = j + 1
                   i = i + 1
                   continue
               if j == 1 and i <= i_f3: 
                   i = i + 1
                   continue
               res_s = res_s + " " + word
               if i + 1 == len(sentence):
                  result[k].append(res_s)
                  result.append([])
                  k = k + 1
               i = i + 1
    return result
