from io import BytesIO, StringIO
from random import randrange
from cairosvg import svg2png
from jinja2 import Template, Environment, FileSystemLoader
import json
import os
# a= open('male_back.json')
# b= a.read()
# print(type(json.loads(b)))
path=os.path.dirname(os.path.realpath(__file__))

load_base = FileSystemLoader(path+'./templates',)
# open("./male_back.json", )
env = Environment(loader=load_base)
env.trim_blocks = True
env.lstrip_blocks = True

template = env.get_template('base.svg')
male_back = json.load(open(path+'/male_back.json'))
male_face = json.load(open(path+'/male_face.json'))
male_eyes = json.load(open(path+'/male_eyes.json'))
male_ears = json.load(open(path+'/male_ears.json'))
male_iris = json.load(open(path+'/male_iris.json'))
male_nose = json.load(open(path+'/male_nose.json'))
male_mouth = json.load(open(path+'/male_mouth.json'))
male_brows = json.load(open(path+'/male_brows.json'))
male_mustache = json.load(open(path+'/male_mustache.json'))
male_beard = json.load(open(path+'/male_beard.json'))
male_hair = json.load(open(path+'/male_hair.json'))
male_clothes = json.load(open(path+'/male_clothes.json'))
# print(male_back)

# peyes = male_eyes['eyesback']['shapes'][0][0]['left']
# pback=male_back['backs']['shapes'][0]['single']

# print(template.render(back=peyes))


FACELOLORS = [
    "#f6e4e2",
    "#fbd5c0",
    "#ffd0bc",
    "#f4baa3",
    "#ebaa82",
    "#d79468",
    "#cb8d60",
    "#b2713b",
    "#8c5537",
    "#875732",
    "#73512d",
    "#582812"
]

HAIRCOLORS = [
    "#2a232b",
    "#080806",
    "#3b3128",
    "#4e4341",
    "#504543",
    "#6b4e40",
    "#a68469",
    "#b79675",
    "#decfbc",
    "#ddbc9b",
    "#a46c47",
    "#543c32",
    "#73625b",
    "#b84131",
    "#d6c4c4",
    "#fef6e1",
    "#cac1b2",
    "#b7513b",
    "#caa478",
]

MATERIALCOLOR = [
    "#386e77",
    "#6a3a47",
    "#591956",
    "#864025",
    "#dcc96b",
    "#638e2f",
    "#3f82a4",
    "#335529",
    "#82cbe2",
    "#39557e",
    "#1e78a2",
    "#a44974",
    "#152c5e",
    "#9d69bc",
    "#601090",
    "#d46fbb",
    "#cbe9ee",
    "#4b2824",
    "#653220",
    "#1d282e"
]

FRONTEYESCOLORS = [
    "#000000",
    "#191c29",
    "#0f190c",
    "#09152e",
    "#302040",
    "#1b2a40",
    "#2c1630",
    "#2a150e",
    "#131111",
    "#1b1929",
    "#09112e",
    "#092e0c",
    "#2e0914",
    "#582311",
    "#210d34",
    "#153a4d",
    "#d6f7f4",
    "#5fa2a5",
    "#782c76",
    "#587d90"
]

IRISCOLORS = [
    "#4e60a3",
    "#7085b3",
    "#b0b9d9",
    "#3c8d8e",
    "#3e4442",
    "#66724e",
    "#7b5c33",
    "#ddb332",
    "#8ab42d",
    "#681711",
    "#282978",
    "#9b1d1b",
    "#4d3623",
    "#9fae70",
    "#724f7c",
    "#fdd70e",
    "#00f0f1",
    "#4faaab",
    "#ea02f5",
    "#bd1c1b"
]

BACKCOLOR = [
    "#c4c7f3",
    "#F1D4AF",
    "#774F38",
    "#ECE5CE",
    "#C5E0DC",
    "#594F4F",
    "#547980",
    "#45ADA8",
    "#9DE0AD",
    "#E5FCC2",
    "#00A8C6",
    "#40C0CB",
    "#F9F2E7",
    "#AEE239",
    "#14305c",
    "#5E8C6A",
    "#88A65E",
    "#036564",
    "#CDB380",
    "#ce6130"
]
MOUTHCOLORS = [
    "#DA7C87",
    "#F18F77",
    "#e0a4a0",
    "#9D6D5F",
    "#A06B59",
    "#904539",
    "#e28c7c",
    "#9B565F",
    "#ff5027",
    "#e66638",
    "#fe856a",
    "#E2929B",
    "#a96a47",
    "#335529",
    "#1e78a2",
    "#39557e",
    "#6f147c",
    "#43194b",
    "#98a2a2",
    "#161925"
]


