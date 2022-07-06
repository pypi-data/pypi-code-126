import subprocess
import datetime

result = subprocess.run(
       ["ab", "-n", "5000", "-k", "-v", "4", "-c", "20", "-p", "data/ab_multipart_data.txt", "-T",
        "multipart/form-data; boundary=12345", "http://10.42.110.174:81/api/scf-import/convert"],
    capture_output=True, text=True
   )

f = open("data/longrun_finreq.txt", "a")
f.write("\n----------------")
f.write(str(datetime.datetime.now()))
f.write("------------\n")
f.write(result.stdout)
f.close()
