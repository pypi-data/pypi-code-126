

import xml.sax
import xml.dom.minidom
import os

L = []
L2 = []
L3 = []
D1 = []
D2 = []
D3 = []
O1=[]

O2=[]

def fileload(file):
    domparse(file)
    XmlRead(file)

def domparse(filepathtxt):
    domtree = xml.dom.minidom.parse(filepathtxt)
    gp = domtree.documentElement

    people = gp.getElementsByTagName('DTS:ConnectionManager')

    for person in people:
        path = person.getAttribute('DTS:ConnectionString')
        O2.append(path)



class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.price = ""
        self.qty = ""
        self.company = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if (tag == "inputColumn"):
            title = attributes["cachedName"]
            L.append(title)
        if (tag == "outputColumn"):
            title = attributes["name"]
            D1.append(title)
        if (tag == "component"):
            title = attributes["name"]
            O1.append(title)

    # Call when a character is read
    def characters(self, content):
        if (self.CurrentData == "price"):
            self.price = content
        elif (self.CurrentData == "qty"):
            self.qty = content
        elif (self.CurrentData == "company"):
            self.company = content




#print("Input Copy Column Name :", L3)
#print("Output Copy Column Name :", D3)
#print("Transformation Name :", O1[t])

def XmlRead(xmlpath):
    # create an XMLReader
    parser = xml.sax.make_parser()

    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = XMLHandler()
    parser.setContentHandler(Handler)
    parser.parse(xmlpath)

#Transformation Name Return Function

def TransformationNamereturner():

    t = len(O1)
    t = t - 3
    return O1[t]

#Input Column Name return function
def InputColumnNamereturner():
    for i in L:
        if i not in L2:
            L2.append(i)
        else:
            L3.append(i)

    return L3

#output Column name return function
def OutputColumnNamereturner():
    for i in range(len(L3)):
        D3.append(D1[i])

    return D3

#input path return fuction

def Inputpathreturner():

    return O2[3]

#output path return fuction
def Outputpathreturner():
    return O2[1]



#input File name return fuction
def InputFile_namereturner():
    filen = O2[3].split("\\")[-1]
    return filen

def InputFile_typereturner():
    filename, file_extension = os.path.splitext(O2[3])
    return file_extension


def OutputFile_namereturner():
    filen = O2[1].split("\\")[-1]
    return filen


def OutputFile_typereturner():
    filename, file_extension = os.path.splitext(O2[1])
    return file_extension




