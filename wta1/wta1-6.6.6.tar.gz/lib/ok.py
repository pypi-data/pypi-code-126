def ok():
    print("""
    
<html lang = "en">  
<head>  
<title> Calculator </title>  
</head>  
<body>  
<h1> Calculator Program in JavaScript </h1>  
<div class= "formstyle">  
<form name = "f">  
  <input id = "calc" type ="text" name = "a"> <br> 
  <input type = "button" value = "1" onclick = "f.a.value += '1' ">  
  <input type = "button" value = "2" onclick = "f.a.value += '2' ">  
  <input type = "button" value = "3" onclick = "f.a.value += '3' ">  
   <input type = "button" value = "+" onclick = "f.a.value += '+' ">  
  <br>  
  <input type = "button" value = "4" onclick = "f.a.value += '4' ">  
  <input type = "button" value = "5" onclick = "f.a.value += '5' ">  
  <input type = "button" value = "6" onclick = "f.a.value += '6' "> 
  <input type = "button" value = "-" onclick = "f.a.value += '-' ">  
  <br> 
  <input type = "button" value = "7" onclick = "f.a.value += '7' ">  
  <input type = "button" value = "8" onclick = "f.a.value += '8' ">  
  <input type = "button" value = "9" onclick = "f.a.value += '9' ">  
  <input type = "button" value = "*" onclick = "f.a.value += '*' ">  
  <br> 
  <input type = "button" value = "C" onclick = "f.a.value = ' ' " id= "clear" >  
  <input type = "button" value = "0" onclick = "f.a.value += '0' ">  
  <input type = "button" value = "=" onclick = "f.a.value = eval(f.a.value) ">  
  <input type = "button" value = "/" onclick = "f.a.value += '/' ">  
</form>  
</div>  
</body>  
</html> 

    """)