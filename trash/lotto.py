import requests
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


minDrwNo = 1  # 취득하고 싶은 회차 시작
maxDrwNo = 10000  # 취득하고 싶은 회차 종료
drwtNo1 = []  # 1등 첫번째 번호
drwtNo2 = []  # 1등 두번째 번호
drwtNo3 = []  # 1등 세번째 번호
drwtNo4 = []  # 1등 네번째 번호
drwtNo5 = []  # 1등 다섯번째 번호
drwtNo6 = []  # 1등 여섯번째 번호
bnusNo = []  # 1등 보너스 번호
drwNoDate = []  # 로또 추첨일
next_drw = 0  # 다음 회차

toto = 0
req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1000"
req_lotto = requests.get(req_url)
lottoNo = req_lotto.json()
print(lottoNo['returnValue'] == 'fail')

# 지정한 시작 회차 부터 종료 회차 까지 취득


def init():
    global next_drw
    for i in tqdm(range(minDrwNo, maxDrwNo + 1, 1)):

        # 1등 번호를 취득
        req_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=" + \
            str(i)

        req_lotto = requests.get(req_url)

        lottoNo = req_lotto.json()

        if(lottoNo['returnValue'] == 'fail'):
            next_drw = i
            return

        drwNoDate.append(lottoNo['drwNoDate'])  # 로또 추첨일
        drwtNo1.append(lottoNo['drwtNo1'])  # 1등 첫번째 번호 저장
        drwtNo2.append(lottoNo['drwtNo2'])  # 1등 두번째 번호 저장
        drwtNo3.append(lottoNo['drwtNo3'])  # 1등 세번째 번호 저장
        drwtNo4.append(lottoNo['drwtNo4'])  # 1등 네번째 번호 저장
        drwtNo5.append(lottoNo['drwtNo5'])  # 1등 다섯번째 번호 저장
        drwtNo6.append(lottoNo['drwtNo6'])  # 1등 여섯번째 번호 저장
        bnusNo.append(lottoNo['bnusNo'])  # 1등 보너스 번호 저장


def run():
    print('run')


init()

print(next_drw)
# 로또 1등 번호를 하나의 리스트로 머지
# 보너스 번호를 포함해 분석 하고 싶은 경우
# drwtNo6뒤에 bnusNo를 추가
# h = np.hstack((drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6))
# print(h)
# cnt = Counter(h)
# print(cnt)
# 결과 출력
# print(sorted(cnt.items(), key=lambda x: x[1], reverse=False))
