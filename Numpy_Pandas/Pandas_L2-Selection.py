#coding=utf-8
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""
# -------------------------------------------
# 简单筛选
# 筛选列， 使用 列名
print(df['A'])
print(df.A)
"""
2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int64
"""

# 筛选行， 使用index的 切片（序列或名称） 
print(df[0:3])
"""
            A  B   C   D
2013-01-01  0  1   2   3
2013-01-02  4  5   6   7
2013-01-03  8  9  10  11
"""
print(df['20130102':'20130104'])
"""
A   B   C   D
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
"""

# -------------------------------------------
# 根据标签 loc
# 规则： 先行后列，逗号分割，列可选. 
# 行只可用单个或切片形式；列可用单个,数组，或切片形式
print(df.loc['20130102'])
"""
A    4
B    5
C    6
D    7
Name: 2013-01-02 00:00:00, dtype: int64
"""
print(df.loc[:,['A','B']]) 
"""
             A   B
2013-01-01   0   1
2013-01-02   4   5
2013-01-03   8   9
2013-01-04  12  13
2013-01-05  16  17
2013-01-06  20  21
"""
print(df.loc['20130102',['A','B']])
"""
A    4
B    5
Name: 2013-01-02 00:00:00, dtype: int64
"""

# -------------------------------------------
# 根据序列 iloc
# 规则： 先行后列，逗号分割，列可选. 
# 行和列均可分别使用 单个,数组，或切片形式
print(df.iloc[3,1])
'''
13
'''
print(df.iloc[3:5,1:3])
"""
             B   C
2013-01-04  13  14
2013-01-05  17  18
"""
print(df.iloc[[1,3,5],1:3])
"""
             B   C
2013-01-02   5   6
2013-01-04  13  14
2013-01-06  21  22
"""

# -------------------------------------------
# 混合 ix
print(df.ix[:3,['A','C']])
"""
            A   C
2013-01-01  0   2
2013-01-02  4   6
2013-01-03  8  10
"""

# -------------------------------------------
# 条件筛选(Boolean indexing)
print(df[df.A>8])
"""
             A   B   C   D
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""