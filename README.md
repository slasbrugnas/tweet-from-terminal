# TWEET FROM TERMINAL

## Requirements
Using python 3+ with tweepy & dotenv

https://www.python.org/downloads/

`pip install tweepy python-dotenv`

## How To
Get a Twitter for Developer account from https://developer.twitter.com/

Authorize your app for your Twitter account

Then put your consumer key, consumer secret, access token and token secret in a `.env` file this way:

```js
CONSUMER_KEY="XXXX"
CONSUMER_SECRET="XXXX"
ACCESS_TOKEN="XXXX"
TOKEN_SECRET="XXXX"
```

Then run the command `python main.py` from a terminal in the project's folder, enter your message, press ENTER and your message should be posted.
