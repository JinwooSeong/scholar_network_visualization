from selenium import webdriver
import time,os,json
if __name__ == '__main__':
    executable_path = 'G:\\Study_Study\\CS_4th\\soa\\chromedriver.exe'
    browser = webdriver.Chrome(executable_path=executable_path)
    author_list = []
    existed_author = []
    for filename in os.listdir('./person_html'):
        existed_author.append(filename.replace('.html' ,''))
    with open("person2id.json")as f:
        person2id = json.load(f)
    author_list = list(person2id.keys())
    # print(len(existed_author))
    # print(len(author_list))
    rest_list = list(set(author_list).difference(set(existed_author)))
    # print(len(rest_list))
    for author_name in rest_list:
        f_name = author_name + ".json"
        print(author_name)
        id = person2id[author_name]
        browser.get('https://www.aminer.cn/profile/'+author_name+"/"+id)
        time.sleep(2) 
        
        get_html = "./person_html/"+author_name+".html"
        f = open(get_html,'wb')
        f.write(browser.page_source.encode("utf-8", "ignore")) 
        f.close()
    browser.quit()
