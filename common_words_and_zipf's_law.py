from math import log
from altair import Data, Chart

# used csv of 5000 most common English words with part of speech, frequency, and dispersion
file = open('words5000.csv', 'r')
lines = file.readlines()
rank = []
word = []
pos = []
freq = []
disp = []
for line in lines[1:]:
    line = line.split(',')
    rank.append(int(line[0]))
    word.append(line[1])
    pos.append(line[2])
    freq.append(int(line[3]))
    disp.append(float(line[4]))
print(rank[0])

# usage percentage for top 10
file = open('words5000.csv', 'r')
lines = file.readlines()
rank = []
word = []
pos = []
freq = []
disp = []
for line in lines[1:]:
    line = line.split(',')
    rank.append(int(line[0]))
    word.append(line[1])
    pos.append(line[2])
    freq.append(int(line[3]))
    disp.append(float(line[4]))
##

freq_perc = []
freq_sum = 0
for num in freq:
    freq_sum += num
print(freq_sum)  # 329794508
for num in freq:
    freq_perc.append(num / freq_sum)
print(freq_perc[0])
top_10 = 0
bottom_10 = 0
for perc in freq_perc[:10]:
    top_10 += perc
for perc in freq_perc[4990:]:
    bottom_10 += perc

# add log of freq and rank
file = open('words5000.csv', 'r')
lines = file.readlines()
rank = []
word = []
pos = []
freq = []
disp = []
for line in lines[1:]:
    line = line.split(',')
    rank.append(int(line[0]))
    word.append(line[1])
    pos.append(line[2])
    freq.append(int(line[3]))
    disp.append(float(line[4]))
##

freq_perc = []
freq_sum = 0
for num in freq:
    freq_sum += num
# print(freq_sum) # 329794508
for num in freq:
    freq_perc.append(num / freq_sum)
# print(freq_perc[0])
top_10 = 0
bottom_10 = 0
for perc in freq_perc[:10]:
    top_10 += perc
for perc in freq_perc[4990:]:
    bottom_10 += perc
##

log_freq = []
log_rank = []
for num in freq:
    log_freq.append(log(num, 10))
for num in rank:
    log_rank.append(log(num, 10))


x_vals = rank
y_vals = freq

data = Data(rank=x_vals, freq=y_vals)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='rank', y='freq')
enc.display()

x_vals = log_rank
y_vals = log_freq

data = Data(log_rank=x_vals, log_freq=y_vals)
chart = Chart(data)
mark = chart.mark_point()
enc = mark.encode(x='log_rank', y='log_freq')
enc.display()

# which words are on list forwards and backwards
file = open('words5000.csv', 'r')
lines = file.readlines()
rank = []
word = []
pos = []
freq = []
disp = []
for line in lines[1:]:
    line = line.split(',')
    rank.append(int(line[0]))
    word.append(line[1])
    pos.append(line[2])
    freq.append(int(line[3]))
    disp.append(float(line[4]))

reverse = []
for wrd in word:
    reverse.append(wrd[::-1])
count = 0
for wrd in reverse:
    if wrd in word:
        print(wrd)
        count += 1
print(count)

# reversed with 's' on end
file = open('words5000.csv', 'r')
lines = file.readlines()
rank = []
word = []
pos = []
freq = []
disp = []
for line in lines[1:]:
    line = line.split(',')
    rank.append(int(line[0]))
    word.append(line[1])
    pos.append(line[2])
    freq.append(int(line[3]))
    disp.append(float(line[4]))

reverse_plus_s = []
for wrd in word:
    wrd2 = wrd + "s"
    reverse_plus_s.append(wrd2[::-1])
count = 0
for wrd in reverse_plus_s:
    if wrd in word:
        print(wrd)
        count += 1
print(count)

# distribution of parts of speech
file = open('words5000.csv', 'r')
lines = file.readlines()
rank = []
word = []
pos = []
freq = []
disp = []
for line in lines[1:]:
    line = line.split(',')
    rank.append(int(line[0]))
    word.append(line[1])
    pos.append(line[2])
    freq.append(int(line[3]))
    disp.append(float(line[4]))

POS = ['a', 'v', 'c', 'i', 't', 'p', 'd', 'x', 'r', 'm', 'n', 'e', 'j', 'u']
COUNT = []
for x in POS:
    cnt = pos.count(x)
    COUNT.append(cnt)

x_vals = POS
y_vals = COUNT

data = Data(POS=x_vals, COUNT=y_vals)
chart = Chart(data)
mark = chart.mark_bar()
enc = mark.encode(x='POS:N', y='COUNT:Q')
enc.display()
