# Visual Studio Marketplace Scrapper.
Get the details of an extension from `marketplace.visualstudio.com`.  
Details are:
1. Extension title: `title: STRING`
2. Extension publisher name: `publisher_name: STRING`
3. Extension main image/logo: `default_image: URL`
4. Number of installs: `installs: INTEGER`    

All you need is the extension ID eg: `muremwa.read-urls`  
The extension ID is called the __'Unique Identifier'__.

## Usage
### In python code.  
Import the main function.
```python
from src.main import main

details = main('muremwa.read-urls')

```
The main function returns a dict with the details as described above.

![Looks like this in python](img/py_look.jpg)


### In command line
 Use the `read_ext.py` file and add one argument extension ID.
 
 ```commandline
python read_ext.py muremwa.read-urls
```

![Looks like this in commandline](img/cmd_look.jpg)