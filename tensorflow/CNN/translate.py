import os

rootPath = "D:\\English\\python\\tensorflow\\CNN\\Chapter06"

os.chdir("C:\\Users\\xie\\AppData\\Roaming\\Python\\Python36\\Scripts")
fileList = os.walk(rootPath)
for root, dirs, files in fileList:
    for val in files:
        if val.find(".ipynb") != -1:
            print("root:", root)
            print("dirs:", dirs)
            print("files:", files)
            try:
                os.remove(root + "\\" + val)
                print("delet:", root + "\\" + val)
            except Exception as e:
                print(e)

    # os.system("jupyter nbconvert --to script "+root+"\\"+"*.ipynb")
