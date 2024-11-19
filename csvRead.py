from CSVtoTable import *
path = 'results/vg_hopper/'
AnalyzedFile = "2.csv"
tbl = TableCsv(path+AnalyzedFile, ";", progress=True)

def CountWords(lst):
    words = {}
    for str in lst:
        str.replace(';', ' ')
        str_spl = str.split(" ")
        for word in str_spl:
            if word.lower() in words.keys():
                words[word.lower()] += 1
            else:
                words[word.lower()] = 1
    sorted_words = dict(sorted(words.items(), reverse=True, key=lambda item: item[1]))
    return sorted_words

cc = CountWords(tbl.getColumnList('description'))
print(cc)

