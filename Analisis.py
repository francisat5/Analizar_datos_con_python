import pandas as pd
File = pd.ExcelFile(r"C:\Users\franc\Desktop\Workspace\Analizar_datos_con_python\Medals.xlsx")
print(File.sheet_names)
df=File.parse("Details")
print(df)

df.describe()
