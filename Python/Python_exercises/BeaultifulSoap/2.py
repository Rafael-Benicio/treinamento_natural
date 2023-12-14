# Write a Python program to retrieve all the paragraph tags from a given html document.

from bs4 import BeautifulSoup

HTML_IN_PLAIN_TEXT = """
<html>
     <head>
          <meta http-equiv="Content-Type" content="text/html;
          charset=iso-8859-1">
          <title>An example of HTML page</title>
     </head>
     <body>
          <h2>This is an example HTML page</h2>
          <p>Much time ago, here had a big text, but...
          </p>
          <p><a href="https://zelda.php">Do you want a sword</a></p>
          <p><a href="https://link.php">Do you want a shield</a></p>
     </body>
</html>
"""

if __name__=='__main__':
     soup_html=BeautifulSoup(HTML_IN_PLAIN_TEXT, "html.parser")
     tag_p_finded=soup_html.find_all('p')
     [print(tag_p) for tag_p in tag_p_finded]