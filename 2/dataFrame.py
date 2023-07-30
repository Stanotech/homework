import pandas as pd

class DataFrame:
    def __init__(self, name):
        self.df = pd.read_csv(name)



pp = DataFrame("Owners.csv")
print(pp)