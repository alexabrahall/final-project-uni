import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level   
import os
async def main():
    api = API()  

    set_log_level("DEBUG")
    #add account to log into, this is all burner data, in a real world scenario you would use .env for sensitive data
  
    await api.pool.login_all()

    

   


    #open the textfile with tweet ids to fetch
    with open ("en.txt", "r") as myfile:
        tweet_ids = myfile.readlines()
        myfile.close()

    for tweet_id in tweet_ids:
        

        # tweet info
        tweet = await api.tweet_details(int(tweet_id))  # Tweet
        
        if tweet is None:
            print("Tweet not found")

            #remove tweetid from textfile
            with open("en.txt", "r") as f:
                lines = f.readlines()
            with open("en.txt", "w") as f:
                for line in lines:

                    if(line.strip("\n") == tweet_id.strip("\n")):
                        continue
                   
                    f.write(line)

            continue
        tweet_text = tweet.rawContent

        tweet_text = tweet_text.replace("\n", " ")

         # open the csv to write to
        csv = open("dataset.csv", "a", encoding="utf-8")
        #write to csv
        csv.write(f'"{tweet_text}"\r')

        csv.close()

        # remove tweetid from textfile
        with open("en.txt", "r") as f:
                lines = f.readlines()
        with open("en.txt", "w") as f:
            for line in lines:

                if(line.strip("\n") == tweet_id.strip("\n")):
                    continue
                
                f.write(line)





        print(f"Tweet {tweet_id} written to csv")
        
        
    


if __name__ == "__main__":
    asyncio.run(main())