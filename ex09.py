
# 생존율 출력 프로그램
msg = '최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요 '
time = int(input(msg))

live = 25
if time > 360: live = 25
elif time > 300: live = 47
elif time > 240: live = 57
elif time > 180: live = 66
elif time > 120: live = 76
elif time > 60: live = 85
else: live = 90

print(f'생존율 : {live} %')