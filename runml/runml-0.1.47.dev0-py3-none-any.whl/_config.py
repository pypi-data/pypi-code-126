import os


TELEMETRY_ADDRESS = "https://telemetry-321112.ew.r.appspot.com/post_data"
TELEMETRY_ENABLED = not os.getenv("runml_DISABLE_TELEMETRY", "0") == "1"
