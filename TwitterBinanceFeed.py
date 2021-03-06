import tweepy
import json
import winsound
"""API Keys, make your own at Twitter apps"""

auth = tweepy.OAuthHandler("Consumer Key", "Consumer Secret Key")
auth.set_access_token("Access Token", "Access Token Secret")
api = tweepy.API(auth)

"""User ID's for the twitter accounts of coins listed on Binance"""

coinuserids = ['2425322684','902926941413453824','877807935493033984','826699259441328128','869908314292924416','4897921972','880423818594070528','882330272280322050','915531221551255552','774791455680434176','841424245938769920','816646997356777472','808032684270354433','927804348859428864','3318365565','4135644558','4871918301','2338506822','2925093697','862675563693125632','3305325070','2312333412','862007728956485632','871853588540248064','877078771366453248','3214742482','946758251902881792','776803955301093376','769457743807844352','865963965649571840','4736263474','1393174363','812121371199164416','858954415176396800','2313671966','2592325530','2532881881','878291606830542848','913837178261663744','862609366582571008','900532456821932032','922358568602365953','739770876808167424','918011835554570240','773009781644677120','906057790707216384','902262803557482496','888343534083944448','1051053836','781574541164150785','736586614797783040','2460502890','879923428794355714','888794609509433347','1201353103','929649576151154689','894231710065446912','4792182482','431417121','903434091650883586','887696537400332289','4020178512','842473913997250566','903565929719541760','890522833381715968','760049490187386880','856193547976028161','908863693248593920','503238457','880413992040222722','1031080662','2794894848','884936655437791232','1530530365','922077056309121025','900267964737478656','3291830170','865213817466142724','843372242381783044','20356963','759252279862104064','2965296846','867100084248469505','774689518767181828','718774766136532992','868837446938742786','911172484254150657','767645185962455040','889691121000996864','775658150179508224','725253338640617472','3992601857','9130922','3111739836','719994873491931136','844185333478637568','864347902029709314','2478439963','704476690139885568','912987663052836864','831847934534746114','854430875211124737','907209378331336705','2893134987','818371891937296384','711030662728437760','345738416','734688391942524928','119060937','908576143975919616','4826209539','2432540773','885426541185818625','883984505119297536','707515829798182912','732169766450954240','4633094778','810263154458578944','872984298973941764']

"""Function to split tweets into new lines"""
def insert_newlines(string, every=64):
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

"""Modify the streamlistener"""
class StreamListener(tweepy.StreamListener):
      
    def on_status(self, status):
        """Filter out som noise"""
        if (status.author.id_str in coinuserids) and (not status.in_reply_to_status_id_str):
            winsound.Beep(500,500)
            """Try if tweet is more than 140 chars to display the full tweet"""
            try:    
                text1 = insert_newlines(status.extended_tweet['full_text'])
                print("----------" + "\n" + status.user.name + "\n" + "Status Posted: " + str(status.created_at) + " GMT" + "\n" + text1 + "\n" + "*****" + "\n" + "Link to post: " + "https://twitter.com/statuses/" + status.id_str + "\n" + "*****" + "\n" + "----------")
            except:
                text1 = insert_newlines(status.text)
                print("----------" + "\n" + status.user.name + "\n" + "Status Posted: " + str(status.created_at) + " GMT" + "\n" + text1 + "\n" + "*****" + "\n" + "Link to post: " + "https://twitter.com/statuses/" + status.id_str + "\n" + "*****" + "\n" + "----------")
    def on_error(self, status_code):
        """Close stream if errorcode 420 is returned"""
            if status_code == 420:
                return False
            print(status_code)
"""Call the stream listener"""            
stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(follow=coinuserids)            
