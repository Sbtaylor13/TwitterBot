import tweepy
import keys_test
import time

def api():
    auth = tweepy.OAuth1UserHandler(keys_test.api_key, keys_test.api_secret, keys_test.access_token, keys_test.access_token_secret)

    return tweepy.API(auth)

if __name__ == '__main__':

    api = api()
    client = tweepy.Client(consumer_key = keys_test.api_key, consumer_secret = keys_test.api_secret, access_token= keys_test.access_token, access_token_secret = keys_test.access_token_secret)
        
    while True:
        with open('Dune.txt', 'r') as f:
            f_content = f.readline()
            if len(f_content) > 12 and len(f_content) < 280:
                response = client.create_tweet(text=f_content.lstrip() + " #Dune")
        with open('Dune.txt', 'r+') as fp:
            # read an store all lines into list
            lines = fp.readlines()
            # move file pointer to the beginning of a file
            fp.seek(0)
            # truncate the file
            fp.truncate()

            # start writing lines except the first line
            # lines[1:] from line 2 to last line
            fp.writelines(lines[1:])
        time.sleep(900)
        
