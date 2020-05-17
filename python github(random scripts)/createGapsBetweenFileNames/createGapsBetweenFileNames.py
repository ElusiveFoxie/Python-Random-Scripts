import os, shutil

path = r'C:\Users\mkacz\OneDrive\Desktop\python_guide\Creating_Gaps\files'
list = os.listdir(path)

print(list)

num = int(input("Where do you want to make a gap: "))


for i in range(len(list)-1,num-1,-1):
    if i < 9:
        Src = path + "\\" + list[i]
        Dst = path + "\\" + 'spam00' + str(i + 1) + '.txt'
        shutil.move(Src, Dst)
    elif i >= 9:
        Src = path + "\\" + list[i]
        Dst = path + "\\" + 'spam0' + str(i + 1) + '.txt'
        shutil.move(Src, Dst)


