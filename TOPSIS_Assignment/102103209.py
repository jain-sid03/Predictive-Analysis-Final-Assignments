# -*- coding: utf-8 -*-
"""learning-mcdm-using-topsis(1).ipynb

Automatically generated by Colaboratory.

---
# **Multi-criteria decision making (MCDM) using Topsis**
---
- MCDM refers to select the best choice, having multiple-conflicting-criteria.
- Topsis helps to generate single score to make the decision

---
## **1.1 Installing topsis library**
---
"""

install.packages('topsis')

"""---
## **1.2 Import the library**
---
"""

library(topsis)

"""
## **1.4 Read the dataset**
---"""

dataset=read.csv('/kaggle/input/practise-mcdm-using-topsis/Topsis-Dataset.csv')
dataset

write.csv(dataset,file="/kaggle/working/102103189-data.csv")

"""---
## **1.5 Convert the dataset to Matrix**
---
"""

d <- as.matrix(dataset[,-1]) # -1, drop 1st column
d

"""---
## **1.6 Assigning the impacts**
---
"""

i <- c("+", "+", "-", "+")
i

"""---
## **1.7 Assigning the weights**
---
"""

w <- c(1,1,1,1)
w

"""---
## **1.8 Calling the topisis function**
---
"""

topsis(d, w, i)

"""---
## **2. Complete Code**
---
"""

library(topsis)
dataset=read.csv('/kaggle/input/practise-mcdm-using-topsis/Topsis-Dataset.csv')
dataset
d <- as.matrix(dataset[,-1]) # -1, drop 1st column
i <- c("+", "-", "+", "-")
w <- c(2,2,3,3)
topsis(d, w, i)

