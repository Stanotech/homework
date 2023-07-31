import pandas as pd
import math

pd.set_option('display.max_rows', None)

class DataFrame:
    def __init__(self, name):
        self.df = pd.read_csv(name)

    def avg(self):
        for Sex in set(self.df['Sex']):
            for Pclass in set(self.df['Pclass']):
                avg =(self.df[(self.df.Pclass == Pclass) & (self.df.Sex == Sex)])['Age'].mean()
                print(f'The average age of {Sex} passangers with {Pclass} class ticket is {avg}')

    def maturity(self):
        def condition(age):
            if age < 18:
                return "Child"
            elif age < 60:
                return "Adult"
            elif math.isnan(age):
                return "Unknown"
            else:
                return "Oldie"
        
        self.df['Maturity'] = self.df["Age"].apply(lambda x: condition(x))
        print(self.df.head(100))


titanic = DataFrame("2/titanic.csv")
titanic.avg()
titanic.maturity()


