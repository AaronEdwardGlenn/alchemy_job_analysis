# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# %%
df = pd.read_csv('pdxDevJobs.csv')


# %%
df = df.drop(['Unnamed: 0'], axis=1)


# %%
pd.set_option('display.max_columns', 29)


# %%
df.head(20)


# %%
def title_simplifier(title):
    if 'software engineer' in title.lower():
        return 'software engineer'
    elif 'software developer' in title.lower():
        return 'software developer'
    elif 'web developer' in title.lower():
        return 'web developer'
    elif 'UX' in title.lower():
        return 'UX'
    elif 'frontend' in title.lower() or 'front-end' in title.lower():
        return 'frontend'
    elif 'backend' in title.lower() or 'back-end' in title.lower():
        return 'backend'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower() or 'junior' in title.lower() or 'entry' in title.lower():
        return 'jr'
    else:
        return 'na'


# %%
df['simplified_title'] = df['Job Title'].apply(title_simplifier)


# %%
df.simplified_title.value_counts()


# %%
df['seniority'] = df['Job Title'].apply(seniority)


# %%
df.seniority.value_counts()


# %%
df['description_length'] = df['Job Description'].apply(lambda x: len(x))


# %%
df


# %%
df['comp_count'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x != '-1' else 0)


# %%
df.comp_count


# %%
df.columns


# %%
df['company_fullname'] = df.company_fullname.apply(lambda x: x.replace('\r', ''))


# %%
df.company_fullname


# %%
df.describe()


# %%
df.Rating.hist()


# %%
df.average_salary.hist()


# %%
df.columns


# %%
df.description_length.hist()


# %%
df.boxplot(column = ['age', 'average_salary', 'Rating'])


# %%
df[['age', 'average_salary', 'Rating']].corr()


# %%
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(df[['age', 'average_salary', 'Rating']].corr(), cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})


# %%
df.columns


# %%
df_cat = df[['Location', 'Headquarters', 'Size', 'Founded',
       'Type of ownership', 'Industry', 'Sector', 'Revenue', 'company_fullname',
       'in_PDX', 'age', 'javascript_yn', 'react_yn', 'node_yn', 'mongodb_yn',
       'heroku_yn', 'webpack_yn', 'simplified_title',
       'seniority']]


# %%
for i in df_cat.columns: 
    cat_num = df_cat[i].value_counts()
    print("graph for %s: total = %d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


# %%
for i in df_cat[['Headquarters', 'company_fullname']].columns: 
    cat_num = df_cat[i].value_counts()[:25]
    print("graph for %s: total = %d" % (i, len(cat_num)))
    chart = sns.barplot(x=cat_num.index, y=cat_num)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
    plt.show()


# %%
df.columns


# %%
pd.pivot_table(df, index = ['simplified_title', 'seniority'], values = 'average_salary')


# %%
pd.pivot_table(df, index = ['in_PDX', 'simplified_title'], values = 'average_salary')


# %%
df.columns


# %%
df_piv = df[['Rating', 'Size', 'Revenue', 'comp_count', 'javascript_yn', 'react_yn', 'node_yn', 'mongodb_yn',
       'heroku_yn', 'webpack_yn', 'Industry','Type of ownership','average_salary']]


# %%
for i in df_piv.columns: 
    print(i)
    print(pd.pivot_table(df_piv, index=i, values='average_salary').sort_values('average_salary', ascending=False))


# %%
pd.pivot_table(df_piv, index='Industry', columns='react_yn', values = 'average_salary', aggfunc= 'count')


# %%
pip install wordcloud


# %%
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# %%
words = " ".join(df['Job Description'])

def punctuation_stop(text):
    """remove punctuation and stop words"""
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered


words_filtered = punctuation_stop(words)

text = " ".join([ele for ele in words_filtered])

wc= WordCloud(background_color="white", random_state=1,stopwords=STOPWORDS, max_words = 100, width =800, height = 1500)
wc.generate(text)

plt.figure(figsize=[10,10])
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()


# %%
df.to_csv('PDXDevJobsEDA.csv')


# %%



