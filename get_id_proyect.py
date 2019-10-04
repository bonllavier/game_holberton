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
from datetime import date

day = date.today()
today = day.strftime("%B %d, %Y")
month = str(today)[0:3]
month = "Mar"
print(month)
day = int(day.strftime("%d"))

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
    data = {}
    for n in range(len(soup.find_all('li', {'class': 'list-group-item'}))):
        d = soup.find_all('li', {'class': 'list-group-item'})[n]
        child_date = d.findChildren('em', recursive=False)
        child_cd = d.findChildren('code', recursive=False)
        for i in range(len(child_date)):
            data[child_date[i].string] = child_cd[i].string
    print(data)
    val = {}
    for key, value in data.items():
        var = key.split(" ")
        if var[0][1:] == month:
            print(True)
            val[key] = int(var[1])

    print(val)
    get = max(val, key=val.get)
    print(get)
    return(data[get])
