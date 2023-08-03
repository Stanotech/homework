from PdDataFrame import PdDataFrame
from PlDataFrame import PlDataFrame

            
titanic = PdDataFrame("2/titanic.csv")
# titanic = PlDataFrame("2/titanic.csv")
titanic.avg()
# print(titanic.maturity())
# print(titanic.youngest())
# print(titanic.oldest())
# print(titanic.age_group())
# print(titanic.forever_alone())
# print(titanic.fill())