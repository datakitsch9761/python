num1 = 10
num2 = 20
num3 = num1 + num2 #정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2 #실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2 #정수 + 실수 = 실수

#매출액 구하기
# month1 = int(input('1월 매출'))
# month2 = int(input('1월 매출'))
# month3 = int(input('1월 매출'))
#
# quarter1 = month1 + month2 + month3
# print('1분기 전체 매출 : {0} %'.format(quarter1))
#
# num1 = 3.14
# num2 = 0.25
# num3 = num1 + num2
# float(num3)
# int(num3)

#이익 구하기
# sales1 = int(input('1분기 매출은?'))
# buy1 = int(input('1분기 매입은?'))
#
# profit = sales1 - buy1
# print('1분기 이익 : {0}원'.format(profit))

#방 너비 구하기
# width = int(input('방 가로크기는? '))
# height = int(input('방 세로크기는? '))
#
# area = width * height
# print('방 너비 {0} square foot'.format(area))
#
# str1 = 'hello world!!'
# str1 * 3
# 3 * str1
# 3 * str1 * 2

# BMI 구하기
# 18.5 : 저체중
# 23 : 정상
# 25 : 과체중
# 30 : 비만
# 30 이상 : 고도 비만
# weight = int(input('몸무게는 ? '))
# height = float(input('신장은 ? '))
# height = height/100
#
# bmi = weight / (height * height)
# print('BMI :{0:.2f} BMI'.format(bmi))
# print(f'BMI :{bmi:.2f} BMI') #f-string 기능 을 활용 -> py 3.6부터 지원하는 기능

# print 출력 속도 :  .format -> % -> f-string (순서대로 속도가 빠르다)

# 동전 갯수 알아보기
# coins = int(input('손안의 동전 수를 입력하세요'))
#
# isEven = coins % 2;
# print(f'동전의 홀짝여부 (0:짝) {isEven}')



#빵 나누어 주기
#빵, 나눠줄 빵 갯수 입력 받음
#최대 몇명까지 나눠 줄 수 있는지와 남는 빵 갯수 출력
# bread = int(input('빵의 총 갯수는?'))
# div = int(input('나눠줄 빵의 갯수는 ?'))
#
# student = bread // div
# divmod = bread % div
#
# print(f'{bread}개의 빵은 {div}개 씩, {student}명의 학생에 나눠줄 수 있고,')
# print(f'{divmod}개의 빵이 남음')

# 은행 복리 계산기 만들기
# 원금, 유치기간, 연이율을 입력받아 복리계산 후 총 수령액 출력

# money = 5_000_000
# duration = 5
# interest = 5.0
#
# takes = money + (money * 0.05) #1년 차
# # takes = takes + (takes * 0.05) #2년 차
# takes += takes * 0.05
# # takes = takes + (takes * 0.05) #3년 차
# takes += takes * 0.05
# # takes = takes + (takes * 0.05) #4년 차
# takes += takes * 0.05
# # takes = takes + (takes * 0.05) #5년 차
# takes += takes * 0.05

# 범퍼카 탑승 가능 신장 확인하기
# height = int(input('본인의 신장을 입력해주세요'))
# isRide = height > 120
# print(f'탑승 가능여부 : {isRide} (True : 탑승 가능한 신장입니다)')

'a' == 'b'
'a' > 'b' #아스키 코드로 변환 후 비교 한 값이기 때문에 'a'가 더 큰걸로 나오는 경우

# 범퍼카 탑승 가능 신장 확인하기
# height = int(input('본인의 신장을 입력해주세요'))
# # isRide = height > 120 and height < 170
# isRide = 120 < height < 170 #해당 수식 파이썬에서 지원하는 방식
# print(f'탑승 가능여부 : {isRide} (True : 탑승 가능한 신장입니다)')

# 범퍼카 탑승 가능 신장 확인하기
# height = int(input('본인의 신장을 입력해주세요'))
# # isRide = height > 120 and height < 170
# isRide = 120 < height < 170 #해당 수식 파이썬에서 지원하는 방식
# print(f'탑승 가능여부 : {isRide} (True : 탑승 가능한 신장입니다)')
#
# temp = 0
# temp <= 16 or temp > 28

# short circuit evaluation
# num1 = 17
# num2 = 20
# (num1 < 15) and (num2 > 15) #False and True -> FALSE 답이 바로 나온다
#
# num1 = 10
# num2 = 20
# (num1 < 15) or (num2 < 15) #True and False -> True 답이 바로 나온다
#
# (num1 < 5) and xyz

# 삼항 연산자
# 참값때 값 if 조건식 else 거짓일때 값
# num = 10
# '짝수' if (num % 2 == 0) else '홀수'

#  적자 흑자 판단하기
# income = int(input('수입은?'))
# outcome = int(input('지출은?'))
# '흑자' if(income > outcome) else '적자'

# 윤년 여부 알아보기
# 4로 나눠 떨어지고 100으로 나눠 떨어지지 않음
# 400으로 나줘 떨어짐
# year = int(input('년도는 ? '))
# isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 ==0 )
# result = '윤년' if (isLeap) else '평년'
# print(result)


# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램을 작성해보세요

# 키보드로 정수를 하나 입력받아 그 값이 정수, 음수, 0인지 구분하는 프로그램을 작성하시오. 각각의 경우에 따라 “정수입니다”, “음수입니다”, “0입니다”라고 출력하도록 한다.

# 지금 현재 수지의 통장잔액이 25,000원이다. 은행이자가 연 6%라 가정할 때, 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지 알아보는 프로그램을 작성하세요