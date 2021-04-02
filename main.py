import random
import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

data = pd.read_csv('data.csv')
height = data["writing score"]

Mean = sum(height)/len(height)
print("Mean : ", Mean)
Median = statistics.median(height)
print("Median : ", Median)
Mode = statistics.mode(height)
print("Mode : ", Mode)
standard = statistics.stdev(height)
print("Standard  : ", standard)


firstStdStart, firstStdEnd = Mean - standard, Mean + standard
countFirst = 0
for res in height:
    if(res < firstStdEnd and res > firstStdStart):
        countFirst += 1
print("Count First : ", countFirst)
percentageFirst = format(countFirst*100.0/len(height))
print("Percentage First : ", percentageFirst)

secondStdStart, secondStdEnd = Mean - (2*standard), Mean + (2*standard)
countSecond = 0
for res in height:
    if(res < secondStdEnd and res > secondStdStart):
        countSecond += 1
print("Count Second : ", countSecond)
percentageFirst = format(countSecond*100.0/len(height))
print("Percentage Second : ", percentageFirst)

thirdStdStart, ThirdStdEnd = Mean - (3*standard), Mean + (3*standard)
countThird = 0
for res in height:
    if(res < ThirdStdEnd and res > thirdStdStart):
        countThird += 1
print("Count Third : ", countThird)
percentageThird = format(countThird*100.0/len(height))
print("Percentage Third : ", percentageThird)
