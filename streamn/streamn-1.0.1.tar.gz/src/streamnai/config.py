import os
import json

CREATE_AWS_TRANSCRIPT_URL = 'https://api.streamn.ai/main/create_new_transcribe_job'
GET_AWS_TRANSCRIPT_URL = 'https://api.streamn.ai/main/get_job_transcript'
START_AUDIO_LAB_URL = 'https://api.streamn.ai/main/audiolab_job'
GET_AUDIO_LAB_TRANSCRIPT = "https://api.streamn.ai/main/get_audiolab_transcript"
GET_IMPROVED_TRANSCRIPT_URL = 'https://api.streamn.ai/main/improved_transcript' 

config_data = {}
streamn_config_file = os.path.join( os.getcwd() , "streamn_config.json" )

if os.path.isfile( streamn_config_file ):
    with open( streamn_config_file , 'r' ) as cfp:
        config_data = json.load(cfp)

else:
    print(f"config file {streamn_config_file} not found")
    print(f"please create config file at {streamn_config_file} and add api key")
    os._exit(1)

API_KEY = config_data.get('api_key','')