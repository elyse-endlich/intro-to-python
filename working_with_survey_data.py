# number of respondents per country
fileref = open("so_survey.csv", "r")
countries = {}

lines = fileref.readlines()
for row in lines[1:]:
    vals = row.strip().split('|')
    if vals[1] not in countries:
        countries[vals[1]] = 1
    else:
        countries[vals[1]] += 1
print(countries.items())

# most popular programming languages
fileref = open("so_survey.csv", "r")
languagecount = {}

lines = fileref.readlines()
for row in lines[1:]:
    vals = row.strip().split('|')
    temp = vals[12]
    languages = temp.split(';')
    for lang in languages:
        if lang not in languagecount:
            languagecount[lang] = 1
        else:
            languagecount[lang] += 1
# print(languagecount.items())

sorted_keys = sorted(languagecount, key=languagecount.get, reverse=True)
sorted_keys = sorted_keys[:10]

for k in sorted_keys:
    print(k, languagecount[k])

# average salary by gender
fileref = open("so_survey.csv", "r")
gender = {}
gender['Male'] = []
gender['Female'] = []
gender['Non-binary, genderqueer, or gender non-conforming'] = []

lines = fileref.readlines()
for row in lines[1:]:
    vals = row.strip().split('|')
    gen = vals[6]
    if 'Male' in gen:
        gender['Male'].append(vals[4])
    elif 'Female' in gen:
        gender['Female'].append(vals[4])
    elif 'Non-binary, genderqueer, or gender non-conforming' in gen:
        gender['Non-binary, genderqueer, or gender non-conforming'].append(vals[4])
print(gender.keys())
total = 0
count = 0

gendersal = gender.copy()
for gen in gendersal:
    salaries = gendersal.get(gen)
    for salary in salaries:
        total += float(salary)
        count += 1
    average = total / count
    print(average)
