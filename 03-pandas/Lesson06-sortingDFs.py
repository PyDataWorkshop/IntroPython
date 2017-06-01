data = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'year': [2012, 2012, 2013, 2014, 2014],
        'reports': [1, 2, 1, 2, 3],
        'coverage': [2, 2, 3, 3, 3]}
df = pd.DataFrame(data, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
df



df.sort_values(by='reports', ascending=0)


df.sort_values(by=['coverage', 'reports'])
