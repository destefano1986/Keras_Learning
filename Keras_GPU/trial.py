# -*- coding: UTF-8 -*-
import pandas as pd

df = pd.read_csv('ROE.csv', encoding = 'gbk')
df1 = df.groupby(['证监会行业门类代码_Csrciccd1', '截止日期_Enddt'])['净资产收益率(摊薄)_ROE'].median()
df1.to_csv('ROE_median.csv', encoding = 'gbk')