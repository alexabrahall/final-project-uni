import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level   
import os
async def main():
    api = API()  

    set_log_level("DEBUG")
    #add account to log into, this is all burner data, in a real world scenario you would use .env for sensitive data
    cookies = 'g_state={"i_l":0}; lang=en; guest_id=v1%3A169860847306382967; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCBR39HyLAToMY3NyZl9p%250AZCIlY2QzMWMwYjFlYzdjNWM1MzlhMzQ3NDMxMWUzNmEwOWM6B2lkIiViYjBh%250ANDBlYzFjODdiM2EyOTdlYzI1ZmY1ODcwMmM0Ng%253D%253D--a0c4d84dd8a682a835777029879e85c923caae44; kdt=rlMXb7XGuCrVUeIdzYuC1B3X6MjrogLvMxEjWhAw; auth_token=ff91d70cbce136ef1c64854181cefa7b6b77d4be; ct0=c420ef3ce4dcaf34728080b04853f769fa4c4a256d458fca99525cfc88ff7c567a93b16087f3cd20c0d38289b666996ea761bfb95eadc670a51e48ad0b23d5e37c1c0fa5d7a4c3643e7e6e673ab21bb3; att=1-M11Un4Lg2WrCXhUgdUUr7MWPJ4E0H2xCNAynBQy1; twid=u%3D1718619449983483904'
    await api.pool.add_account("alexunitwitter@gmail.com", "JA7MYuFL3,Rn^vN", "alexunitwitter@gmail.com", "AlexUniTwitter123@", cookies=cookies)

    cookies = 'guest_id=v1%3A169838999318545129; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCBmp7m%252BLAToMY3NyZl9p%250AZCIlZGFiMDg0MjUwZDFiNzJiY2EwMjAxNDU0OGVmMDY0NzY6B2lkIiUzMmI3%250ANzZjMTZkNzE0Yzc2MzhhYzFjY2NkNGRmMmQwOA%253D%253D--89f6b3c1f7e7e9773d6512e5497c0a7229bb1a71; kdt=VIocDovyVJobZFU2UDNJajxNGfyVW7e7irns6MeG; auth_token=befbaee890e505cd63aee59f223301071d1eff07; ct0=4ff48ecc9e06e33629331ae736629902c80ceecd842b6bae783fcbf07a15c097f0074509c36b63480857166467705ba43c813b86685dc32218ecf9abf1754fe43fb1e2326daab00d587910e645fdbe6c; lang=en; twid=u%3D1460064481; dnt=1; twtr_pixel_opt_in=Y; des_opt_in=Y; att=1-Vfz2UgBIyEUOFyOEesL5Fq8QuXORlezAFOB7rOkL'

    await api.pool.add_account("bongo120901@gmail.com", "JA7MYuFL3,Rn^vN", "alexunitwitter@gmail.com", "AlexUniTwitter123@", cookies=cookies)
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