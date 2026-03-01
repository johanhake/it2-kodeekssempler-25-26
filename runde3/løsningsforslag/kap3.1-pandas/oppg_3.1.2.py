import pandas as pd
from IPython.display import display

df = pd.read_csv("https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv", sep=",", encoding="utf-8")

display("a) ", df.sort_values("total_bill", ascending=False).head(3))

if sum(df["sex"]=="Male")>len(df.index)/2:
    print("b) Det er flest menn")
else:
    print("b) Det er flest kvinner")

print(f"c) Mest i tips: {df['tip'].max()}$")

# d) Alternativ med beregnig på Serier(numpy-arrays)
print(f"d) Størst prosentvise tip: {(df['tip']/df['total_bill']).max()*100:.1f}%")

# Alternativt med sortvalues:
df["prosent"] = df['tip']/df['total_bill']*100
print(f"d) Alternativ {df.sort_values('prosent').iloc[-1]['prosent']:.1f}%")

# e) 
grupper = df.groupby("sex").mean(numeric_only=True)
display(grupper)
print(f"e) Prosentvis mest tips: {grupper.sort_values('prosent', ascending=False).index[0]}")

# f) 
print(f"f) Total antall gjester: {df['size'].sum()}")

# g) 
sortert = df.groupby('size').count().sort_values('total_bill', ascending=False)
display(sortert)
print(f"g) Vanligst antall gjester per regning: {sortert.index[0]}")