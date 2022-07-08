import click
# importing the required modules
import os
import speech_recognition as sr

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .js file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."


def validate_file(file_name):
    """
    validate file name and path.
    """
    if not valid_path(file_name):
        print(INVALID_PATH_MSG % (file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG % (file_name))
        quit()
    return


def valid_filetype(file_name):
    # validate file type
    return file_name.endswith(".js")

def valid_path(path):
    # validate file path
    print(path)
    return os.path.exists(path)


@click.group()
def main():
  pass


@main.command(name='addLn')
@click.option('--file_name', type=click.Path(exists=True), prompt="Enter The File Path", help="Provide the file path of the file ")
@click.option("--label", prompt="Enter component label", help="Provide your name")
@click.option("--component", prompt="Enter component type", help="Provide your name")
def addline(file_name,label,component):
    validate_file(file_name)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.8)
        print("Tell Label Audio")
        audio = r.listen(source)

        text =  r.recognize_google(audio)
        print("You Said "+text)
    
    

    with open(file_name) as f:
        line =  f.readlines()

    line.insert(int(3),"<MainComponent type='"+component+"' label='"+text+"' kind = 'secondary' />"+" \n")
    with open(file_name, 'w') as f:
        for l in line:
            f.write(l)


@main.command(name='wel')
def welcome():
    click.echo('Welcome')


if __name__ == '__main__':
    main()