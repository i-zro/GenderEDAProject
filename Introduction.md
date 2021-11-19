## 사용할 데이터 영역
`SE.TER.CUAT.BA.MA.ZS`  - Educational attainment, at least Bachelor's or equivalent, population 25+, female (%) (cumulative) : 25세 이상 여성 중 ‘학사’ 학위 이상을 가진 인구의 퍼센티지 데이터
<br>
`SE.TER.CUAT.BA.FE.ZS`  - Educational attainment, at least Bachelor's or equivalent, population 25+, male (%) (cumulative) : 25세 이상 남성 중 ‘학사’ 학위 이상을 가진 인구의 퍼센티지 데이터
<br>
`SG.VAW.ARGU.ZS` - Women who believe a husband is justified in beating his wife when she argues with him (%) : ‘여성이 남편에게 논쟁을 할 때 맞아도 된다’고 믿는
<br> 
`SG.VAW.BURN.ZS` - Women who believe a husband is justified in beating his wife when she burns the food (%) : ‘여성이 요리를 태웠을 때 남편에게 맞아도 된다’
<br>
`SG.VAW.GOES.ZS` - Women who believe a husband is justified in beating his wife when she goes out without telling him (%) : ‘여성이 말 없이 외출 시 남편에게 맞아도 된다.’ 
<br>
`SG.VAW.NEGL.ZS` - Women who believe a husband is justified in beating his wife when she neglects the children (%) : ‘여성이 아이들을 무시하면 남편에게 맞아도 된다’
<br>
`SG.VAW.REFU.ZS` - Women who believe a husband is justified in beating his wife when she refuses sex with him (%) : ‘여성이 성관계를 거부하면 남편에게 맞아도 된다
<br>
`SP.DYN.TFRT.IN` - Fertility rate, total (births per woman) : 여성 1명이 출산하는 아이의 수
<br>
`SP.ADO.TFRT` - Adolescent fertility rate (births per 1,000 women ages 15-19) : 15-19세 여성의 1000명이 출산하는 아이의 수
<br>
`SE.ENR.PRSC.FM.ZS` - School enrollment, primary and secondary (gross), gender parity index (GPI) : 초등 및 중등 교육에서 남아에 대한 여아 비율 (%)
<br>
`SP.DYN.CONU.ZS` - Contraceptive prevalence, any methods (% of women ages 15-49) : 15세 – 49세 사이 모든 방법을 사용한 여성의 피임 보급율
<br>
`SG.GEN.PARL.ZS` - Proportion of seats held by women in national parliaments (%) : 국회 여성 의석 비율(%)
<br>
`SL.AGR.EMPL.FE.ZS` - Employment in agriculture, female (% of female employment) (modeled ILO estimate) : 농업계의 여성 고용률
<br>
`SL.IND.EMPL.FE.ZS` - Employment in industry, female (% of female employment) (modeled ILO estimate) : 산업계의 여성 고용률
<br>
`SL.SRV.EMPL.FE.ZS` - Employment in services, female (% of female employment) (modeled ILO estimate) : 서비스업계의 여성 고용률
<br>
`SH.STA.SUIC.FE.P5`  - Suicide mortality rate, female (per 100,000 female population) : 여성의 100,000명당 자살률 데이터 
`NY.GDP.MKTP.CD` - GDP (current US$) : 1년동안 한 국가에서 생산된 재화와 용역의 시장 가치를 합한 것

### 탐색 / 파악하고자 하는 질문
1) ‘여성이 남편에게 맞아도 된다’라고 한 나라의 핵심 문제는 젠더 갈등을 넘어서, 자신에 대한 ‘폭력의 정당화’라는 생각이 들었기에 자존감 부재와 문화나 도덕적 지식 습득의 결여를 동시에 겪으려면 어느 정도의 `여성의 고등 교육이 주제와 연관관계는 있을 수도 있지 않을까?`하는 생각이 들어서, 여성의 학사 학위 분포와 해당 주제를 연결해 보려 합니다. 또, ‘여성과 남성의 학위 취득율이 모두 높은 나라, 남성의 학위 취득율만 높은 나라, 여성과 남성의 학위 취득율이 모두 낮은 나라를 비교하여 어떤 나라에서 가장 해당 주제의 퍼센티지가 높을까?’가 궁금하여, 이를 알아보려 합니다. 
2) 조금 극단적이지만, ‘이런 사고방식이 원인이 되어 여성의 자살률이 높을 수도 있지 않을까?’라는 생각이 들어서 이러한 인과 관계 여부를 분석해 보고 싶습니다.
3) 전세계 여성들의 총 출산율과 청소년의 출산율은 관계가 있을까요? 아이를 많이 낳는 나라는 청소년의 출산율도 높은지에 대해 분석해보고 싶습니다.
4) 여아의 취학률과 청소년의 출산율은 관계가 있을까요? 출산 때문에 학업을 연장하지 못하는 여아들이 많지 않을까요?
5) 여성의 피임보급률과 여성의 사회 진출의 (여성의 국회 의석 비율과 농업+산업+서비스업의 여성 취업률)은 관계가 있을까요?
6) 여성의 삶을 학위 취득 정도, 학업 진학 비율, 출산율, 사회 진출 등 다양한 지표를 하나로 합쳐 점수화 한 후 경제 발전의 대표 지표인 GDP와의 상관관계를 도출해봅니다.
7) 위 모든 분석을 끝난 후 다양한 시각으로 본 여성의 삶에 대해 정리한 후, 국가가 사회적, 경제적으로 발전 지표와 평등한 사회가 연관성이 있는지 결론을 내고 싶습니다.

