import requests
import settings
import misc

from flask import Flask

testData = "hello this is preview.jpg and welcome to jackass"

def test():
    return misc.findFileNameByExt(testData,'jpg') + ' <-: file name found in :-> ' + testData

def print_info(m_app):
    output = misc.runProc('ls')

    #print(output)

    #print("Debug ->", m_app.debug) ip addr show
    #print("Testing ->", m_app.testing)

def init_run(m_app):
    settings.load_settings()

    settings.update_setting('port',8080)

    m_app.add_url_rule('/','index',requests.index)
    m_app.add_url_rule('/t','test',test)
    m_app.add_url_rule('/get_picture','get_picture',requests.get_picture)
    m_app.add_url_rule('/get_preview','get_preview',requests.get_preview)
    m_app.add_url_rule('/take_picture','take_picture',requests.take_picture)

    print_info(m_app)
    m_app.run(host = "0.0.0.0",port = settings.g_port)

init_run(Flask(__name__))
