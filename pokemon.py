import random
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('./static/image') if isfile(join('./static/image', f))]

class Rand_poke():



    def __init__(self):

        self.num = self.rand_poke()

    def rand_poke(self):
        with open('./list.txt', 'w') as f:
            for i in onlyfiles:
                print(i)
                f.writelines(i + "\n")

        with open("./list.txt") as f:
            num_pool = f.readlines()
        # 파일을 리스트로 변환 > 숫자만 남기기
        num_pool = [line.rstrip('\n')[3:6] for line in num_pool]
        num_pool = list(dict.fromkeys(num_pool))
        num_pool.sort()
        with open('./Pool_num.txt', 'w') as f:
            for i in num_pool:
                print(i)
                f.writelines(i + "\n")

        with open("./chosen.txt") as f:
            chosen_num = f.readlines()
        chosen_num = [i.rstrip('\n') for i in chosen_num]
        print(chosen_num)
        # 전체리스트에서 뽑았던 리스트 제외 > POOL을 재정의
        num_pool = [x for x in num_pool if x not in chosen_num]
        # print('\n')
        # print(len(num_pool))

        rand_poke = random.choice(num_pool)
        chosen_num.append(rand_poke)

        # chosen_num을 업데이트
        with open('./chosen.txt', 'w') as f:
            for i in chosen_num:
                f.writelines(i + "\n")
        return chosen_num[-1]

