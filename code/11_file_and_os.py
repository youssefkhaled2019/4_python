# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
# ======================os==============================
# import os 
# dir_path = os.path.dirname(os.path.realpath(__file__)) #pwd or '__file__'
# print(os.path.abspath(__file__) + "\n")#file path
# print( os.path.join(dir_path,"ccc.txt"))
# print(os.getcwd() + "\n")#pwd    #h:\2025\summary\4_python

# a = os.path.exists('D:\\00')  #folder 
# a = os.path.exists('D:\\1\\0.txt') # file 
# os.path.isfile("/etc/password.txt")

# os.remove(file_path) #removes a file.
# os.rmdir(file_path) #removes an empty directory.


# os.makedirs('D:\\1\\00' , exist_ok = True)



# import shutil as sh
# sh.copyfile( 'D:\\1\\1.txt', 'D:\\1\\00\\0.txt')#copy file
# sh.copytree('D:\\1\\00' , 'D:\\1\\33')#copy folder
# sh.move('D:\\1\\1.txt' , 'D:\\1\\33\\55.txt')# move file

# ========================glob============================


import glob as gb
# a = gb.glob(pathname= r'H:\2025\summary\4_python\code\*.*')# list of path file
b = gb.glob1(r'H:\2025\summary\4_python\code' , '*.*' ) #'*.pdf' #list name file 

# ====================================================
# a=open('xx.txt','w',encoding="utf8")
# a.write("xxxxxx\n nousdrr ")
# a.close()

# ====================================================

# f = open("demofile.txt", "rt")                             #Because "r" for read, and "t" for text are the default values, you do not need to specify them.
# dir_path = os.path.dirname(os.path.realpath(__file__)) #'__file__'
# file_path= os.path.join(dir_path,"demofile.txt")
# print(os.path.exists(file_path))
# ====================================================
# f = open("demofile.txt", "r")
# print(f.read()) #read all file 
# print(f.read(5)) # 5 first characters 
# print(f.readline()) #read on line 
# print(f.readlines())#lines in list 

# for x in f:
#   print(x) 

# f.close() 
# ====================================================
# f = open("demofile2.txt", "a")
# f.write("Now the file has more content!")
# f.close()

# ====================================================
# import os
# os.remove("demofile.txt") 

# #Check if File exist:
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# # Delete Folder
# os.rmdir("myfolder") 
# ====================================================
# import numpy as np 

# A=np.arange(0,100).reshape(10,10)
# A=str(A)
# p=r"H:\2025\Hesham Asem\slide_or_pdf\ML\1.csv"
# outfile = open(p, 'w')
# outfile.write(A)
# outfile.close()
# ====================================================

