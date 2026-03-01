import pandas as pd
from IPython.display import display

df = pd.read_csv("https://raw.github.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv", sep=",", encoding="utf-8")

print(f"a) {len(df.columns)} antall kolonner og {len(df.index)} antall rader")
print(f"b) Kolonner: {', '.join(df.columns)}")
display("c)", df.head(3))
display("Alternativt:", df.iloc[:3])
display("d) ", df[["total_bill", "tip"]])

display("e)", df.iloc[99])
display("f)", df[["sex", "size"]].iloc[[9,10]])
display("g)", df[df["total_bill"]<8])

# # 3.1.2 a) 
# print(df.sort_values("total_bill", ascending=False).iloc[:3])

# # b) 
# if sum(df["sex"]=="Male")>len(df.index)/2:
#     print("Det er flest menn")
# else:
#     print("Det er flest kvinner")

# # c)
# print(f"Mest i tips: {df['tip'].max()}$")

# # d) 
# print(f"Størst prosentvise tip: {(df['tip']/df['total_bill']).max()*100:.1f}%")

# # e) 
# df["prosent tip"] = df['tip']/df['total_bill']*100
# grupper = df.groupby("sex").mean()
# print(grupper)
# print(f"Prosentvis mest tips: {grupper.sort_values('prosent tip', ascending=False).index[0]}")

# # f) 
# print(f"Total antall gjester: {df['size'].sum()}")
# print(df.groupby('size').count().sort_values("total_bill", ascending=False).index[0])
