import sys,add,pro,encry,sqlite3
d = sqlite3.connect('hola')
c = d.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS info(site TEXT(10) ,uname TEXT(40) NOT NULL,pass TEXT(40))''')


if len(sys.argv)==2:
    if sys.argv[1]=="admin":
        print " Main Menu "
        print "1.Add "
        print "2.Update "
        print "3.Delete "
        print "4.Login "
        n=input( "Enter your choice : ")
        if(n==1):
            s=raw_input("Enter site to add : ")
            u=raw_input("Enter username to add : ")
            p=raw_input("Enter password for username : ")
            add.add(s,u,p)
        if n==2:
            s = raw_input("Enter site to update : ")
            u = raw_input("Enter username to update : ")
            p = raw_input("Enter updated password for username : ")
            add.update(s,u,p)

        if n==3:
            s = raw_input("Enter site to delete : ")
            u = raw_input("Enter username to delete : ")
            p = raw_input("Enter password to delete account : ")
            add.delete(s,u,p)
        if n==4:
            i=1
            l=[]
            if c.execute('''SELECT DISTINCT site FROM info'''):
                c=c.fetchall()
                for record in c:
                    print i,'.',record[0]
                    l.append(record[0])
                    i=i+1
                j=input('Select site no: ')
                f=getattr(pro,l[j-1])
                c = d.cursor()
                l1 = []
                o=l[j-1]
                k=1

                if c.execute('''select uname from info where site=?''',(o,)):
                    c=c.fetchall()
                    for record in c:
                        l1.append(record[0])
                        print k,'.',record[0]
                        k=k+1
                    m=input('Select username to login: ')
                    c=d.cursor()
                    y=l1[m-1]

                    if c.execute('''select pass from info where site=? AND uname=?''', (o, y)):
                        c = c.fetchall()
                        for record in c:
                            p = encry.dec(record[0])
                        f(y, p)



if len(sys.argv)==3:
    s=sys.argv[1]
    u=sys.argv[2]
    if s=="gmail":
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
            c=c.fetchall()
            for record in c:
                p = encry.dec(record[0])

            pro.gmail(u,p)
    else:
         print 'Wrong details'

    if s=='fb' or s=='facebook':
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
            c = c.fetchall()
            for record in c:
                p = encry.dec(record[0])
            pro.fb(u, p)
        else:
            print 'Wrong details'

    if s=='twitter':
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
           c=c.fetchall()
           for record in c:
                p = encry.dec(record[0])
           pro.twitter(u, p)
        else:
            print 'Wrong details'


    if s=='youtube':
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
           c=c.fetchall()
           for record in c:
               p = encry.dec(record[0])
           pro.youtube(u, p)
        else:
            print 'Wrong details'


    if s=='odrive' or s=='onedrive':
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
           c=c.fetchall()
           for record in c:
               p = encry.dec(record[0])
           pro.odrive(u, p)
        else:
            print 'Wrong details'


    if s=='gdrive'or s=='googledrive':
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
           c=c.fetchall()
           for record in c:
                p = encry.dec(record[0])
           pro.gdrive(u, p)
        else:
            print 'Wrong details'


    if s=='linkedin':
        if c.execute('''select pass from info where site=? AND uname=?''', (s, u)):
           c=c.fetchall()
           for record in c:
                p = encry.dec(record[0])
           pro.linkedin(u, p)
        else:
            print 'Wrong details'
