import pandas as pd
import numpy as np

df.shape

df.isnull().sum()

drop_col = df.isnull().sum()[df.isnull().sum()>35/100 * df.shape[0]]
drop_col





df.groupby(['Embarked'])['Survived'].mean()
