# import module
import codecs
import webbrowser
import os

# to open/create a new html file in the write mode
f = open('Results-Page-TweetSA.html', 'w')

#directory of python script as variable      
#get path to parent directory of this file
rel_path = os.path.dirname(os.path.realpath(__file__))
#construct the full path to store collected tweet data
filename = "sentiment_comparisongraph.png"
mypath = os.path.join(rel_path, filename)

# the html code which will go in the file Results-Page-TweetSA.html
html_template = f"""

<html lang="en-US:>

<head>
<title>Tweet Sentiment Analysis Student Research</title>
<basefont size=4>
</head>

<body bgcolor=FFFFFF>

<h1 align=center>Twitter Sentiment Analysis With NLTK's Vader</h1>
<h2 align=center>(ACO 499) 2022 Summer Session B</h6>

<h2 align=center>Mitchell Hoikka</h6>

<p align=center>Display and analyse twitter sentiment data for given keywords</p>

<p align=center>Execute Python code and prompt user input</p>



<link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
<script defer src="https://pyscript.net/alpha/pyscript.js"></script>

<img src={mypath} alt="Graph comparing baseline sentiment to keyword sentiment scores">
<hr>

<h2>How about a nice ordered list!</h2>
<ol>
  <li>This little piggy went to market
  <li>This little piggy went to SB228 class
  <li>This little piggy went to an expensive restaurant in Downtown Palo Alto
  <li>This little piggy ate too much at Indian Buffet.
  <li>This little piggy got lost
</ol>

<h2>Unordered list</h2>
<ul>
  <li>First element
  <li>Second element
  <li>Third element
</ul>

<hr>

<h2>Nested Lists!</h2>
<ul>
  <li>Things to to today:
    <ol>
      <li>Walk the dog
      <li>Feed the cat
      <li>Mow the lawn
    </ol>
  <li>Things to do tomorrow:
    <ol>
      <li>Lunch with mom
      <li>Feed the hamster
      <li>Clean kitchen
    </ol>
</ul>

<p>And finally, how about some <a href=http://www.yahoo.com/>Links?</a></p>

<p>Or let's just link to <a href=../../index.html>another page on this server</a></p>

<p>Remember, you can view the HTMl code from this or any other page by using the "View Page Source" command of your browser.</p>

</body>

</html>

"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()

# viewing html files
# below code creates a
# codecs.StreamReaderWriter object
file = codecs.open("Results-Page-TweetSA.html", 'r', "utf-8")

# using .read method to view the html
# code from our object
print(file.read())

# open html file
webbrowser.open('Results-Page-TweetSA.html')
