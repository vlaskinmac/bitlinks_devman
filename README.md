# Bitlinks - Devman
Operations with bitlinks.

This script is written as part of the task of the courses dvmn.org .

- When entering a betlink into the program, the sum of clicks on it and the sum of clicks on individual days will be displayed.

- When entering other links, a bitlink is output

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Python Version

Python 3.6 and later

### Installing

To install the software, you need to install the dependency packages from the file: **requirements.txt**

Perform the command:

```
python pip install -r requirements.txt
```

## Import

```python
import logging
import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

```

## Connecting the API key

You need to create a `.env` file and write all sensitive data into it, like this:

```python
API_KEY = "272a05d39ec46fdac5be4ac7be45f3f"
```

## Examples

### Getting a bitlink

Enter link: `https://dvmn.org`

```python
>>> Введите полный адрес ссылки: https://dvmn.org
 Битлинк:  https://bit.ly/2P4hRWf

```
### Getting the total amount of clicks and on individual days

Enter bitlink: `https://bit.ly/2P4hRWf`

```python
>>> Введите полный адрес ссылки: https://bit.ly/2P4hRWf
  
  Сумма кликов: 5 

  Кликов по дням:
  Кликов: 1 - 2021-10-23
  Кликов: 1 - 2021-10-22
  Кликов: 2 - 2021-10-21
  Кликов: 1 - 2021-10-20
  Кликов: 0 - 2021-10-19

```
The number of days is specified in the constructor variable of the class `self.units_days=` (In the example, 5 days are set)

```python
class Bitlinks:

    def __init__(self):
        self.token = os.getenv('API_KEY')
        self.url = "https://api-ssl.bitly.com/v4/bitlinks"
        self.units_days = 5

```

## Authors

**vlaskinmac**  - [GitHub-vlaskinmac](https://github.com/vlaskinmac/)


