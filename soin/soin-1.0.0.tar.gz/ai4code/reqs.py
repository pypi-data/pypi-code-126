from soin.request import Request


kernels = Request(
    url="https://www.kaggle.com/api/i/kernels.KernelsService/ListKernelIds",
    method="post",
    headers={
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "134",
        "content-type": "application/json",
        "cookie": "ka_sessionid=199a6b9c19841be93758df26ee12c5af; CSRF-TOKEN=CfDJ8EUIQmP2mdlBpjerWetYwI6yqm4SFx7KO0ozMVhCi0EDaHx_lRnz58P1vqm8DXVLfN0LUe4MT-rWoUs-pUaX0IjIyPV4smOAQ-F5WYFUKA; GCLB=CJTKypO7i7-utAE; _ga=GA1.2.1264795371.1657008641; _gid=GA1.2.2141459610.1657008641; ACCEPTED_COOKIES=true; XSRF-TOKEN=CfDJ8EUIQmP2mdlBpjerWetYwI7-P1z-t9FOEZiAnVc7nNg8LBZeLbIOdxnFnmLcg41LCSwlRky5uIIGvc0IDIwogXFlCSORypCCYCpeuJYDpxDznw; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOm51bGwsIm5idCI6IjIwMjItMDctMDVUMDg6MTU6MTAuMDA2NTY3OFoiLCJpYXQiOiIyMDIyLTA3LTA1VDA4OjE1OjEwLjAwNjU2NzhaIiwianRpIjoiZGM1MDY2YmQtZWIzMS00MTQ2LWJjODMtNTA0OGVjZDNlNzAyIiwiZXhwIjoiMjAyMi0wOC0wNVQwODoxNToxMC4wMDY1Njc4WiIsImFub24iOnRydWUsImZmIjpbIktlcm5lbHNTYXZlVG9HaXRIdWIiLCJLZXJuZWxzTHNwQXV0b2NvbXBsZXRlIiwiR2Nsb3VkS2VybmVsSW50ZWciLCJLZXJuZWxFZGl0b3JLaXR0eU1vZGUiLCJLZXJuZWxWaWV3ZXJDbGllbnRMb2FkZWRUYWdzIiwiQ2FpcEV4cG9ydCIsIkNhaXBOdWRnZSIsIktlcm5lbHNGaXJlYmFzZUxvbmdQb2xsaW5nIiwiS2VybmVsc1N0YWNrT3ZlcmZsb3dTZWFyY2giLCJLZXJuZWxFZGl0b3JSZWZhY3RvcmVkU3VibWl0TW9kYWwiLCJLZXJuZWxFZGl0b3JTY3JpcHRUaXBzIiwiS2VybmVsc01hdGVyaWFsTGlzdGluZyIsIktlcm5lbHNFbXB0eVN0YXRlIiwiQ29tbXVuaXR5S21JbWFnZVVwbG9hZGVyIiwiRGF0YXNldHNNYXRlcmlhbERldGFpbCIsIkRhdGFzZXRzTWF0ZXJpYWxMaXN0Q29tcG9uZW50IiwiRGF0YXNldHNTaGFyZWRXaXRoWW91IiwiQ29tcGV0aXRpb25EYXRhc2V0cyIsIlRQVUNvbW1pdFNjaGVkdWxpbmciLCJBbGxvd0ZvcnVtQXR0YWNobWVudHMiLCJLZXJuZWxFZGl0b3JGb3JjZVRoZW1lU3luYyIsIktNTGVhcm5EZXRhaWwiLCJGcm9udGVuZENvbnNvbGVFcnJvclJlcG9ydGluZyIsIkxvd2VyRGF0YXNldEhlYWRlckltYWdlTWluUmVzIiwiRGlzY3Vzc2lvbkVtcHR5U3RhdGUiLCJGaWx0ZXJGb3J1bUltYWdlcyIsIlBob25lVmVyaWZ5Rm9yQ29tbWVudHMiLCJQaG9uZVZlcmlmeUZvck5ld1RvcGljIiwiSW5DbGFzc1RvQ29tbXVuaXR5UGFnZXMiLCJQaW5EYXRhc2V0VmVyc2lvbiIsIkxpaHBOZXdNb2R1bGVzIiwiTGlocE5leHRTdGVwc01ldHJpY3MiLCJDb21wZXRpdGlvbnNMUE11bHRpbGluZUNoaXAiXSwiZmZkIjp7Iktlcm5lbEVkaXRvckF1dG9zYXZlVGhyb3R0bGVNcyI6IjMwMDAwIiwiRnJvbnRlbmRFcnJvclJlcG9ydGluZ1NhbXBsZVJhdGUiOiIwLjAxIiwiRW1lcmdlbmN5QWxlcnRCYW5uZXIiOiJ7IH0iLCJDbGllbnRScGNSYXRlTGltaXQiOiI0MCIsIkZlYXR1cmVkQ29tbXVuaXR5Q29tcGV0aXRpb25zIjoiMzM2MTEsMzM2ODksMzQxODksMzUwMzcsMzU0MjcsMzUyOTEsIDM1Nzk3LCAzNTc2OCwgMzUzMjUsIDM1NDI5LCAzNDkwOSwgMzM1NzksMzcwNjksMzYxNjEiLCJBZGRGZWF0dXJlRmxhZ3NUb1BhZ2VMb2FkVGFnIjoiZGF0YXNldHNNYXRlcmlhbERldGFpbCJ9LCJwaWQiOiJrYWdnbGUtMTYxNjA3Iiwic3ZjIjoid2ViLWZlIiwic2RhayI6IkFJemFTeUE0ZU5xVWRSUnNrSnNDWldWei1xTDY1NVhhNUpFTXJlRSIsImJsZCI6IjM2Y2JhMGExYzk3MmI1NGZlMmIzZGIyYjYxZDhlNmJhOGQ3Mjk1YzAifQ.; _gat_gtag_UA_12629138_1=1; GCLB=COWSi6KS0ennfQ; ka_sessionid=bd21ea11e12a424f3adf9a18eb3981e2",
        "origin": "https://www.kaggle.com",
        "referer": "https://www.kaggle.com/code?page=10",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "x-xsrf-token": "CfDJ8EUIQmP2mdlBpjerWetYwI7-P1z-t9FOEZiAnVc7nNg8LBZeLbIOdxnFnmLcg41LCSwlRky5uIIGvc0IDIwogXFlCSORypCCYCpeuJYDpxDznw",
    },
    preset_body={
        "sortBy": "HOTNESS",
        "pageSize": 100,
        "group": "EVERYONE",
        "tagIds": "",
        "excludeResultsFilesOutputs": False,
        "wantOutputFiles": False,
    },
)


