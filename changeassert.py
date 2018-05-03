import os

'''files = os.listdir("D:\Assets")  # 列出当前目录下所有的文件


for filename in files:

    print(filename, end='\n')
    portion = os.path.splitext(filename)  # 分离文件名字和后缀

    if portion[1] == "":  # 根据后缀来修改,如无后缀则空
        newname = portion[0]+".jpg"  # 要改的新后缀
        # 切换文件路径,如无路径则要新建或者路径同上,做好备份
        os.rename(filename, newname)
# 这么写是行得通的，注意看转义\\
old_name = 'D:\Assets\\141fc006a606326e0763dc07ea04f04f1d71f0f4497b47b6841c36aa83c870fe'
new_name = 'D:\Assets\\141fc006a606326e0763dc07ea04f04f1d71f0f4497b47b6841c36aa83c870fe.jpg'
os.rename(old_name, new_name)'''

# 注意/和\的不同，在win下，路径名中的划线可以是\也可以是/
# 考虑到\需要转义，还是用/吧

files = os.listdir('D:/Assets')

for file_name in files:
    portion = os.path.splitext(file_name)

    if portion[1] == "":
        new_name = portion[0]+'.jpg'
        os.rename(file_name, new_name)
    else:
        pass
