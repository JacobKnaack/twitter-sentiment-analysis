# Twitter-Sentiment-Analysis

## Scrapes Twitter for tweets and provides Sentiment Analysis with Googles Cloud's Natural Language Processor

Tweepy: [<img src="https://readthedocs.org/projects/tweepy/badge/?version=v3.5.0" >](http://docs.tweepy.org/en/v3.5.0/)

Google Cloud Platform [python documentation](https://github.com/GoogleCloudPlatform/google-cloud-python)

### 3/22/2018

* Beginning of front end client used to interface with python scripts.  Ignore npm scripts and node code if you just want to run python scripts to obtain tweet sentiment scores in a csv.

### 11/18/2017

* Tweepy script working: Scrapes data from search terms, adds them to a folder called results.
* Sentiment analysis working: takes twitter-raw-scrape json object and runs each individual sentence through google cloud API.
* Produces a csv file, each line has a score followed by a magnitude score.

### Getting Started

**Before you start on the code, make sure you have created a Twitter App and a Google Cloud App**
  * [Twitter Dev Console](https://apps.twitter.com/)
  * [Google Cloud Console](https://console.cloud.google.com)

#### In your terminal:
```
git clone https://github.com/JacobKnaack/twitter-sentiment-analysis.git
```
#### Install dependencies with pip:
```
pip install -r requirements.txt
```
#### Configure the application with your credentials for Twitter and Google cloud
* ##### Configuring Twitter Credentials:
    * Replace or add hashtags and search terms with the items you want to use to search twitter.
    * Create a .env_config.sh file and export your credentials as environment variables:
```
export API_KEY=your-api-key-here,
export API_SECRET=your-api-secret-here
export ACCESS_TOKEN=your-access-token-here
export ACCESS_TOKEN_SECRET=your-access-token-here
```

Once this is set you can scrape twitter for your tweets

* ##### Configuring Google Cloud Natural Language Processor

  * Download the sdk from the [cloud.google.com](https://cloud.google.com/sdk/)
  * extract to your working directory and run:

  On Mac
  ```
  ./path-to-sdk/install.sh
  ```
  On Windows
  ```
  ./path-to-sdk/install.bat
  ```

  * Configure your environment with your Google Cloud application:
  ```
  gcloud init
  ```

  * You should receive a key file which you will export in the .env_config.sh file:
  ```
  export GOOGLE_APPLICATION_CREDENTIALS=./path-to-key-file.json
  ```


#### Run the main shell script:
```
source main.sh
```
