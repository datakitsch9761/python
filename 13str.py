# 문자열은 문자들의 리스트와 유사
# 따라서 리스트 슬라이싱을 통해 개별 문자열의 각 문자를 추출할 수 있음

# '파이썬은완전재미있어요'라는 문자열에서
#  홀수 위치에 있는 문자를 #'로 출력하는 코드 작성

str = '파이썬은완전재미있어요'
print(str)

for i in range(len(str)):
    if i % 2 == 0 :
        print(str[i], end='') #end = ''를 붙여서 줄 바꿈이 없게 한다
    else :
        print('#', end='')
print()

# 거꾸로 출력하는 글자문 연습해보기!!
inStr, outStr = "",""
count, i = 0,0

inStr = input('문자열을 입력하세요 :')
count = len(inStr)

for i in range(0,count):
    outStr += inStr[count - (i+1)]
print("내용을 거꾸로 출력 --> %s" %outStr)

# 문자열 함수
# 대소문자 변환
str = 'Python is Easy. 그래서 programming이 재미있어요'
str.lower() #소문자
str.upper() #대문자
str.swapcase() #첫글자 소문자
str.title() #첫글자 대문자

# 문자열 찾기
str = '파이썬 공부는 즐겁습니다 물론 모든 공부가 다 재미있지는 않죠 ^^'

str.count('공부') #특정 문자열 존재 갯수를 알려준다
str.find('공부')  #문자열을 찾은 위치(왼쪽기준)
str.find('공부',5)  #특정 인덱스를 시작으로 문자열을 찾은 위치(왼쪽기준)
str.find('공부',str.find('공부')+1)
str.find('없다') #찾지 못하는 경우 : -1
str.rfind('공부') #문자열을 찾은 위치(오른쪽 기준)

str.index('공부')
str.index('공부',5)
str.rindex('공부')
str.index('없다') #찾지 못하는 경우 : 오류가 발생한다!

str.startswith('파이썬') # 특정 문자열로 시작하는지 여부
str.startswith('파이썬',10) # 특정 인덱스 이후로 특정 문자열로 시작하는지 여부
str.startswith('물론',14)
str.endswith('^^') # 특정 문자열로 끝나는지 여부


# 문자열내 공백 다루기
str = ' 파  이  썬   '
str.strip() #공백제거 : 매개변수 없음
str.rstrip()
str.lstrip()

str = '--파---이---썬--'
str.strip('-') # 지정문자 제거 : 매개변수로 제거할 문자 지정
str.rstrip('-') #오른쪽 끝
str.lstrip('-') #왼쪽 끝

str = '<<파 << 이 >> 썬>>'
str.strip('<>') # 지정문자들 제거 : 매개변수로 제거할 문자 지정
str.rstrip('<>')
str.lstrip('<>')

str = '열심히 파이썬 공부중 ~'
str.replace('파이썬','Python') #지정한 문자열을 새로운 문자열로 바꿈

str = ' 파  이  썬   '
str.replace(' ', '')

str = '--파---이---썬--'
str.replace('--','')

str = '<<파 << 이 >> 썬>>'
str = str.replace('<','')
str = str.replace('>','')
str.replace(' ','')

#문자열 분리 결합
str = '혜교, 98,65,77' #구분기호로 문자열을 분리하고 리스트로 저장
str.split(',')

str = '혜교|98|65|77'
str.split('|')

str = '혜교\r\n98\r\n65\r\n77'
str.split('\r\n') #줄바꿈 기호 기준 문자열 분리
str.splitlines()

str = ['혜교', '98','65','77']
','.join(str) #리스트의 각 항목을 구분기호로 합침

result = '' #join을 사용하지 않은 경우
for s in str:
    result += s + ','


#객체를 특정 함수에 일괄적으로 적용하기
#map(적용할 함수명, 대상객체)
str = ['123','456','789'] #문자열을 숫자로 변경

nums = [] #map을 사용하지 않는 경우 ㄴ
for s in str :
    nums.append(int(s))

nums = list(map(int,str))

#문자열 정렬하기

#특정 문마로 채우기

#문자열 구성 파악하기

# 입력한 값이 영어/한글이면 '글자', 숫자면 '숫자', 섞여있으면 '글자 + 숫자',
# 그외 나머지 문자면 '모르겠습니다'라고 출력하는 프로그램
str = input('문자열 입력')

result = ''
if str.isalpha():
    result = '글자입니다'
elif str.isdigit():
    result = '숫자입니다'
elif str.isalnum():
    result = '숫자입니다'
else :
    result = '모르겠습니다'

print(result)


