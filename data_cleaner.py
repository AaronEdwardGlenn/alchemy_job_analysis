# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 12:33:58 2020

@author: aaron
"""

import pandas as pd

df = pd.read_csv('glassdoor.csv')

filt = df['Salary Estimate'] != '-1'
df = df[filt]

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K', '').replace('$', ''))

df['min_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_Kd.apply(lambda x: int(x.split('-')[1]))
df['average_salary'] = (df.min_salary+df.max_salary)/2

df['company_fullname'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)

df['in_PDX'] = df['Location'].str.contains('Portland')

df['age'] = df.Founded.apply(lambda x: x if x <1 else 2020-x)

df['javascript_yn'] = df['Job Description'].apply(lambda x: True if 'javascript' in x.lower() else False)
df['react_yn'] = df['Job Description'].apply(lambda x: True if 'react' in x.lower() else False)
df['node_yn'] = df['Job Description'].apply(lambda x: True if 'node' in x.lower() else False)
df['mongodb_yn'] = df['Job Description'].apply(lambda x: True if 'mongodb' in x.lower() else False)
df['heroku_yn'] = df['Job Description'].apply(lambda x: True if 'heroku' in x.lower() else False)
df['webpack_yn'] = df['Job Description'].apply(lambda x: True if 'webpack' in x.lower() else False)

df.columns
df_out = df.drop(['Unnamed: 0'], axis=1)

df_out.to_csv('pdxDevJobs.csv')