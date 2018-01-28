import glob, os
import fileinput

os.chdir("\\\\sdvnas\\TestCaseBase_Shiny4\\Skywalker\\TestCase\\USPI\\TestCase\\Easan\\")
for file in glob.glob("*.txt"): # 取指定目錄下的.txt檔
    print(file)

    fileOut = open("backup\\"+file, "w") # 寫入目標檔

    with open(file, 'r') as myfile:
        for line in myfile.readlines(): # 將.txt內逐行截取
            if line=="sck_freq = 16'h5dbd\n":
                line=line.replace('h5dbd', 'hbb7C') # 取代關鍵字
                print("|"+line+"|")

            fileOut.write(line)

    fileOut.close()