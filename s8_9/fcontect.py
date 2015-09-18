from bs4 import BeautifulSoup
soup = BeautifulSoup(open('./index.html'))
print soup.title
print soup.div
print soup.a
