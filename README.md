# Bitlinks - Devman
Operations with bitlinks.

This script is written as part of the task of the courses [Devman](https://dvmn.org).

- When entering a betlink into the program, the sum of clicks on it and the sum.

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

### Getting a one bitlink

Enter link: [`https://dvmn.org`](https://dvmn.org)

```python
>>> $ python bitlinks.py -n https://dvmn.org
 Вы ввели длинную ссылку!
 Bitlink:  https://bit.ly/2P4hRWf

```
### Getting the total clicks

Enter bitlink: [`https://bit.ly/2P4hRWf`](https://bit.ly/2P4hRWf)

```python
>>> $ python bitlinks.py -n https://bit.ly/2P4hRWf
  
  Вы ввели Bitlink!
  Сумма кликов Bitlink: 7
  
```
### Getting multiple bitlinks

Enter links: [`https://dvmn.org`](https://dvmn.org), [`https://www.google.ru`](https://www.google.ru), [`https://twitter.com`](https://twitter.com)

```python
>>> $ python bitlinks.py -n https://dvmn.org https://www.google.ru https://twitter.com

 Вы ввели длинную ссылку!
 Bitlink:  https://bit.ly/2P4hRWf
 
 Вы ввели длинную ссылку!
 Bitlink:  https://bit.ly/3BIc8M9

 Вы ввели длинную ссылку!
 Bitlink:  https://bit.ly/2ZIU8UN

```
### Getting the total clicks

Enter bitlink: [`https://bit.ly/2P4hRWf`](https://bit.ly/2P4hRWf) [`https://bit.ly/3BIc8M9`](https://bit.ly/3BIc8M9) [`https://bit.ly/2ZIU8UN`](https://bit.ly/2ZIU8UN)

```python
>>> $ python bitlinks.py -n https://bit.ly/2P4hRWf https://bit.ly/3BIc8M9 https://bit.ly/2ZIU8UN
  
  Вы ввели Bitlink!
  Сумма кликов Bitlink: 7 

  Вы ввели Bitlink!
  Сумма кликов Bitlink: 4 

  Вы ввели Bitlink!
  Сумма кликов Bitlink: 11
```
## Authors

**vlaskinmac**  - [GitHub-vlaskinmac](https://github.com/vlaskinmac/)


