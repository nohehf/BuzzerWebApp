from configparser import ConfigParser

#Get the configparser object
config_object = ConfigParser()

#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG
# config_object["GAME"] = {
#     "admin": "Chankey Pathak",
#     "loginid": "chankeypathak",
#     "password": "tutswiki"
# }

config_object["SERVER"] = {
    "host": "127.0.0.1",
    "port": "5000",
}

config_object["WEBHOOK"] = {
    "webhook_id": "774676765369040946",
    "webhook_token":"zq-XZ3x2CR5QQnwKH-n-5_TUOCewPASXZiCnBxCXA0G0Y_iN-FylZZK41z5LANQ6bVgn",
}

config_object["DISCORD"] = {
    "VoiceChannel": "Bureau",
    "token":"Nzc0NDE1MjE3NjQ3OTQzNjgy.X6XcXw.UIe9ZesQhp4RGU1yB_xUtTI2oi0",
    "chara":"_",
    "whitelist":'Nano#5738,Nohz#9888',
}

#Write the above sections to config.ini file
with open('config.ini', 'w') as conf:
    config_object.write(conf)