class Canvas:
    def __init__(self, back, face, eyes_back, eyes_front,ears, iris, nose, mouth, brows, mustache, beard, hair, cloth,
    haircolor,backcolor,faceColor, materialcolor, fronteyescolor,iriscolor,mouthcolors, type=0,) -> None:
        self.back = back
        self.face = face
        self.eyes_back = eyes_back
        self.eyes_front = eyes_front
        self.ear = ears
        self.iris = iris
        self.nose = nose
        self.mouth = mouth
        self.brows = brows
        self.mustache = mustache
        self.beard = beard
        self.hair = hair
        self.cloth = cloth
        self.type=type
        
        self.haircolor=haircolor
        self.backcolor= backcolor
        self.facecolor=faceColor
        self.materialcolor=materialcolor
        self.fronteyescolor=fronteyescolor
        self.iriscolor=iriscolor
        self.mouthcolor=mouthcolors


    def canvas(self, obj=None):
        context = self.make()

        return template.render(context)

    def toPng(temp):
        arr = bytes(temp, 'utf-8')

        byte=BytesIO(arr)
        svg2png(arr,write_to="ade.png")

    def make(self):
        type=self.type
        pback = male_back['backs']['shapes'][0]['single']
        peyesback = male_eyes['eyesback']['shapes'][type][self.eyes_back] # not thesame with front
        peyesfront = male_eyes['eyesfront']['shapes'][type][self.eyes_front]
        pears = male_ears['ears']['shapes'][type][self.ear]
        piris = male_iris['eyesiris']['shapes'][type][self.iris]
        pnose = male_nose['nose']['shapes'][type][self.nose]['single']
        pmouth = male_mouth['mouth']['shapes'][type][self.mouth]['single']
        pbrows = male_brows['eyebrows']['shapes'][type][self.brows]
        pmustache = male_mustache['mustache']['shapes'][type][self.mustache]['single']
        pbeard = male_beard['beard']['shapes'][type][self.beard]['single']
        phair = male_hair['hair']['shapes'][type][self.hair]
        pclothes = male_clothes['clothes']['shapes'][type][self.cloth]['single']

        faceshape = male_face['faceshape']['shapes'][type][self.face]['single']
        chinshadow = male_face['chinshadow']['shapes'][type][randrange(3)]['single']
        haircolor=self.haircolor
        backcolor=self.backcolor
        facecolor=self.facecolor
        materialcolor=self.materialcolor
        fronteyescolor=self.fronteyescolor
        iriscolor=self.iriscolor
        mouthcolor=self.mouthcolor
        
        # humanbody=male_face['humanbody']['shapes'][0][0]['single']

        return {
            'back': pback,
            'eyesback': peyesback,
            'eyesfront': peyesfront,
            'ears': pears,
            'iris': piris,
            'nose': pnose,
            'brows': pbrows,
            'mouth': pmouth,
            'mustache': pmustache,
            'beard': pbeard,
            'hair': phair,
            'cloth': pclothes,
            'faceshape': faceshape,
            'chinshadow': chinshadow,
            # 'humanbody':humanbody,
            'haircolor':haircolor,
            'backcolor':backcolor,
            'facecolor':facecolor,
            'materialcolor':materialcolor,
            'fronteyescolor':fronteyescolor,
            'iriscolors':iriscolor,
            'mouthcolor':mouthcolor
        }

def toPng(temp):
    # arr = bytes(temp, 'utf-8')

    # byte=BytesIO(arr)
    return svg2png(temp,  output_height=200,output_width=200)
def toPngfile(temp:str, outfile:str):

    svg2png(temp, write_to=outfile,  output_height=200,output_width=200)

# a = Canvas(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,2,"#582311",
#     "#210d34",
#     "#153a4d",
#     "#d6f7f4",
#     "#5fa2a5",
#     "#782c76",
#     "#587d90").canvas()
# b=toPng(a)
# print(b)
# with open("./sample.svg", 'w') as f:
#     f.write(a)
#     f.close()