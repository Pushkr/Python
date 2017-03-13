from nltk.corpus import stopwords
from collections import Counter
import re


class Solution:
    def __init__(self):
        pass

    def book(self):
        with open("alice.txt", encoding="utf-8") as file:
            lines = file.readlines()
        self.common("".join(lines))

    def blog(self):
        import requests
        from bs4 import BeautifulSoup

        try:
            page = requests.get("http://codelingo.wordpress.com/2017/02/22/stopwords/")
            soup = BeautifulSoup(page.text, "html.parser")
            data = soup.find_all("p", {"style": "text-align:justify;"})
            text_data = ""
            for record in data:
                text_data += record.text

            self.common(text_data)
        except ConnectionError:
            print("Unable to connect to site, Good Bye.")

    @staticmethod
    def common(blob):
        tokenized_words = re.findall("[a-zA-Z\'{1}]+", blob)

        filtered_words = [word for word in tokenized_words
                          if word not in stopwords.words('english')]

        cnt_words = Counter(filtered_words)

        for word in cnt_words.most_common(50):
            print(word)


if __name__ == "__main__":
    Solution().blog()
