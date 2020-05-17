import os, re, shutil

path = r'C:\Users\mkacz\OneDrive\Desktop\python_guide\Filling_in_the_Gaps\files'
list = os.listdir(path)
list2 = []

for i in range (len(list)):
    try:
        if i < 10:
            IRegex = re.compile('spam00'+str(i)+'.txt')
            find = IRegex.match(list[i])
            if find == None:
                list2.append(i)
        elif i >= 10:
            IRegex = re.compile('spam0' + str(i) + '.txt')
            find = IRegex.match(list[i])
            if find == None:
                list2.append(i)
    except IndexError:
        print('noMore')

for i in list2:

    if i < 10:
        shutil.move(path + "\\" + list[i], path + "\\" + 'spam00'+str(i)+'.txt')
    elif i >= 10:
        shutil.move(path + "\\" + list[i], path + "\\" + 'spam0' + str(i) + '.txt')

