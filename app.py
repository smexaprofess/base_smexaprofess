from twitter import Twitter
import time

#test pancing ke heroku supaya keluar dyno

tw = Twitter()

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) != 0:
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) != 0 and len(message) < 280:
                    if "smexapro!" in message:
                        message = message.replace("smexapro!", "Halo guys!")
                        if len(message) != 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                #delete dm
                            else:
                                print("DM will be posted with media")
                                print(dms[i]['shorted_media_url'])
                                tw.post_tweet_with_media(message, dms[i]['media'],dms[i]['shorted_media_url'], dms[i]['type'])
                                #delete dm
                        else:
                            print("DM deleted because its empty..")
                            #delete dm
                    else:
                        print("DM will be deleted because does not contains keyword..")
                        #delete dm

            dms = list()

        else:
            print("Direct message is empty...")
            dms = tw.read_dm()
            if len(dms) == 0:
                time.sleep(30)

if __name__ == "__main__":
    start()