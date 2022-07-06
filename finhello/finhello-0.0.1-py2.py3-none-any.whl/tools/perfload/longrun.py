import subprocess
import datetime

for i in range(114):
    # to do subprocess call with forwarded stdout
    result = subprocess.run(
        ["ab", "-n", "1000000", "-k", "-c", "50", "http://10.42.110.120/centos"], capture_output=True, text=True
    )

    f = open("/home/centos/longrun_perfload.txt", "a")
    f.write("\n----------------")
    f.write(str(datetime.datetime.now()))
    f.write("------------\n")
    f.write(result.stdout)
    f.close()