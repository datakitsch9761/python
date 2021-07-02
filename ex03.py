# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 출력하는 프로그램 구하기
name = input('이름은?')
kor = int(input('국어 점수는'))
eng = int(input('영어 점수는'))
mat = int(input('수학 점수는'))

tot = kor + eng + mat
avg = tot / 3

print(tot)
print(avg)
print(grd)

# 조건문을 작성합니다
if (avg > 90):print('수')
elif 90>= avg >80:print('우')
elif 80>= avg >70:print('미')
elif 70>= avg >60:print('양')
elif 60>= avg >50:print('가')
