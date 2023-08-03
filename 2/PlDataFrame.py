import polars as pl

class PlDataFrame:
    def __init__(self, name):
        self.df = pd.read_csv(name)

    def avg(self):
        for Sex in set(self.df['Sex']):
            for Pclass in set(self.df['Pclass']):
                avg = self.df.filter((self.df['Pclass'] == Pclass) & (self.df['Sex'] == Sex))['Age'].mean()
                print(f'The average age of {Sex} passengers with {Pclass} class ticket is {avg}')

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
            
        self.df = self.df.with_columns(self.df["Age"].apply(lambda x: condition(x)).alias("Maturity"))
        return self.df
    
    def youngest(self):
        df_a = self.df.filter(~pl.col("Age").is_nan())
        df_a = df_a.sort("Age")
        return df_a[0]

    def oldest(self):
        df_a = self.df.filter(~pl.col("Age").is_nan())
        df_a = df_a.sort("Age", descending=True)
        return df_a[0]

    def age_group(self):
        def condition(age):
            dev = age // 10
            a, b = dev * 10, (dev + 1) * 10
            return f"{a}-{b}"                    
        
        self.df = self.df.with_columns(pl.col('Age').apply(lambda x: condition(x)).alias('Age_group'))
        return self.df.groupby("Age_group", maintain_order=True).count()

    def forever_alone(self):
        return self.df.filter((self.df["SibSp"] == 0) & (self.df["Parch"] == 0))['Name']

    def fill(self):
        avg = self.df['Age'].mean()
        self.df = self.df.with_columns(self.df['Age'].fill_null(avg))
        return self.df