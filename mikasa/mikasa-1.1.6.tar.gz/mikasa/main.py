DEV = False
import typer
import os


if not DEV:
    from .db import delete, draw,fetch,drop,update_data,insert_data
    from ..config import reader,write
else:
    from db import delete, draw,fetch,drop,update_data,insert_data
    from config import write,reader






print("-"*20,"\n")

app = typer.Typer()




@app.command()
def config(group,key,value):
    write(group,key,value)

if not reader.get("config","db"):
    print("please set the path of the database [you can add your old database that you've been using with Mikasa tool ] : ")
    typer.run(config)
    # draw the database 
    draw()
else:
    # draw the database 
    draw()


@app.command()
def dropall():
    drop()

@app.command()
def insert(name,path):
    insert_data(name,path)


@app.command()
def update(name,path):
    update_data(name,path)



@app.command()
def get(name):
    fetch(name)

@app.command()
def go(project_name):
    
    if not fetch(project_name):
        
        exit()
    
    os.chdir(fetch(project_name))
    os.system("code .")

@app.command()
def remove(name):
    delete(name)




if __name__ == '__main__':
    app()