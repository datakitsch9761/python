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