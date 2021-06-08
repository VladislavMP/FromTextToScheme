import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
#print (stopwords.words("russian")) 
#ru_stops = set(stopwords.words('russian'))
#ru_stops.add(".");
#ru_stops.add(",");
#ru_stops.add(")");
#ru_stops.add("(");
stops = ['%']
stops_s = ['\x02']
stops_for_n = ['(', ')', '-', '–', ':', '.']
legend_words = ['тыс.', 'тыс', '%', 'млн.', 'млн', 'млрд', 'млрд.', 'В', 'Гц', 'дБ', 'см', 'м', 'км']


def legend_f(list_f1, sentence, result):
    legend = []
    legend_i = ""
    for i in list_f1:
        k = 1
        while (i + k < len(sentence)):
             if sentence[i + k] in legend_words:
                 legend_i = legend_i + sentence[i + k] + " "
                 k = k + 1
             else:
                 break   
        legend.append(legend_i)
        legend_i = ""
    result.append(legend)  

def diagram(text):
    text = "".join([ch for ch in text if ch not in stops_s])
    new_text = word_tokenize(text, language="russian")
    flag1 = 0
    arr_of_words = [[]]
    i1 = 0
    i2 = 0
    i3 = 0
    for word in new_text: # токенизация по предложениям + токенизация по словам + удаление лишнего
        p = morph.parse(word)
        #print(p[0].tag.case)
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

    result = []
    for sentence in arr_of_words:
        i = 0
        j = 0
        k = 0
        flag1 = 1 # флаг обнаружения :
        flag2 = 0
        new_res = []
        list_f1 = []
        for word in sentence:
            p = morph.parse(word)
            if ({'NUMB'} in p[0].tag and flag1 == 0) or (word in stops_for_n):
                if len(new_res) > 1:
                    result.append(new_res)
                else:
                    while (i > 0):
                        list_f1.pop()
                        i = i - 1
                if len(new_res) > 1:
                    legend_f(list_f1, sentence, result)
                    list_f1 = []
                new_res = []
                i = 0
                j = j + 1
                flag1 = 1
            if {'NUMB'} in p[0].tag and flag1 == 1:
                word = word.replace(',','.')
                new_res.append(word)
                i = i + 1
                list_f1.append(k)
                flag1 = 0
            if word == ',' or {'CONJ'} in p[0].tag:
                flag1 = 1
            k = k + 1

        if len(new_res) > 1:
            result.append(new_res)
            legend_f(list_f1, sentence, result)
            list_f1 = []

#   for sentence in arr_of_words:      
#       for word in sentence:
    result.append([])
#    i = 0
#    j = 0
#    k = 0
#    result = [[]]
#     while j < len(short_text):
#        p = morph.parse(short_text[j])
#        if {'NUMB'} in p[0].tag:
#            short_text[j] = short_text[j].replace(',','.')
#            result[i].append(short_text[j])
#            j = j + 1
#            continue
#    
#        if short_text[j] == ".":
#            if len(result[i]) <= 1:
#                result[i] = []
#                i = i - 1
#            if len(result[i]) != 0:
#                result.append([])
#            i = i + 1
#            j = j + 1
#            continue
#        j = j + 1
      
    return result
