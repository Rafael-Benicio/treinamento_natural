# Write a Python program to extract the text in the first paragraph tag of a given html document

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
          <p>Much time ago, here had a big text, but...</p>
          <p><a href="https://zelda.php">Do you want a sword</a></p>
          <p><a href="https://link.php">Do you want a shield</a></p>
     </body>
</html>
"""

if __name__=='__main__':
     bs_html=BeautifulSoup(HTML_IN_PLAIN_TEXT, "html.parser")

     fst_tag_p_text= bs_html.find('p')

     print(fst_tag_p_text)