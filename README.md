# Twitter Sentiment Analysis

This project demonstrates how to connect to the Twitter API and analyze the sentiment of tweets for two user-given search terms. The program fetches tweets containing the search terms and uses a sentiment analysis model to assign a sentiment score for each term. The script then prints which term has a more positive sentiment score and the sentiment values of the inputs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To run this script, you will need Python 3 and several Python packages. The required packages are listed in the `requirements.txt` file and can be installed using pip:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Installing

To install this script, you just need to clone the repository:

\`\`\`bash
git clone https://github.com/<your_username>/twitter-sentiment-analysis.git
cd twitter-sentiment-analysis
\`\`\`

### Usage

You need to create a `sentiment.input` file where each line represents a search term you want to analyze.

For example, to analyze the sentiment related to the Los Angeles Lakers and Clippers, the file will look like this:

\`\`\`
Lakers
Clippers
\`\`\`

Now you can run the script with the command:

\`\`\`bash
python sentiment.py
\`\`\`

## Structure

The `sentiment.py` script performs the following steps:

1. Authenticates with the Twitter API using your access tokens.
2. Prompts the user to enter two search terms.
3. Fetches recent tweets containing these terms.
4. Extracts the text, usernames, and hashtags from these tweets.
5. Calculates a sentiment score for each term based on the sentiment value of the words in the tweets.
6. Prints which term has a more positive sentiment score, and the sentiment values of each term.

Please note that you should replace the placeholders in the code with your own Twitter API credentials.

## Built With

* Python 3
* Twitter API
* `oauth2`
* `requests-oauthlib`
* `twitter`
* `flake8` for linting

## Author

* **Dean Nunis**
