#!/usr/bin/python3
""" bring the proyects id's from a given user """
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from sys import argv
from lxml import html
import mechanize
from http.cookiejar import CookieJar
from get_token import get_token

def get_id_proyect(email, password, token):

    USERNAME = email
    login_url = "https://intranet.hbtn.io/auth/sign_in"
    password = password
    br = mechanize.Browser()
    cj = CookieJar()
    br.set_cookiejar(cj)
    br.open(login_url)
    br.select_form(nr=0)
    br.form['user[login]'] = USERNAME
    br.form['user[password]'] = password
    br.submit()
    page = br.open("https://intranet.hbtn.io/dashboards/my_current_projects")
    list_soup = []
    print("done")
    soup = BeautifulSoup(page, 'html.parser')
    soup.prettify(formatter=lambda s: s.replace(u'\xa0', ''))
    for i in range(len(soup.findAll('code')) - 1):
        spoon = soup.findAll('code')[i]
        spoon = spoon.string
        list_soup.append(spoon)
    print(list_soup)
    print(i)
    return(list_soup)
