from environs import Env

env = Env()
env.read_env()

BOT_TOKEN=env('BOT_TOKEN') 
ADMIN=env('ADMIN')
CHANNEL_ID=env('CHANNEL_ID')

API_ID=env('API_ID')
API_HASH=env('API_HASH')
PHONE_NUMBER=env('PHONE_NUMBER')