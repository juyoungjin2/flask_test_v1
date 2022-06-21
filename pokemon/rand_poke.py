import random
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('../static/image') if isfile(join('../static/image', f))]
# 숫자만 남기기
num = [i[3:6] for i in onlyfiles]
# print(len(num))
num_2 = list(dict.fromkeys(num))
print(num_2)
num_2.sort()
print(num_2)
print(len(num_2))
# class MyClass:
# chosen_list = []
# with open('./test.txt', 'w') as f:
#     for i in onlyfiles:
#         print(i)
#         f.writelines(i+"\n")



