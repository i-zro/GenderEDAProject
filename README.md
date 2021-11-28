### 데이터 프레임 내 Index 없애고 싶을 때
![Image](https://i.imgur.com/KNg7ml9.png)
(economy 부분이 index인 상황, <br>
그래서 원하는 방향으로 그래프가 안그려지고 있었음)

```
: reset_index() 사용
```

## femAdoFer.ipynb
3번

## priAdoFer.ipynb


![Image](https://i.imgur.com/Z5OajgQ.png)

# wbgapi 관련
### skipBlanks=True
빈 연도, 나라 제거하고 시작

# 데이터 프레임 처리 관련
### dropna
NaN값 하나라도 있으면 해당 행 지우기

### 결측치로만 채워진 열 제거
`dropna(axis=1, how='all')`

https://data-newbie.tistory.com/564

https://github.com/iNeuronai/EDACollection/blob/master/FitBit/FitBit%20EDA.ipynb

![Image](https://i.imgur.com/nfS13oM.png)

'ARGU', 'BURN', 'GOES', 'NEGL', 'REFU']

ecoDF = wb.economy.DataFrame()
ecoR = ecoDF.reset_index()
ecoR

vawE = ecoR[ecoR.id.isin(conList)]
vawE

## matplotlib 한글 출력
```python
# 사용자 운영체제 확인
import platform
platform.system()
# 운영체제별 한글 폰트 설정
if platform.system() == 'Darwin': # Mac 환경 폰트 설정
    plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': # Windows 환경 폰트 설정
    plt.rc('font', family='Malgun Gothic')

plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정


# 글씨 선명하게 출력하는 설정
%config InlineBackend.figure_format = 'retina'
```

