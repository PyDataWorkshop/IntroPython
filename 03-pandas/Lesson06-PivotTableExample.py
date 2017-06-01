raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 
        'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 
         'Scouts', 'Scouts', 'Scouts', 'Scouts'],
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
        'TestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3]}

df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'TestScore'])
df


##################################################################

pd.pivot_table(df, index=['regiment','company'], aggfunc='mean')


df.pivot_table(index=['regiment','company'], aggfunc='count')


###################################################################
