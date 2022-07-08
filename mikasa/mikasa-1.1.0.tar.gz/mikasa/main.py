DEV = False
import typer
import os


if not DEV:
    from .db import delete, draw,fetch,drop,update_data,insert_data,change_db
else:
    from db import delete, draw,fetch,drop,update_data,insert_data,change_db



# draw the database 
draw()

print("-"*20,"\n")

app = typer.Typer()


@app.command()
def config(db):
    change_db(db)

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