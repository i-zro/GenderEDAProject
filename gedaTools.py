# 데이터프레임의 time(연도) 'YR~' string을 int64로 바꿔주는 메서드
def timeToInt(df):
    df = df['time'].apply(lambda x : int(x[2:]))
    return df