kernel_versions = Request(
    url="https://www.kaggle.com/api/i/kernels.KernelsService/ListKernelVersions",
    method="post",
    headers={
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "134",
        "content-type": "application/json",
        "cookie": "ka_sessionid=199a6b9c19841be93758df26ee12c5af; CSRF-TOKEN=CfDJ8EUIQmP2mdlBpjerWetYwI6yqm4SFx7KO0ozMVhCi0EDaHx_lRnz58P1vqm8DXVLfN0LUe4MT-rWoUs-pUaX0IjIyPV4smOAQ-F5WYFUKA; GCLB=CJTKypO7i7-utAE; _ga=GA1.2.1264795371.1657008641; _gid=GA1.2.2141459610.1657008641; ACCEPTED_COOKIES=true; XSRF-TOKEN=CfDJ8EUIQmP2mdlBpjerWetYwI7-P1z-t9FOEZiAnVc7nNg8LBZeLbIOdxnFnmLcg41LCSwlRky5uIIGvc0IDIwogXFlCSORypCCYCpeuJYDpxDznw; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOm51bGwsIm5idCI6IjIwMjItMDctMDVUMDg6MTU6MTAuMDA2NTY3OFoiLCJpYXQiOiIyMDIyLTA3LTA1VDA4OjE1OjEwLjAwNjU2NzhaIiwianRpIjoiZGM1MDY2YmQtZWIzMS00MTQ2LWJjODMtNTA0OGVjZDNlNzAyIiwiZXhwIjoiMjAyMi0wOC0wNVQwODoxNToxMC4wMDY1Njc4WiIsImFub24iOnRydWUsImZmIjpbIktlcm5lbHNTYXZlVG9HaXRIdWIiLCJLZXJuZWxzTHNwQXV0b2NvbXBsZXRlIiwiR2Nsb3VkS2VybmVsSW50ZWciLCJLZXJuZWxFZGl0b3JLaXR0eU1vZGUiLCJLZXJuZWxWaWV3ZXJDbGllbnRMb2FkZWRUYWdzIiwiQ2FpcEV4cG9ydCIsIkNhaXBOdWRnZSIsIktlcm5lbHNGaXJlYmFzZUxvbmdQb2xsaW5nIiwiS2VybmVsc1N0YWNrT3ZlcmZsb3dTZWFyY2giLCJLZXJuZWxFZGl0b3JSZWZhY3RvcmVkU3VibWl0TW9kYWwiLCJLZXJuZWxFZGl0b3JTY3JpcHRUaXBzIiwiS2VybmVsc01hdGVyaWFsTGlzdGluZyIsIktlcm5lbHNFbXB0eVN0YXRlIiwiQ29tbXVuaXR5S21JbWFnZVVwbG9hZGVyIiwiRGF0YXNldHNNYXRlcmlhbERldGFpbCIsIkRhdGFzZXRzTWF0ZXJpYWxMaXN0Q29tcG9uZW50IiwiRGF0YXNldHNTaGFyZWRXaXRoWW91IiwiQ29tcGV0aXRpb25EYXRhc2V0cyIsIlRQVUNvbW1pdFNjaGVkdWxpbmciLCJBbGxvd0ZvcnVtQXR0YWNobWVudHMiLCJLZXJuZWxFZGl0b3JGb3JjZVRoZW1lU3luYyIsIktNTGVhcm5EZXRhaWwiLCJGcm9udGVuZENvbnNvbGVFcnJvclJlcG9ydGluZyIsIkxvd2VyRGF0YXNldEhlYWRlckltYWdlTWluUmVzIiwiRGlzY3Vzc2lvbkVtcHR5U3RhdGUiLCJGaWx0ZXJGb3J1bUltYWdlcyIsIlBob25lVmVyaWZ5Rm9yQ29tbWVudHMiLCJQaG9uZVZlcmlmeUZvck5ld1RvcGljIiwiSW5DbGFzc1RvQ29tbXVuaXR5UGFnZXMiLCJQaW5EYXRhc2V0VmVyc2lvbiIsIkxpaHBOZXdNb2R1bGVzIiwiTGlocE5leHRTdGVwc01ldHJpY3MiLCJDb21wZXRpdGlvbnNMUE11bHRpbGluZUNoaXAiXSwiZmZkIjp7Iktlcm5lbEVkaXRvckF1dG9zYXZlVGhyb3R0bGVNcyI6IjMwMDAwIiwiRnJvbnRlbmRFcnJvclJlcG9ydGluZ1NhbXBsZVJhdGUiOiIwLjAxIiwiRW1lcmdlbmN5QWxlcnRCYW5uZXIiOiJ7IH0iLCJDbGllbnRScGNSYXRlTGltaXQiOiI0MCIsIkZlYXR1cmVkQ29tbXVuaXR5Q29tcGV0aXRpb25zIjoiMzM2MTEsMzM2ODksMzQxODksMzUwMzcsMzU0MjcsMzUyOTEsIDM1Nzk3LCAzNTc2OCwgMzUzMjUsIDM1NDI5LCAzNDkwOSwgMzM1NzksMzcwNjksMzYxNjEiLCJBZGRGZWF0dXJlRmxhZ3NUb1BhZ2VMb2FkVGFnIjoiZGF0YXNldHNNYXRlcmlhbERldGFpbCJ9LCJwaWQiOiJrYWdnbGUtMTYxNjA3Iiwic3ZjIjoid2ViLWZlIiwic2RhayI6IkFJemFTeUE0ZU5xVWRSUnNrSnNDWldWei1xTDY1NVhhNUpFTXJlRSIsImJsZCI6IjM2Y2JhMGExYzk3MmI1NGZlMmIzZGIyYjYxZDhlNmJhOGQ3Mjk1YzAifQ.; _gat_gtag_UA_12629138_1=1; GCLB=COWSi6KS0ennfQ; ka_sessionid=bd21ea11e12a424f3adf9a18eb3981e2",
        "origin": "https://www.kaggle.com",
        "referer": "https://www.kaggle.com/code?page=10",
        "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "x-xsrf-token": "CfDJ8EUIQmP2mdlBpjerWetYwI7-P1z-t9FOEZiAnVc7nNg8LBZeLbIOdxnFnmLcg41LCSwlRky5uIIGvc0IDIwogXFlCSORypCCYCpeuJYDpxDznw",
    },
    preset_body={
        "sortBy": "HOTNESS",
        "pageSize": 100,
        "group": "EVERYONE",
        "tagIds": "",
        "excludeResultsFilesOutputs": False,
        "wantOutputFiles": False,
    },
)
