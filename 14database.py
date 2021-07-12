# sqlite를 이용한 데이터베이스 활용하기
import sqlite3

# 데이터 조회
# 데이터베이스 연결
conn = sqlite3.connect('c:/java/sqlite3/siestageek.db')

# 접속후 커서를 가져옴
cur = conn.cursor()

# 질의문 작성
sql = 'select pcode, pname, price, amount from product'

# 질의문 실행후 결과집합 가져오기
# 결과집합은 리스트 형태로 저장
cur.execute(sql)
rows = cur.fetchall()

# 리스트 내용 출력하기 I
for row in rows:
    print(row[0], row[1], row[2], row[3])

# 리스트 내용 출력하기 II
# 리스트를 컬럼명으로 출력하려면 커서모드는 dictCursor 이용
# 단, sqlite3은 미지원
# for row in rows:
#     print(row['pcode'], row['pname'], row['price'], row['amount'])

# 작업종료
cur.close()
conn.close()


# mysql를 이용한 데이터베이스 활용하기
import pymysql

conn = pymysql.connect(host='bigdata.cfedxhiyqmff.ap-northeast-2.rds.amazonaws.com',
                       charset='utf8', user='playground',
                       password='bigdata2020', db='playground')

# 결과집합 출력시 dict 형식으로 리스트를 다룰 수 있음
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from EMPLOYEES'
cursor.execute(sql)
rows = cursor.fetchall()

cursor.close()
conn.close()

for row in rows:
    print(row['EMPLOYEE_ID'], row['FIRST_NAME'], row['LAST_NAME'])


# 직책이 IT_PROG인 사원들의 사번, 성, 입사일을 출력하는 코드 작성



# 30번 부서의 사원수를 조회하는 코드 작성