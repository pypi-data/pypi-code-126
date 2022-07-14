from streamnai.libraries import *
from streamnai.config import *
import time



class TaskInProgress(Exception):
    """
    Exception raised for jobs in progress
    """

    def __init__( self , job_id ):
        self.message = f"job: {job_id} in progress"
        super().__init__(self.message)
        


def retry(exceptions, total_tries=10, initial_wait=10, backoff_factor=2, logger=None):
    """
    calling the decorated function applying an exponential backoff.
    Args:
        exceptions: Exception(s) that trigger a retry, can be a tuple
        total_tries: Total tries
        initial_wait: Time to first retry
        backoff_factor: Backoff multiplier (e.g. value of 2 will double the delay each retry).
        logger: logger to be used, if none specified print
    """
    def retry_decorator(f):
        @wraps(f)
        def func_with_retries(*args, **kwargs):
            _tries, _delay = total_tries + 1, initial_wait
            while _tries > 1:
                try:
                    print(f'{total_tries + 2 - _tries}. try:', logger)
                    return f(*args, **kwargs)
                except exceptions as e:
                    _tries -= 1
                    print_args = args if args else 'no args'
                    if _tries == 1:
                        msg = str(f'Function: {f.__name__}\n'
                                  f'Failed despite best efforts after {total_tries} tries.\n'
                                  f'args: {print_args}, kwargs: {kwargs}')
                        print(msg, logger)
                        raise
                    msg = str(f'Function: {f.__name__}\n'
                              f'Exception: {e}\n'
                              f'Retrying in {_delay} seconds!, args: {print_args}, kwargs: {kwargs}\n')
                    print(msg, logger)
                    time.sleep(_delay)
                    _delay *= backoff_factor

        return func_with_retries
    return retry_decorator


class hit_api:

    def __init__( self , debug = False ):
        self.debug = debug


    def create_new_transcribe_job( self, job_id , audio_file_path , is_medical , vocabulary_name = '',LanguageModelName=''):
        '''
        This function creates a new transcribe job and returns the job id.
        parameters:
            job_id: the job id to be used for the transcribe job.
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
        returns:
            job_id: the job id of the transcribe job.
        '''

        #audio_file_name = os.path.basename(audio_file_path)
        url = CREATE_AWS_TRANSCRIPT_URL

        headers = {
            'accept': 'application/json',
            'Authorization':API_KEY,
            # requests won't add a boundary if this header is set when you pass files=
            # 'Content-Type': 'multipart/form-data',
            }
        
        params = {
            'jobid': job_id,
            'is_medical':is_medical,
            'SPECIALITY':'PRIMARYCARE',
            'Type':'DICTATION',
            'vocabulary_name':vocabulary_name,
            'LanguageModelName':LanguageModelName,
        }

        files = {
            'upload_file': open( audio_file_path , 'rb' ),
        }

        response = requests.post( url , params = params , headers = headers , files = files )

        if self.debug:
            print(f"create job response: {response.text}\tstatus_code: {response.status_code}")

        #remove extra quotes from the response
        job_id = response.text.replace("\"",'')

        return response.status_code , job_id


    #create_new_transcribe_job( job_id = JOB_ID , audio_file_path = SAMPLE_AUDIO_FILE_PATH , is_medical = True )

    @retry(exceptions = TaskInProgress, total_tries = 5 , initial_wait = 20 , backoff_factor = 2, logger=None)
    def get_aws_transcript( self , job_id , is_medical ):
        '''
        This function gets the aws transcript of the audio file.
        parameters:
            job_id: the job id of the transcribe job.
            is_medical: boolean value indicating if the audio file is medical or not.
        returns:
            aws_transcript: the aws transcript of the audio file.
        '''
        url = GET_AWS_TRANSCRIPT_URL

        if self.debug:
            print(f"job_id passed in get aws transcript: {job_id}")

        params = {
            'jobid': job_id ,
            'is_medical': is_medical ,
            }
        
        headers = {
            'Authorization': API_KEY,
        }

        try:
            response = requests.post( url , params = params , headers = headers , timeout = 100 )
        except requests.exceptions.ReadTimeout:
            # back off and retry
            print(f"request timed out")
            raise TaskInProgress(job_id)
            
        if self.debug:
            print(f"response from get aws transcript: {response.text}\tresponse.status_code: {response.status_code}")

        if response.status_code != 200:
            raise TaskInProgress(job_id)
        
        return response.status_code , json.loads(response.text)


    def start_audio_lab_job( self , job_id ):
        '''
        This function starts the audio lab job and returns the results.
        parameters:
            job_id: the job id of the transcribe job.
        returns:
            results: the results of the transcribe job.
        '''

        url = START_AUDIO_LAB_URL

        data = {
            "job_id": job_id 
            }

        headers = {
            'Authorization':API_KEY,
        }

        response = requests.post( url , data = json.dumps(data) , headers = headers )

        return response.status_code , json.loads(response.text)

    
    @retry(exceptions = TaskInProgress, total_tries = 5 , initial_wait = 20 , backoff_factor = 2, logger=None)
    def get_audio_lab_results(self , job_id ):
        '''
        This function gets the audio lab results and returns the results.
        parameters:
            job_id: the job id of the transcribe job.
        returns:
            results: transcript with audio lab results
        '''
        
        url = GET_AUDIO_LAB_TRANSCRIPT

        headers = {
            'Authorization': API_KEY
            }
        
        params = {
            'job_id': job_id
        }

        try:
            response = requests.post( url , params = params , headers = headers , timeout= 100 )
        except requests.exceptions.ReadTimeout:
            # back off and retry
            print(f"request timed out")
            raise TaskInProgress(job_id)
            
        if self.debug:
            print(f"response from get audiolab transcript: {response.text}\tresponse.status_code: {response.status_code}")

        if response.status_code != 200:
            raise TaskInProgress(job_id)

        if self.debug:
            print(f"response form audio lab job start: response_status: {response.status_code}\t transcipt: {response.text}")

        return response.status_code , json.loads(response.text)


    
    @retry(exceptions = TaskInProgress, total_tries = 5 , initial_wait = 20 , backoff_factor = 2, logger=None)
    def start_and_get_improved_transcript_results( self , job_id , is_medical , media_file_extension = '.mp3' ):
        '''
        This function starts the gets the improved transcript and returns the results.
        parameters:
            job_id: the job id of the transcribe job.
            is_medical: boolean value indicating if the audio file is medical or not.
            media_file_extension: the extension of the media file.
        returns:
            results: improved transcribe of the job.
        
        '''

        url = GET_IMPROVED_TRANSCRIPT_URL

        params = {
            'job_id': job_id ,
            'is_medical': is_medical ,
            'media_file_extension': media_file_extension ,
        }

        headers = {
            'Authorization': API_KEY ,
        }

        try:
            response = requests.post( url , params = params , headers = headers , timeout = 100 )
        except requests.exceptions.ReadTimeout:
            print(f"request timed out")
            #retry
            raise TaskInProgress(job_id)
            
        if self.debug:
            print(f"response from get improved transcript: {response.text}\tresponse.status_code: {response.status_code}")

        if response.status_code != 200:
            raise TaskInProgress(job_id)

        return response.status_code , json.loads(response.text) 
    


    
