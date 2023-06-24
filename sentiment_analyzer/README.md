
# Sentiment Analyzer

The `Sentiment_analyzer.py` script performs sentiment analysis on some Twitter data. It calculates the positive score, negative score, and net score for each tweet based on predefined positive and negative word lists.

## Requirements

- Python 3

## Usage

1. Place the `Sentiment_analyzer.py` script in the desired directory.
2. Ensure that the input files (`project_twitter_data.csv`, `positive_words.txt`, and `negative_words.txt`) are located in the same directory as the script.
3. Open a command prompt or terminal and navigate to the directory where the script is located.
4. Run the script using the following command: `python Sentiment_analyzer.py`
5. The script will process the input files and generate an output file named `resulting_data.csv` in the same directory.

## Input Files

- `project_twitter_data.csv`: This CSV file contains the Twitter data to be analyzed. The file should have the following format:
    - The first line should contain the headers: "tweet_text", "retweet_count", "reply_count".
    - Each subsequent line should represent a single tweet, with the tweet text, number of retweets, and number of replies separated by commas.

- `positive_words.txt`: This text file contains a list of positive words used for sentiment analysis. Each word should be on a separate line.

- `negative_words.txt`: This text file contains a list of negative words used for sentiment analysis. Each word should be on a separate line.

## Output

The script generates an output file named `resulting_data.csv`. This CSV file contains the analyzed data for each tweet, including the number of retweets, number of replies, positive score, negative score, and net score.

The output file has the following format:
- The first row contains the headers: "Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score".
- Each subsequent row represents a single tweet and contains the corresponding values for the headers.


## Disclaimer

This script is intended for educational and informational purposes only, it was a final exercise for a python course therefore any inappropriate use of it is considered as plagiarism. 


