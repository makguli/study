""" 웹스크래핑 샘플
from bs4 import *
import requests
    
url = "https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
txt = soup.find("div", attrs = {"class", "win_result"}).get_text()
result = txt.split("\n")
#print(len(result), result, result[7:13], result[19])
print("{0} 번호 {1}입니다. 보너스 번호는 {2}입니다.".format(result[1], result[7:13], result[17]))
"""

"""
HumanA = 20000000
HumanB = 45000000
HumanC = 25000000

rateA = 2.99/100
rateB = 3.90/100
rateC = 1.79/100

Weighted_Average_Rate = (HumanA*rateA+HumanB*rateB+HumanC*rateC)/(HumanA+HumanA+HumanA)
print("가중평균금리 = {}".format(Weighted_Average_Rate))
"""

from dataclasses import dataclass

@dataclass
class debt_ratio:
    debt : float = None
    rate : float = None


yejin = debt_ratio()
yejin.debt = 1000000000.0
yejin.rate = 4.1/100.0

yesung = debt_ratio()
yesung.debt = 2000000000.0
yesung.rate = 3.5/100.0

yeshin = debt_ratio()
yeshin.debt = 25000000.0
yeshin.rate = 1.79/100.0

print("산술평균 금리 : {0:.03%}".format( (yejin.rate+yesung.rate+yeshin.rate)/3.0) )

total = (yejin.debt*yejin.rate + yesung.debt*yesung.rate + yeshin.debt*yeshin.rate)/(yejin.debt + yesung.debt + yeshin.debt)
print("가중평균 금리 : {0:.03%}".format(total))