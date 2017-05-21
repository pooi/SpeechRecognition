class Test:
    def printA(self):
        print("a")

    def test1(self, index, list):
        count = 0
        for i in range(len(list)):
            c = abs(list[i])
            if c <= 25:
                count += 1

        print("sample 25 이하 비율 | ", index, " | percentage : ", round(count/len(list)*100, 2), "%")

    def test2(self, index, list):
        sum = 0
        sum1 = 0
        sum2 = 0
        for i in range(len(list)):
            if i < len(list)/2:
                sum1 += abs(list[i])
            else:
                sum2 += abs(list[i])
            sum += abs(list[i])

        print("좌우 sample 비율 | %d | sum1 : %5.2f %% | sum2 : %5.2f %%"
              %(index, round(sum1/sum*100, 2),round(sum2/sum*100, 2))
              )

    def test3(self, index, list, area):

        total = len(list)*200
        print("전체 면적 대비 넓이 비율 | %d | percentage : %5.2f %%"
              %(index, round(area/total*100, 2))
              )

    def test4(self, index, list):
        sum = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for i in range(len(list)):
            c = abs(list[i])
            if i < len(list)*1/3:
                sum1 += c
            elif i < len(list)*2/3:
                sum2 += c
            else:
                sum3 += c
            sum += c

        print("3등분 후 sample 비율 | %d | sum1 : %5.2f %% | sum2 : %5.2f %% | sum3 : %5.2f %%"
              %(index, round(sum1/sum*100, 2), round(sum2/sum*100, 2), round(sum3/sum*100, 2))
              )

    def test5(self, index, list):
        sum = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0
        for i in range(len(list)):
            c = abs(list[i])
            if i < len(list)*1/5:
                sum1 += c
            elif i < len(list)*2/5:
                sum2 += c
            elif i < len(list)*3/5:
                sum3 += c
            elif i < len(list)*4/5:
                sum4 += c
            else:
                sum5 += c
            sum += c

        print("5등분 후 sample 비율 | %d | sum1 : %5.2f %% | sum2 : %5.2f %% | sum3 : %5.2f %% | sum4 : %5.2f %% | sum5 : %5.2f %%"
              %(index, round(sum1/sum*100, 2), round(sum2/sum*100, 2), round(sum3/sum*100, 2), round(sum4/sum*100, 2), round(sum5/sum*100, 2))
              )

    def test6(self, index, list):
        sum = 0
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum5 = 0
        for i in range(len(list)):
            c = abs(list[i])
            if i < len(list)*1/5:
                sum1 += c
            elif i < len(list)*2/5:
                sum2 += c
            elif i < len(list)*3/5:
                sum3 += c
            elif i < len(list)*4/5:
                sum4 += c
            else:
                sum5 += c
            sum += c

        left = sum1/sum*100
        right = sum5/sum*100

        print("5등분 후 좌우 sample 비율 10% 미만 | ", index, " | ", end='')
        if left < 10 and right < 10:
            print("좌, 우")
        elif left < 10:
            print("좌")
        elif right < 10:
            print("우")
        else:
            print("X")