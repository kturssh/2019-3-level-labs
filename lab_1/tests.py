import unittest
import secondtry
import json

url = 'http://ru-good.ru/category/science'


class MyTestCase(unittest.TestCase):

    def test_html_return(self):

        secondtry.get_html_page(url)

        with open('articles.json', encoding='utf-8') as f_obj:
            f = f_obj.readlines()

        self.assertNotEqual(len(f), 0)

    def test_json_file(self):

        with open('articles.json', encoding='utf-8') as f_obj:
            js_file = json.load(f_obj)

        self.assertTrue('url' in js_file.keys())
        self.assertTrue('articles' in js_file.keys())
        self.assertTrue('title' in js_file['articles'][0].keys())

    def test_check_titles(self):

        secondtry.get_html_page(url)

        with open('articles.json', encoding='utf-8') as f_obj:
            js_file = json.load(f_obj)

        number_of_articles = 7

        self.assertEqual(len(js_file['articles']), number_of_articles)

if __name__ == '__main__':
    unittest.main()

