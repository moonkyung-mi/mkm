# f = open('member.csv','w',encoding='utf-8')
#
# while True :
#     name = input('멤버 이름을 입력하세요. 종료하려면 이번 입력에서 quit를 입력하세요.')
#     if name == 'quit' :
#         break
#     birth = input('멤버 생년월일을 입력하세요.')
#     adr = input('멤버 주소를 입력하세요.')
#
#     mem = name+','+birth+','+adr+'\n'
#     f.write(mem)
#
# f.close()

with open('test3.txt','w',encoding='utf-8') as f:
    f.write('가나다')
