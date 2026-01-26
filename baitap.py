#Viết chương trình đếm số lượng ký tự trong chuỗi 
# currency = "abcde"
# counts = 0
# for letter in currency:
#     counts = counts + 1
# print(counts)



#Viết chương trình nhập một chuỗi và in ra các ký tự ở vị trí chẵn của chuỗi đó
# strings = "abcdxyz"
# position = 0
# for letter in strings:
#     if position % 2 == 0:
#         print(letter)
#     position = position + 1 
# strings = "abcdxyz"
# for index in range(0, len(strings)):
#     if index % 2 == 0:
#         print(strings[index])
# strings = "abcdxyz"
# position = 0
# while position < len(strings):
#     if position % 2 == 0:
#         print(strings[position])
#     position = position + 1

# name = 'vinh'

# positioninput = input('Enter position: ')
# letterinput = input('Enter letter: ')
# ipos = int(positioninput)
# firstname = name[0:ipos:1]
# lastname = name[ipos + 1: len(name): 1]
# overallname = firstname + letterinput + lastname
# print(overallname)

#2) Nhập 1 chuỗi, nhập  n. Biến n ký tự đầu thành số 0 
#Ví dụ: Nhập chuỗi “camvinh”-  nhập n= 3 ==> Kết quả là “000vinh”

# strings = "camvinh"
# ninput = input('letter:')
# ininput = int(ninput)
# inpos = "0"*ininput
# print(inpos)
# last = strings[ininput :len(strings):1]
# result = inpos + last
# print(result)

# 3) Viết chương trình kiểm tra số đó có phải là số tuyệt vời không ( số tuyệt vời là số khi đảo ngược sẽ bằng chính nó )
# str = '121'
# reversedstr = ""
# for index in range(len(str)-1, -1,-1):
#     reversedstr = reversedstr + str[index]
# if reversedstr != str:
#     print("số không tuyệt vời")
# elif reversedstr == str:
#     print("số tuyệt vời")
# inputstr = input("cho số bất kỳ:")
# reversedstr = ""
# index = len(inputstr) -1
# while index >= 0:
#     num = inputstr[index]
#     # print(index, num)
#     reversedstr = reversedstr + inputstr[index]
#     index = index - 1
# if reversedstr != inputstr:
#     print("số không tuyệt vời")
# elif reversedstr == inputstr:
#     print("số tuyệt vời")

# 4) In ra màn hình ( For/ WHile )
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# star = '*'


# # for index in range(1,6):
# #     print(index*star)
# # for index in range(4,0,-1):
# #     print(index*star)

# index = 1
# while index <= 5:
#     print(index*star)
#     index = index + 1
# index = 4
# while index >= 1:
#     print(index*star)
#     index = index - 1 
    
# 5) Viết chương trình in ra ( For/ While )
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
 
#toi dag index = 1

# for index in range(1,10,1):
#     for mult in range (1,index + 1,1):
#         print(index,end='')
#     print()

# for index in range(1,10,1):
#     print(index*str(index))
# num = 1
# while num <=9:
#     print(num * str(num))
#     num = num + 1
def solve(row):
    global count
    if row == 8:        # all 8 queens placed
        count += 1     # found ONE valid solution
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve(row + 1)
 

        
    
        


    



    
    



    













  
 
















        
