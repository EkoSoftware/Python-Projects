
""" 
Dependencies:
    python -m pip install segno
"""
from segno import make_qr
from datetime import datetime
from sys import argv


debug = False
if debug == True: print(argv[0])   #   Python-Filen
if debug == True: print(argv[1])   #   URL argumentet
if debug == True: print(argv[2])   #   Storleks argumentet


# Variablar
now = datetime.now()
time = now.strftime("%H:%M:%S")
outfile = f"QR_({time})_.png"
   
url = argv[1]
storlek = argv[2]

# Funktioner
def die():
    print(f"Användning: skapaqr.py URL storlek_mellan_1_till_10")
    print(f"Exempel: python skapaqr.py https://makabgroup.se/support-2/ 1-10")
    print(f"Alla storlekar: python skapaqr.py https://makabgroup.se/support-2/ *")
    exit(1)

def makeone(url, storlek):
    make_qr(url,).save(outfile,scale=storlek)
    print(f"File saved as {outfile}")
    
def makemany(url):
    for i in range (1,11):
        outfile = f"QR_{str(i)}_({time})_.png"
        make_qr(url,).save(outfile,scale=i)



# Kör programmet
if __name__ == '__main__':
    assert len(argv) > 1, die()
    if storlek.isnumeric(): 
        makeone(url, storlek)
    else: 
        makemany(url)

    


