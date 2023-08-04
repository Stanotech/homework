import polars as pl
import pandas as pd
pd.set_option('display.max_rows', None)

# Pd_df_Owners = pd.read_csv("2 DataFrame/PetShop/Owners.csv")
# Pd_df_Pets = pd.read_csv("2 DataFrame/PetShop/Pets.csv")

# Pd_merged_df = Pd_df_Owners.merge(Pd_df_Pets, on="OwnerID")

# print(Pd_merged_df)


Pl_df_Owners = pl.read_csv("2 DataFrame/PetShop/Owners.csv")
Pl_df_Pets = pl.read_csv("2 DataFrame/PetShop/Pets.csv")

Pl_merged_df = Pl_df_Owners.join(Pl_df_Pets, on="OwnerID")

print(Pl_merged_df)
