import pandas as pd

source_df = pd.read_csv('../data/foneticadivisaosilabica.csv')

separator = " "

result_df = source_df.drop_duplicates()
result_df = result_df.dropna()
# ou
blankIndex=[''] * len(result_df)
#result_df.index=blankIndex

for index, row in result_df.iterrows():
    row['fonetica-divisao_silabica'] = separator.join(row['fonetica-divisao_silabica'])


print(result_df)
#print(separator.join(result_df['fonetica-divisao_silabica']))

result_df.to_csv('../data/userdict-pt_BR.txt', sep='|', index=False, header=None)