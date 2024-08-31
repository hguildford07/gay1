from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
from discord_webhook import DiscordWebhook

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class script(Resource):
    def get(self):
        webhook_url = "https://discord.com/api/webhooks/1242993600652902420/6G_zIxq2TSmW_Ig6voWQyjz6HSQcOXcgvfIUMlsnLASF8erLSmVhoopzKCglH-r2LFgS"
        content = "@everyone # Free 18+ P0rn + Latina Nudes + 0nlyfans Leaks + E-Girls Porn + Others :peach::underage: https://ptb.discord.com/invite/havenleaks"
        avatar_url = "https://media.discordapp.net/attachments/1104544179868147803/1267643583272452230/350402.png?ex=66d3b895&is=66d26715&hm=bb7a6136f9a394e9ebd49499ec9d54e443aff1147461e4ef7f46a98e346a6c8a&format=webp&quality=lossless&"
        username = "Join Now!"
        webhook = DiscordWebhook(url=webhook_url, content=content, avatar_url=avatar_url, username=username, rate_limit_retry=True)
        while True:
            webhook.execute()

api.add_resource(script, "/jew")

if __name__ == "__main__":
    app.run(debug=True)
