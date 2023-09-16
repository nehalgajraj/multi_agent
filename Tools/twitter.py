import tweepy
import json



ClientID = "aWtqcFNtbHBoTcVAySHRZcGo3ZkE6MTpjaQ"
ClientID_sercert = "quhqqqkKHGor_d4plz0IE3ZUtbCfK5zblbrPOH1TLypQRW9kXxe"
beare_token = "AAAAAApAAAAAAAAAAAAAAAJB7ogEAAAAAh1o%2BUVpKiB2%2FnogTP641revchzM%3DFt9a8DfIk2LYaCymCLmMuFaAEQBlkhd6jdd5prBngsC0fXEGvm"
API_KEY = "bL3IYBQsQ1k0snu5EyCwbrxuBQ"
API_SECRET_KEY = "FwDUa9WfrhH3pFbbmRAT4JaTjyYow6PxBYvhG5g8bf4MPzcQyjF"
ACCESS_TOKEN = "1676523k960702320642-xIaasrSuJE32Wdxd6LDqV7gqkAen0C"
ACCESS_TOKEN_SECRET = "iiQfz5KWtpB3UbKoUqtPWrfKCopuJmSa6ZwQhZIwlMD43q"
        
class Twitter:

    def __init__(self,API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET):


        self.api_key = API_KEY
        self.api_key_secret = API_SECRET_KEY
        self.access_token = ACCESS_TOKEN
        self.access_token_secret = ACCESS_TOKEN_SECRET

        auth = tweepy.OAuthHandler(self.api_key, self.api_key_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)

    @classmethod
    def tweet(self ,message: str):
        """Post a tweet to Twitter."""
        self.api.update_status(message)
        return json.dumps({"status": "success", "message": message})

    function_metadata = {
        "name": "tweet",
        "description": "Post a tweet to Twitter",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The content of the tweet",
                },
            },
            "required": ["message"],
        },
    }
