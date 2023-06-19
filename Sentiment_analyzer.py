# function to strip punctuation from a string
def strip_punctuation(st):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in st:
        if char in punctuation_chars:
            st = st.replace(char, "")
    return st

# function to get positive word count
def get_pos(st):
    count = 0
    for word in strip_punctuation(st.lower()).split():
        if word in positive_words:
            count += 1
    return count

# function to get negative word count
def get_neg(st):
    count = 0
    for word in strip_punctuation(st.lower()).split():
        if word in negative_words:
            count += 1
    return count

# open the input file and read data
with open('project_twitter_data.csv', 'r') as file:
    data = file.read().splitlines()

# extract the headers and tweet data
headers = data[0].split(',')
tweets = [line.split(',') for line in data[1:]]

# load positive and negative word lists
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# create the output data
output_data = []
output_data.append(["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"])
for tweet in tweets:
    num_retweets = int(tweet[1])
    num_replies = int(tweet[2])
    pos_score = get_pos(tweet[0])
    neg_score = get_neg(tweet[0])
    net_score = pos_score - neg_score
    output_data.append([num_retweets, num_replies, pos_score, neg_score, net_score])

# write the output data to a new CSV file
with open('resulting_data.csv', 'w') as file:
    for row in output_data:
        file.write(','.join([str(elem) for elem in row])+'\n')
