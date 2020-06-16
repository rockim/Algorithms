score = []
temp = 0
for i in range(10):
    a = int(input())
    temp += a
    score.append(temp)
    
for i,mush in enumerate(score):
    if mush > 100:
        min_mush = i
        break
    if i == 9:
        min_mush = 9

if abs(score[min_mush]-100) > abs(score[min_mush-1]-100):
    print(score[min_mush-1])
else:
    print(score[min_mush])
