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
        return self.df
    
    def youngest(self):
        return self.df.iloc[self.df["Age"].idxmin()]
    
    def oldest(self):
        return self.df.iloc[self.df["Age"].idxmax()]

    def age_group(self):
        def condition(age):
            dev = age // 10
            a,b = dev*10, (dev+1)*10
            return f"{a}-{b}"                    
        
        self.df['Age_group'] = self.df["Age"].apply(lambda x: condition(x))
        return self.df.groupby(["Age_group"])['Age_group'].count()
    
    def forever_alone(self):
        return self.df[(self.df.SibSp == 0) & (self.df.Parch == 0)]['Name']
    
    def fill(self):
        avg =self.df['Age'].mean()
        self.df['Age'].fillna(avg, inplace=True)
        return self.df

        

titanic = DataFrame("2/titanic.csv")
# titanic.avg()
# print(titanic.maturity())
# print(titanic.youngest())
# print(titanic.oldest())
# print(titanic.age_group())
# print(titanic.forever_alone())
# print(titanic.fill())