import os
# Bot
BOT_TOKEN = '5506081827:AAGPAXNcMsB1ZD8fp5Sc6GQB90X2y7xNRlM'
TG_API_ID = 13233271
TG_API_HASH = 'e3ce8145aa657c2a4cc5cf0f7183e476'
TG_ADMIN = 'Hiyabo'

# Database
DB_LOCAL = False
DB_HOST = 'sql.freedb.tech'
DB_HOST_USERNAME = 'freedb_josemanuel'
DB_HOST_PASSWORD = '5KFPVk*NJ!D%PXq'
DB_NAME = 'freedb_educaDb'

if DB_LOCAL:
    # Database Local
    DB_HOST = ''
    DB_HOST_USERNAME = 'root'
    DB_HOST_PASSWORD = ''
    DB_NAME = 'clutilprodb'