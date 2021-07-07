# 파이썬 리스트

attendList = ['순철','병헌','민우','찬호','민태']
print(attendList)

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

complex = [1, 2.0, 3.1415, 40, '5', "6"]
print(complex)

for data in numbers:   # iterable
    print(data)

for data in complex:  # iterable
    print(data)

len(numbers)
len(complex)

msg = 'Hello, World!!'
print(len(msg))

# 메세지 입력받고 문자열 길이 출력
msg = input('메세지를 입력하세요 ')
print(f'입력한 문자열의 길이 : {len(msg)}')

print(len(['Hello, Python!!']))
print(len('Hello, Python!!'))

# 리스트의 모든 항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])

for i in range(len(complex)):
    print(complex[i])

for item in complex:
    print(item)

for idx, item in enumerate(complex):
    print(f'{idx}, {item}')

print(complex.index(3.1415))


sports = ['baseball','basketball','tennis','golf','soccer']
print(sports.index('soccer'))
print(sports[len(sports)-1])

lang = ['C/C++','c#','python','java']
print(lang.index('python'))

hobby = ['독서' , '등산' , '요리']
hobby.append('배구')

print(hobby)


number = [1, 2, 3, 4, 5, 7, 8, 9]
number.append(10)
number.insert(5, 6)
print(number)


weather = ['The','weather','very']
weather.insert(2, 'is')
weather.insert(4, 'cold')


# 성적처리 프로그램 - 3명 학생데이터 입력후
# 총점, 평균, 학점 처리 후 결과 출력
names = []
kors = []
engs = []
mats = []

for i in range(3):
    name = input('이름은? ')
    names.append(name)
    kor = int(input('국어는? '))
    kors.append(kor)
    eng = int(input('영어는? '))
    engs.append(eng)
    mat = int(input('수학은? '))
    mats.append(mat)

tots = []
avgs = []
grds = []
for i in range(3):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)
    grds.append('가')
    if avgs[i] >= 90: grds[i] = '수'
    if avgs[i] >= 80: grds[i] = '우'
    if avgs[i] >= 70: grds[i] = '미'
    if avgs[i] >= 60: grds[i] = '양'

for i in range(3):
    print(f'{names[i]}, {kors[i]},{engs[i]},{mats[i]}\n'
          f'{tots[i]}, {avgs[i]}, {grds[i]}\n')



# 리스트 수정
# 리스트[인덱스] = 수정할값
hobby
hobby[1] = '여행'
hobby


# 리스트 삭제
# pop : 맨뒤의 항목을 제거
# pop(위치) : 해당 위치의 항목을 제거
hobby
hobby.pop()

sports
sports.pop(2)


# remove : 항목값으로 제거
lang
lang.remove('java')
lang.remove('C/C++')

# 과일 리스트에서 야채 삭제하기
fruits = ['사과', '망고','당근','수박','포도','참외','토마토']

#위치값으로 삭제
fruits
fruits.pop(2)

fruits.pop(5)
fruits

#값으로 삭제하기
fruits = ['사과', '망고','당근','수박','포도','참외','토마토']

fruits.remove('당근')
fruits.remove('토마토')
fruits

#공인중개사 합격여부 알아보기
exam = [55,65,40,70,65,30]
exam = [55,60,40,70,65,70]

cnt = int(len(exam))
sum = 0
fails = 0
result = '아쉽습니다. 불합격하셨습니다.'

for i in range(cnt) :
    if exam[i] < 40 : fails += 1 #과락 과목수 증가
    sum += int(exam[i])

avg = sum / cnt
if fails == 0 and avg >= 60 :
    result = '축하합니다. 합격하셨습니다 '

print(f'평균점수 : {sum / cnt : .2f}')
print(result)

#정렬하기
numbers = [5,1,3,4,2,6]

numbers.sort() #기본값이 False
numbers

numbers.sort(reverse=True)
numbers #True를 적용한 후에 내림차순

#모의고사 점수 내림차순으로 정렬하기
mockexam = [90,100,88,85,95,92,70,75,100,92,78,80,75,95,90,100,84]
mockexam.sort(reverse=True)
mockexam

#문자 정렬 (한글)
names = ['김길동', '박길동', '이길동','정길동','홍길동']
names.sort(reverse=True)
names

#문자 정렬 (영어)
units = ['scv','marine','firebat','ghots','dropship','battlecruiser','valkyrie','medic']
units.sort()
units


#리스트 슬라이싱
alphabet = ['a','b','c','d','e','f','g','h','i','j']
alphabet[2:6]
alphabet[0:5]
alphabet[:5]
alphabet[3:8] # 3 ~  7 까지
alphabet[5:10] # 5 ~ 끝까지
alphabet[5:] # 5 ~ 끝까지

alphabet[6:] #6 ~ 끝까지 추출
alphabet[-4:] #오른쪽을 기준으로 왼쪽으로 4번째 요소를 시작으로

# a b c d e
# 1 2 3 4 5
# -5 -4 -3 -2 -1

# a,b,c,d 추출
alphabet[0:4]
alphabet[:4]
alphabet[:-6]

# d c b ,a 추출
alphabet[-7:-11:-1]
alphabet[:-3:-1]

# g,h,e,d 추출
