import requests,re
myList=[]
myNewNothing= str(63579)
for i in range(400):
    res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+myNewNothing)
    res.raise_for_status()
    findNothing=re.compile(r'\d+')
    for chunck in res.iter_content(100000):
        myList +=str(chunck)
    myListS = ''.join(myList)
    mo = findNothing.search(myListS)
    if mo is None:
        print(myNewNothing)
        break
    myNewNothing = str(mo.group())
    myList=[]
    print(myNewNothing)
    




