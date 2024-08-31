from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
from discord_webhook import DiscordWebhook

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class script(Resource):
    def get(self):
        webhook_url = "https://discord.com/api/webhooks/1242674818604728350/d7cMtIS88pKnr_SztW3O64IGuelIAm0NRyAk8r1Ir4u-di_zfP-Qsw9DYt9OuSrcOmSG"
        content = "🔞 Best Free Onlyfans leaks, Teen content, porn, sexcam and daily leaks here: discord.gg/teen-sex ❤️ @here @everyone 💖WITH NEW CONTENT 💖 JOIN NOW❤️"
        avatar_url = "https://cdn.discordapp.com/attachments/1104544179868147803/1267643582190321798/mGwjDbPL.png?ex=66d46155&is=66d30fd5&hm=683ba7aa5d625f3f9799441bfd58aa5035dcd43438f453259838d5684c26e06e&"
        username = "Leaks!"
        webhook = DiscordWebhook(url=webhook_url, content=content, avatar_url=avatar_url, username=username, rate_limit_retry=True)
        while True:
            webhook.execute()

api.add_resource(script, "/jew")

if __name__ == "__main__":
    app.run(debug=True)
