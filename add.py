import sqlite3,sys,encry

d = sqlite3.connect('hola')
c = d.cursor()
def add(site,user,pas):

    s = site
    u = user
    p = encry.en(pas)
    c.execute('''CREATE TABLE IF NOT EXISTS info(site TEXT(10) ,uname TEXT(40) NOT NULL,pass TEXT(40))''')
    if c.execute('''INSERT INTO info (site,uname,pass) VALUES (?,?,?)''', (s, u, p)):
        print 'Inserted'
    else:
        print 'Not Inserted'
    d.commit()


def update(site,user,pas):
    s = site
    u = user
    p = encry.en(pas)
    c.execute('''CREATE TABLE IF NOT EXISTS info(site TEXT(10) ,uname TEXT(40) NOT NULL,pass TEXT(40))''')
    if c.execute('''update info SET pass=? where site=? and uname=?''', (p, s, u)):
        print 'Updated'
    else:
        print 'Wrong Details'
    d.commit()


def delete(site,user,pas):
    s = site
    u = user
    p = encry.en(pas)
    c.execute('''CREATE TABLE IF NOT EXISTS info(site TEXT(10) ,uname TEXT(40) NOT NULL,pass TEXT(40))''')
    if c.execute('''delete  from info where site=? and uname=? and pass=?''', (s, u, p)):
        print 'Deleted'
    else:
        print 'Wrong Details'
    d.commit()