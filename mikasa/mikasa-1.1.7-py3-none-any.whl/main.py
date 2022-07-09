DEV = True
import typer
import os


if not DEV:
    from .db import delete, draw,fetch,drop,update_data,insert_data
    from .config import reader,write
else:
    from db import delete, draw,fetch,drop,update_data,insert_data
    from config import write,reader



def handle_path(path:str):
    path = path.replace("/","\\")
    if path.endswith("\\"):
        return path+"mikasa.sqlite3"
    else:
        return path+"\\mikasa.sqlite3"
    



print("-"*20,"\n")

app = typer.Typer()




@app.command()
def config(value):
    write(handle_path(value))


if not reader.has_section("config") or not reader.has_option("config","db"):
    print("please insert your database path \n")
    typer.run(config)
else:
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