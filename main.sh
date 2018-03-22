# This file meant to run files manurally without the use of the node python-shell module
source .env_config.sh

python3 tweepy-twitter-scrape.py
python3 sentiment-analysis.py