class process_audio(hit_api):

    def __init__(self, debug = False):
        self.job_id = None
        self.debug = debug

    def transcribe_audio( self , audio_file_path , is_medical , vocabulary_name = '' , LanguageModelName = '' ):
        '''
        starts the transcribe job and gets the transcript.
        parameters:
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
            vocabulary_name: the vocabulary name to be used for the transcribe job.
            LanguageModelName: the language model name to be used for the transcribe job.
        returns:
            transcript: the transcript of the audio file.
        
        '''
        #if audio file is not present return error
        if not os.path.isfile( audio_file_path ):
            print(f"Error: Audio file: {audio_file_path} not found")
            return 404 , 'Error: Audio file not found' 
        
        job_id = audio_file_path.split('/')[-1].split('.')[0] 
        response_status_code , job_id = super().create_new_transcribe_job( job_id = job_id , audio_file_path = audio_file_path , is_medical = is_medical , vocabulary_name = vocabulary_name ,LanguageModelName = LanguageModelName )
        self.job_id = job_id
        if response_status_code != 200:
            return response_status_code , 'Error: Unable to create transcribe job'
        else:
            #get aws transcript
            #wait for 10 seconds
            #time.sleep(10)
            response_status_code , transcript = super().get_aws_transcript( job_id = self.job_id , is_medical = is_medical ) 

            if response_status_code != 200:
                return response_status_code , 'Error: Unable to get aws transcript'
        
        if self.debug:
            print(f"returing from transcribe audio , response_status_code: {response_status_code} , transcript: {transcript}")

        return response_status_code , transcript


    def get_audiolab_transcript( self , audio_file_path , is_medical , vocabulary_name = '' , LanguageModelName = '' ):
        '''
        starts the audio lab job and adds audio lab info
        parameters:
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
            vocabulary_name: the name of the vocabulary to be used.
            LanguageModelName: the name of the language model to be used.
        returns:
            transcript: the transcript with audio lab scores added.
        
        '''
        transcipt = ''
        response_status_code , transcipt = self.transcribe_audio( audio_file_path = audio_file_path , is_medical = is_medical , vocabulary_name = vocabulary_name , LanguageModelName = LanguageModelName )

        if response_status_code!=200:
            return response_status_code , transcipt

        #start the audio lab job
        if self.job_id:
            
            #TO-DO , use the below status , before doing next steps
            audiolab_job_start_status = super().start_audio_lab_job( job_id = self.job_id )

            if self.debug:
                print(f"response form start audio lab job: {audiolab_job_start_status}")

            #wait for 15 seconds
            #time.sleep(15)
            #To-DO add retry funtionality

            #get audio lab results
            response_status , transcipt = super().get_audio_lab_results( job_id = self.job_id ) 

            if self.debug:
                print(f"response form audio lab job start: response_status: {response_status}\t transcipt: {transcipt}")

            if response_status != 200:
                return response_status , 'Error: Unable to get audio lab results'


        return response_status , transcipt

    
    def get_improved_transcript( self , audio_file_path , is_medical , vocabulary_name = '' , LanguageModelName = '' ):
        '''
        starts the audio lab job and does iteration to get improved transcript.
        parameters:
            audio_file_path: the path to the audio file to be transcribed.
            is_medical: boolean value indicating if the audio file is medical or not.
            vocabulary_name: the name of the vocabulary to be used.
            LanguageModelName: the name of the language model to be used.

        returns:
            transcript: the improved transcript of the audio file.
        
        '''
        response_status , transcipt = self.get_audiolab_transcript( audio_file_path = audio_file_path , is_medical = is_medical , vocabulary_name = vocabulary_name , LanguageModelName = LanguageModelName )

        if response_status!=200:
            return response_status , 'Error: Unable to get audio lab transcript'
        
        #start the improved transcript job
        if self.job_id:
            response_status , improved_transcript = super().start_and_get_improved_transcript_results( job_id = self.job_id , is_medical = is_medical )

        if response_status != 200:
            return response_status , 'Error: Unable to get improved transcript'
        
        return response_status , improved_transcript

