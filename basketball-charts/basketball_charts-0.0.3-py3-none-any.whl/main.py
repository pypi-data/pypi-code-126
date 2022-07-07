from bs4 import BeautifulSoup, Comment
import requests
import re
from matplotlib import pyplot as plt
from matplotlib import image

url = "https://www.basketball-reference.com/players/a/allenra02/shooting/2001"
# url = "https://www.basketball-reference.com/players/j/jordami01/shooting/1998"
# url = "https://www.basketball-reference.com/players/c/curryst01/shooting/2016"

def create_shot_chart(
    name="curryst01",
    year="2016",
    ms=2.5,
):
    url=f"https://www.basketball-reference.com/players/{name[0]}/{name}/shooting/{year}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    soup = soup.find_all('div', id="all_shot-chart")[0]

    comments = soup.find(text=lambda text:isinstance(text, Comment))
    soup = BeautifulSoup(str(comments), 'html.parser')
    shots = soup.find_all(re.compile("div"))
    shots = soup.find_all('div', {'style': re.compile(r"top:(.*)px;left:(.*)px;")})
    x, y = [], []
    results = []

    for shot in shots:
        try:
            top, left = re.findall(r"top:(\d+)px;left:(\d+)px;", str(shot))[0]
            result = "Made" in str(shot)
        except:
            continue
        x.append(int(left))
        y.append(int(top))
        results.append(result)

    xmade, ymade = [], []
    xmiss, ymiss = [], []
    for i, j, r in zip(x, y, results):
        if r:
            xmade.append(i)
            ymade.append(j)
            continue
        xmiss.append(i)
        ymiss.append(j)
    background = image.imread('basketball_charts/images/nbahalfcourt.png')
    plt.imshow(background)
    plt.plot(xmiss,ymiss,'rx', markersize=ms)
    plt.plot(xmade,ymade,'go', markersize=ms)
    plt.savefig('basketball_charts/images/bbref_shotchart.png', dpi=1200)
    return list(zip(xmade,ymade))+list(zip(xmiss,ymiss))

# Use pandas data frame to get all wanted data from shot
# convert to python package
# devlop function that can generate chart for a given player and season
# develop a function that can generate a shot chart for a given team and season
# reproduce differengt chart styles
# support resizeable charts (I need to calculate the shot locations in feet)
# Use differnt court backgrounds
# Create full court shot charts with two different teams or x nuber of players. Use the quarter to determine which side of the court the point should go
# Publish youtube videos with animated shot chart for the entire game. Unclude face of the person with the shot

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    shots = create_shot_chart()
    print(shots)