# Bitlinks - Devman
Operations with bitlinks.

This script is written as part of the task of the courses [Devman](https://dvmn.org).

- When entering a betlink into the program, the sum of clicks on it and the sum of clicks on individual days will be displayed.

- When entering other links, a bitlink is output.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Python Version

Python 3.6 and later.

### Installing

To install the software, you need to install the dependency packages from the file: **requirements.txt**.

Perform the command:

```

pip3 install -r requirements.txt

```
## Getting API key

- To get the API key. You need to log in to the service link: [`Bitly`](https://bitly.com/).
- In the developer settings menu, select the API and access token.

### Connecting the API key

You need to create a `.env` file and write all sensitive data into it, like this:

```python
BITLY_ACCESS_TOKEN="272a05d39ec46fdac5be4ac7be45f3f"
```

## Examples

### Getting a bitlink

Enter link: [`https://dvmn.org`](https://dvmn.org)

```python
>>> Введите полный адрес ссылки: https://dvmn.org
 Вы ввели длинную ссылку!
 Bitlink:  https://bit.ly/2P4hRWf

```
### Getting the total clicks

Enter bitlink: [`https://bit.ly/2P4hRWf`](https://bit.ly/2P4hRWf)

```python
>>> Введите полный адрес ссылки: https://bit.ly/2P4hRWf
  
  Вы ввели Bitlink!
  Сумма кликов Bitlink: 7 
```

## Authors

**vlaskinmac**  - [GitHub-vlaskinmac](https://github.com/vlaskinmac/)


