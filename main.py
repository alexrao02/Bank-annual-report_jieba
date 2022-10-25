import jieba
import csv
import re
import os



def get_stopwords_list():
    stopwords = [line.strip() for line in open('金融科技词库.txt',encoding='UTF-8').readlines()]
    return stopwords


def move_stopwords(sentence_list, stopwords_list):
    # 去停用词
    out_list = []
    for word in sentence_list:
        if word in stopwords_list:
                out_list.append(word)
    return out_list


path = "21家银行年报" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
files.remove('.DS_Store')
sec_path = []
thi_path = []
for i in files:
    p = path + '/' + i
    sec_path.append(p)
for ppath in sec_path:
    fname = os.listdir(ppath)
    for p in fname:
        pp = ppath + '/' +p
        thi_path.append(pp)

for p in thi_path:
    print(p)
    if p == '21家银行年报/南京银行2011-2021/.DS_Store':
        continue
    obj1 = re.compile(r"21家银行年报/(?P<dic>.*?)/(?P<name>.*?).txt", re.S)
    res = obj1.finditer(p)
    dicname = '1'
    name = '2'
    for i in res:
        dicname = (i.group(("dic")))
        name = (i.group(("name")))
    with open('金融科技词库.txt', 'r', encoding='utf-8') as f:
        ciku = f.read().splitlines()
    for i in ciku:
        jieba.add_word(i)

    with open(p, 'r', encoding= 'UTF-8') as f:
        str = f.read()
    word_list = jieba.lcut(str)
    sws = get_stopwords_list()
    wordlist = move_stopwords(word_list, sws)

    # 遍历 word_list ，对 word 出现的频率进行统计
    counts = {}
    for word in wordlist:
        counts[word] = counts.get(word, 0) + 1

    # 按照词频排序
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 默认升序，reverse=True为降序

    # 保存词频统计结果至csv文件
    # save_path = 'result/' + dicname + '/' + name + '.csv'
    with open('1.csv', 'a', newline='') as f:
        write = csv.writer(f)
        write.writerow([" ", " "])
        write.writerow([" ", " "])
        write.writerow([dicname, name])
        write.writerow(["word", "count"])
        for i in range(len(items)):
            word, count = items[i]  # 返回相对应的键值对
            write.writerow([word, count])

# with open('金融科技词库.txt','r',encoding='utf-8') as f:
#     ciku = f.read().splitlines()
# for i in ciku:
#     jieba.add_word(i)
#
# with open('交通2021.txt','r',encoding='utf-8') as f:
#     str = f.read()
# word_list = jieba.lcut(str)
# sws = get_stopwords_list()
# wordlist = move_stopwords(word_list, sws)
#
# # 遍历 word_list ，对 word 出现的频率进行统计
# counts = {}
# for word in wordlist:
#     counts[word] = counts.get(word, 0)+1
#
# # 按照词频排序
# items = list(counts.items())
# items.sort(key=lambda x: x[1], reverse=True)  # 默认升序，reverse=True为降序
#
# # 保存词频统计结果至csv文件
# with open('result1.csv', 'a', newline='')as f:
#     write = csv.writer(f)
#     write.writerow(["word", "count"])
#     for i in range(len(items)):
#         word, count = items[i]    # 返回相对应的键值对
#         write.writerow([word, count])


#
#
# path = "21家银行年报" #文件夹目录
# files= os.listdir(path) #得到文件夹下的所有文件名称
# files.remove('.DS_Store')
# sec_path = []
# thi_path = []
# for i in files:
#     p = path + '/' + i
#     sec_path.append(p)
# for ppath in sec_path:
#     fname = os.listdir(ppath)
#     for p in fname:
#         pp = ppath + '/' +p
#         thi_path.append(pp)
# for i in thi_path:
#     print(i)
#
