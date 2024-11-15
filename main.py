from bs4 import BeautifulSoup
import requests
import lmxl
# from flask import Flask

# app = Flask(__name__)
username = "kothawleprem"

github_html = requests.get(f"https://github.com/{username}").text
soup = BeautifulSoup(github_html, "lmxl")

print(soup.a)

# @app.route('/<username>')
# def git(username):
#     github_html = requests.get(f'https://github.com/{username}').text
#     soup = BeautifulSoup(github_html, "html.parser")
#     img_url = soup.a
#     print(img_url)
#     repos = soup.find('span',class_="Counter").text
     
#     result = {
#         'imgUrl' : img_url,
#         'numRepos' : repos,
#     }
#     return result

# if __name__ == "__main__":
#     app.run(debug=True)