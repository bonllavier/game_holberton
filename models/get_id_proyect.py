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
from datetime import date

day = date.today()
today = day.strftime("%B %d, %Y")
month = str(today)[0:3]
day = int(day.strftime("%d"))


def get_id_project(email, password):
    """ get a projet id from a given user
    the function select the last finished proyect based in the currend date
    through scrapping in the intranet with the module BeautifulSoup """

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
    soup = BeautifulSoup(page, 'html.parser')
    data = {}
    for n in range(len(soup.find_all('li', {'class': 'list-group-item'}))):
        d = soup.find_all('li', {'class': 'list-group-item'})[n]
        child_date = d.findChildren('em', recursive=False)
        child_cd = d.findChildren('code', recursive=False)
        for i in range(len(child_date)):
            data[child_date[i].string] = child_cd[i].string
    val = {}
    for key, value in data.items():
        var = key.split(" ")
        if var[0][1:] == month:
            val[key] = int(var[1])
    if not val:
        print("not project available")
        return None

    get = max(val, key=val.get)
    return (data[get])
