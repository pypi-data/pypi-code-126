from exergenics import ExergenicsApi
import zipfile
from tempfile import mkdtemp
import requests
import shutil
import os

onWhen = [
    {
        "stage": "stageName",
        "status": "status"
    }
]

for i in onWhen:
    print(i['stage'])

api = ExergenicsApi(useProductionApi=True,
                    token="eyJraWQiOiJpRlwvb0dLamdOTjdLMlEwMWNFRndXUkFROWFZWWdKZ3BBZlNOdDJyWWFIQT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0YzYwNTY3My1kMGQ3LTQwYWUtOWIzMi0yNzhjN2RmYzA3MDUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfQjRUS21DZ2dGIiwiY29nbml0bzp1c2VybmFtZSI6IjRjNjA1NjczLWQwZDctNDBhZS05YjMyLTI3OGM3ZGZjMDcwNSIsImdpdmVuX25hbWUiOiJKb2huIiwiY3VzdG9tOmNvbXBhbnkiOiJIQVNIVEFHIFRFQ0hOT0xPR1kiLCJvcmlnaW5fanRpIjoiNWJiOTA1MjYtZGZkNi00Y2EwLWI5ODItYzhkYTE1NTY4ODhiIiwiYXVkIjoibzg0bms3MDRvbWUwZzZoNjJxazY5amI5ZiIsImV2ZW50X2lkIjoiMWY3ODcyMjYtNzJkNy00ODFmLTliYzgtZjAxNDgxNjMxN2QxIiwidG9rZW5fdXNlIjoiaWQiLCJjdXN0b206dXNlcl9yb2xlIjoiYnVpbGRpbmciLCJhdXRoX3RpbWUiOjE2NTUxNzY4MDIsImV4cCI6MTY1NTI2MzIwMiwiaWF0IjoxNjU1MTc2ODAyLCJmYW1pbHlfbmFtZSI6IkNocmlzdGlhbiIsImp0aSI6ImJjMGYxMDEyLWQyM2UtNDg5MS04NjQyLWUyZTgzY2FjNTZlYSIsImVtYWlsIjoiam9obi5jaHJpc3RpYW5AaGFzaHRhZ3RlY2hub2xvZ3kuY29tLmF1In0.g5M8IXZCgs1ZsUS3JxAcNsoRH9yhgdnd7GV2Lbfu2wOd0nnxMQedju5udUUd7MOXiTQ0dK7Pxbmu--lWPAgRfqCMOG4KjdrDrwPoAxAgB3vJS1qdlgjTwYr5RFaZfkJMADGlMJayK64zbIfiFwlxISqlZaDNXe7_xBhud6CCaCN8wWsA3VINOEwh29MVCj-iSgcuwM5yOVHLZawMnBFW4paV-b7e_muyeHtFv13kOTT9o2eAXjMiMPdIRF75_Kg4Z7Y5OXkYg--u8HXqjTMn6XTshflQbjiEgh0tkkKLiekm4nY5txG18PSgkzRZMGc5zN6Cuj_XXXtrG9BQn4PgUA")

if not api.authenticate():
    exit("couldnt auth")

buildings = api.getBuildings("JC-TEST")

if api.numResults() > 0:
    while api.moreResults():
        building = api.nextResult()
        print(building)

'''
# load the jobs that are ready for merging (rawdata_ready::completed) into an array for looping.
readyJobs = []
api.getJobsByPlant("JC-TEST-PLANT-1")
if api.numResults() > 0:
    while api.moreResults():
        readyJobs.append(api.nextResult())

print(readyJobs)
exit()
'''

# # set these jobs to now waiting for merged ready to begin.
# for i in range(len(readyJobs)):
#     api.setStage(readyJobs[i]['jobId'], "merged_ready", "waiting")
#
# # now loop through all these to download and extract data files
# for i in range(len(readyJobs)):
#
#     # tell the job scheduler we are "running" this job id
#     api.setJobStageRunning(readyJobs[i]['jobId'])
#
#     # get the URL to the datafile from s3 zip (saved from previous stages)
#     urlToDataFile = readyJobs[i]['jobData']['zipfile']
#
#     # download the zip file
#     r = requests.get(urlToDataFile, allow_redirects=True)
#     downloadTempDirectory = mkdtemp()
#     fileSaveAs = "{}/{}".format(downloadTempDirectory, "data.zip")
#     open(fileSaveAs, 'wb').write(r.content)
#
#     # where to save the zip file locally
#     directory_to_extract_to = mkdtemp()
#
#     # extract locally to temp folder
#     with zipfile.ZipFile(fileSaveAs, 'r') as zip_ref:
#         zip_ref.extractall(directory_to_extract_to)
#
#         # get a list of files in this zip
#         listOfiles = zip_ref.infolist()
#
#         # get the location of the extracted file on local storage
#         for extractedFile in listOfiles:
#             # ignore macosx dodgeyness
#             if not extractedFile.filename.startswith("__MACOSX"):
#                 plantDataFile = "{}/{}".format(directory_to_extract_to, extractedFile.filename)
#
#                 ####################################
#                 #### This is a data file to process (merge)
#                 #### TODO @Yi-Jen
#                 ####################################
#                 plantCode = readyJobs[i]['plantCode']
#                 print(plantDataFile)
#
#         # remove the temp directory and all its files.
#         shutil.rmtree(directory_to_extract_to, ignore_errors=True)
#
#         # remove the zip file and directory
#         shutil.rmtree(downloadTempDirectory, ignore_errors=True)
#
#         # once here, merged_ready is set to "complete" (to be picked up by next stage handler)
#         api.setJobStageComplete(readyJobs[i]['jobId'])
