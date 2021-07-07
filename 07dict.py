#딕셔너리
ages = {'박찬호':48,'박지성':40,
        '박세리':50, '이승엽' : 43}

type(ages)

person = {'이름':'홍길동', '나이':25,'몸무게':88.8,
          '주소': '서울 종로구 삼일대로',
          '취미': ['운동','독서','영화감상']}

#확인 문제 1
sungjuk = {'C/C++':'A','JAVA':'B+','네트워킹':'C','보안':'A+','해킹':'F','시스템':'C+'}

#홍길동의 나이와 취미 조회

#홍길동의 혈행형 추가
#dict에 새로운 항목을 추가할때는
#새로운키와 값으로 정의해야함
person['혈행형'] = 'A'

#dict 모든 항목 출력
person = {'이름':'홍길동', '나이':25,'몸무게':88.8,
          '주소': '서울 종로구 삼일대로',
          '취미': ['운동','독서','영화감상']}

for key in person.keys():
    print(person[key])

#dict의 키와 값 모두 가져오기 : items
person = {'이름':'홍길동', '나이':25,'몸무게':88.8,
          '주소': '서울 종로구 삼일대로',
          '취미': ['운동','독서','영화감상']}

person.items()

for k,v in person.items(): #k = key / v = value
    print(k,v)

#중간고사 성적 관리
midsj = {'C/C++':'A','JAVA':'B+','네트워킹':'C',
         '보안':'A+','해킹':'F','시스템':'C+'}

midsj['JAVA']
midsj['시스템']

midsj['파이썬'] = 'A'
midsj['OS'] = 'A+'

midsj['JAVA'] = 'F'
midsj['시스템'] = 'A'

for k,v in midsj.items():
    print(f'{k},{v}')

#딕셔너리 for 축약문
#이름과 성적 리스트를 dict 객체로 재 생성하세요
name = ['혜교','지현','수지'] #키
grd = ['수','양','미'] #값
sj = {}

#반복문을 사용하지 않음
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

#반복문을 사용
for i in range(3):
    sj[name[i]] = grd[i]

#Comprehension version for 축약문
# {키/값 표현식 for 키,값 in zip(반복가능객체,반복가능객첸)}
sj2 = {key : val for key, val in zip(name,grd)}
sj2

#zip : 여러개의 데이터를 하나로 합쳐서
#iterable한 객체로 생성해 줌 - 개별 객체는 튜플로 반환
for pair in zip(name,grd):
    print(pair)