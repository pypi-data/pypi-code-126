import os
def rename(dir,org,new,orgext,newext):
    for i in os.listdir(dir):
        files = os.path.join(dir,i)
        split= os.path.splitext(files)
        if split[1]==orgext:
            with open(files,"r",encoding="UTF-8") as input:
                s=input.read()
                input.close()
            s=s.replace(org,new)
            with open(files,"w",encoding="UTF-8") as output:
                output.write(s)
                output.close()
            os.rename(files,split[0]+newext)