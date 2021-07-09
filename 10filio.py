# 파일 다루기


# 입력한 성적데이터를 파일에 저장하는 방법
fname = '/Users/josephlee/Desktop/data_sciencesungjuk.dat' #맥은 경로가 달라야한다

name = input('이름은')
kor = int(input('국어는? '))
eng = int(input('영어는? '))
mat = int(input('수학은? '))

f = open(fname, 'w') # 지정한 파일을 쓰기모드 엶
#data = 'Hello,World!!'
data = f'{name} {kor} {eng} {mat}' #파일에 기록할 내용을 문자열로 저장
f.write(data)
f.close()

#기록한 성적데이터를 파일로부터 읽어보기
f = open(fname,'r')
data = f.read()
print(data)
f.close()

#일정관리 프로그램
def saveMemo(memo):
    fname = '/Users/josephlee/Desktop/mymemo.txt'
    f = open(fname,'a') #추가 append 모드로 파일을 초기화
    f.write(memo + "\n")
    f.close()

def memoMain():
    memo = input('메모를 입력하세요 ')
    saveMemo(memo)

memoMain()

# py3 방식으로 파일 다루기
# 기존 파일 입출력 코드에서 불편한 점은
# 파일작업후에는 반드시 close를 해야한다는 것
# with문을 사용하면 명시적으로 close를 사용하지 않아도 됨
with open(fname, 'w') as f:
    f.write('blablabla~')

#파일에서 데이터 읽어오기
fname = '/Users/josephlee/Desktop/employees.csv'
with open(fname) as f:
     data = f.read() #모든 데이터를 한번에 다 읽어옴
     print(data)

with open(fname) as f:
    data = f.readline() # 데이터를 한줄 읽어옴
    print(data)

with open(fname) as f :
    data = f.readlines() # 모든 데이터를 라인단위로 읽어옴
    print(data)             # 읽어온 결과는 list 형식

# employees.csv 에서 사번, 이름, 입상일, 급여를 출력하세요
with open(fname) as f :
    f.readline()    #첫줄은 읽기만 함, 처리 X
    while True :
        line = f.readline()
        if not line: break #읽을 데이터가 없는 경우 작업 중단
        data = line.split(',') #문자열을 ,로 분리해서 리스트로 저장한다

        empno = data[0]
        name = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {name} {hdate} {sal:,}'
        print(emp)

#타이타닉 데이터셋을 이용해서
#승객이름 name, 성별 sex, age,embarked, survived
#추출해서 출력하세요
#단, survived가 0이면 '사망', 1이면 '생존'이라 출력함
#embarked가 S이면 'Southhampthon' Q이면 'Queenstown' C이면 Cherbourg,
fname = '/Users/josephlee/Desktop/titanic3b.csv'
with open(fname) as f:
    f.readline()
    while True:
        row = f.readline()
        if not row : break

        data = row.split(',')
        #name = data[2]
        sex = data[2]
        age = data[5]
        pos = data[9]
        live = data[1]

        if pos == 'S' : pos ='Southhampthon'
        elif pos == 'Q' : pos = 'Queenstown'
        elif pos == 'C' : pos = 'Cherbourg'

        if live =='0': live = '사망'
        elif live == '1': live ='생존'

        result = f'{name} {sex} {age} {pos} {live}'
        print(result)