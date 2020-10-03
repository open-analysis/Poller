#! python3
# threadeddownloadPage.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading

site = 'cnn'
os.makedirs(site, exist_ok=True)    # store comics in ./xkcd


def downloadPage():
    url = 'https://cnn.com/2020/06/08/politics/donald-trump-joe-biden-police-funding/index.html'
    # Download the page.
    print('Downloading page https://cnn.com/...')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    pageElem = soup.select('.zn-body__paragraph')
    #print(pageElem[0].text)
    if pageElem == []:
        print('Could not find element.')
    else:
        # Download the page.
        print('Downloading page %s...' % (url))
        pageFile = open(os.path.join('cnn', site +  '_' + 'trump_police'), 'w')
        for elem in pageElem:
            pageFile.write(elem.text)
        
        pageFile.close()
'''
# Create and start the Thread objects.
downloadThreads = []             # a list of all the Thread objects
for i in range(0, 140, 10):    # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.
    downloadThread = threading.Thread(target=downloadPage, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
'''
downloadPage()

print('Done.')