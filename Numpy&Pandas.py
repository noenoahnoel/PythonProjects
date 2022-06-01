import numpy as np 

#defining a list, then creating an array from that list
list1 = [50, 60, 80, 100, 200, 300, 500, 600]

first_array = np.array(list1) 
type(first_array) 

#defining multi-dimensional arrays(matrix)
matrix1 = np.array([ [2,5,8], [7,3,6]])
matrix2 = np.array([ [3,7,9,3], [4,3,2,2]])

##Numpy built-in methods and functions## 

#rand() uniform distribution between 0 and 1 
x = np.random.rand(20)

#rand() on a matrix
x2 = np.random.rand(3,3)

#randint()
#generate a random int between the given range
x3 = np.random.randint(1, 50) 
#generate a certain number of random ints between a given  range 
x4 = np.random.randint(1,100,15)

#arrange() 
#create an ordered array within a given ranhe 
x5 = np.arrange(1,50)

#eye() 
x6 = np.eye(7) 
#ones() 
x7 = np.ones((7,7))
#zeros()
x8 = np.zeros(8)

##User input: take a positive integer "x" from user  
##and create a 1x10 array with random numbers ranging from 0 to x
x= int(input("Please enter a positive numer, "))
x = np.random.randint(1, x, 10)

##Numpy mathematical ops 
x9 = np.arrange(1,10)
x10 = np.arrange(1,10)

sum = x9 + x10 
squared = x9 ** 2 
sqrt = np.sqrt(squared) 
exponentials = np.exp(x10) 

##Array slicing and indexing
numpy_array1 = np.array([3, 5, 6, 2, 8, 10, 20, 50])
#access 1st element of an array, etc  
numpy_array1[0] 
numpy_array1[1]
numpy_array1[-1]

#slicing for first 3 elements 
numpy_array1[0:3] 

#broadcasting altering several values in an array at once
numpy_array1[0:4] = 6

#define a 2 dimension array 
matrix = np.random.randint(1, 10, (4, 4))
#access first row of the matrix
matrix[0] 
#access 2nd row and so on of the matrix
matrix[1]
matrix[-1]
#get one element within a matrix
matrix[0][2] #first row, 3 rd column 

##Element selection with conditions
matrix3 = np.random.randint(1, 10 (5, 5))
new_matrix = matrix3[ matrix3 > 7 ]
#obtain only odd elements
new_matrix1 = matrix3[ matrix3 % 2 == 1 ]

##Pandas Fundamentals 
import pandas as pd

#define a 2 dimensional pandas df 
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
                                'Bank Client Name':['Channel', 'Steve', 'Mitch', 'Ryan'], 
                                'Amount [$]':[35000, 29000, 10000, 20000], 
                                'Years with Bank': [3, 4, 9 ,5]})
#Check type of data type
type(bank_client_df)
#Check first 2 rows in df 
bank_client_df.head(2) 
#Check last 2 rows in df 
bank_client_df.tail(2)

#Create a stocks df
my_stocks_df = pd.DataFrame({'Stock Ticker': ['AAPL', 'GOOG', 'AMZN', 'ATT'], 
                            'Price per share[$]': [3500, 400, 1200, 50], 
                            'Number owned': [100, 600, 2000, 50000], 
                            'Total Value[$]': ['price per share [$]'] * ['Number owned']
                            })

##Pandas with CSV and HTML data##
#scrape with Pandas (make sure to run 'pip3 install lxml')
sample_df = pd.read_html('enter sample link here')

#Read tabular US retirement data 
retirement_df = pd.read_html('https://www.ssa.gov/oact/progdata/nra.html')

##Pandas operations 
#Sample df 
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
                                'Bank Client Name':['Channel', 'Steve', 'Mitch', 'Ryan'], 
                                'Amount [$]':[35000, 29000, 10000, 20000], 
                                'Years with Bank': [3, 4, 9 ,5]})

#pick certain rows that satisfy certain criteria(filtering)
df_loyalCust = bank_client_df[ bank_client_df['Years with Bank'] >=5  ]
df_loyalCust 

#delete a column from the df 
del bank_client_df['Bank Client Id']
bank_client_df

#total of amount in bank accounts 
amount_banked = bank_client_df['Amount [$]'].sum() 

##Pandas dataframe + functions 
#Sample df 
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
                                'Bank Client Name':['Channel', 'Steve', 'Mitch', 'Ryan'], 
                                'Amount [$]':[35000, 29000, 10000, 20000], 
                                'Years with Bank': [3, 4, 9 ,5]})

#define a function that pay an interest rate of 2% to accounts in the bank client df
def amount_paid(balance): 
    return balance * .02 

bank_client_df['Amount [$]'].apply(amount_paid)

#apply a pre-defined function
bank_client_df['Bank Client Name'].apply(len)

##Sorting and ordering in Pandas 
#Sample df 
bank_client_df = pd.DataFrame({'Bank Client ID':[111, 222, 333, 444],
                                'Bank Client Name':['Channel', 'Steve', 'Mitch', 'Ryan'], 
                                'Amount [$]':[35000, 29000, 10000, 20000], 
                                'Years with Bank': [3, 4, 9 ,5]})
#sort rows by a client's years with the bank
bank_client_df.sort_values(by = 'Years with Bank')
#now change value in memory 
bank_client_df.sort_values(by = 'Years with Bank', inplace = True)

##Concatenating and merging with Pandas 
#create sample dfs

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3',]
                    'C': ['C0', 'C1', 'C2', 'C3',]
                    'D': ['D0', 'D1', 'D2', 'D3',]}, 
                index = [0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 
                    'B': ['B4', 'B5', 'B6', 'B7',]
                    'C': ['C4', 'C5', 'C6', 'C7',]
                    'D': ['D4', 'D5', 'D6', 'D7',]}, 
                index = [4, 5, 6, 7])

df3 =  pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 
                    'B': ['B8', 'B9', 'B10', 'B11',]
                    'C': ['C8', 'C9', 'C10', 'C11',]
                    'D': ['D8', 'D9', 'D10', 'D11',]}, 
                index = [8, 9, 10, 11])

#concatenate dfs 
pd.concat([df1, df2, df3])