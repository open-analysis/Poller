#! python3
# CNN_sitemap_test       goes through CNN's sitemap to gather political pagesZ

import requests, os, bs4, threading

site = 'cnn'
os.makedirs(site, exist_ok=True)    # store comics in ./xkcd


def downloadPage():
    url = 'https://cnn.com'
    # Download the page.
    print('Downloading page https://cnn.com/...')
    res = requests.get(url+'/sitemap.html')
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    article_endings = []
    special_endings = []
    
    dateElem = soup.select('.date')
    for elem in dateElem:
        ref = elem.find('a')
        href = ref.get('href')
        # to only get articles
        if href[1] is 'a':
            #print(href)
            article_endings.append(href)
        # to get special
        elif href[1] is 's':
            if href[2] is 'p':
                #print(href)
                special_endings.append(href)
    
    url_endings = [article_endings, special_endings]
    #print(url_endings)
    #print(article_endings)
    #print(special_endings)
    
    month_endings = []
    
    print("Checking yearly sitemaps")
    for endings in url_endings:
        print("Checking specific sitemaps")
        for end in article_endings:        
            res = requests.get(url+end)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            monthElem = soup.select('.month')

            for month in monthElem:
                ref = month.find('a')
                if ref is None:
                    continue
                href = ref.get('href')
                #print(href)
                month_endings.append(href)
    
    #print(month_endings)
    final_urls = []
    
    print("Checking monthly entries")
    for month in month_endings:
        print('\t' + url + month)
        res = requests.get(url+month)
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        entryElem = soup.select('.sitemap-link')
        #entryElem = soup.find_all('a')
        #print(entryElem[0])
        #print(entryElem)


        for entry in entryElem:
            if entry.string == 'Title':
                continue
            #print(entry)
            ref = entry.find('a')
            #print(ref)
            if ref is None:
                continue
            href = ref.get('href')
            #print(href)
            final_urls.append(href)
        
    # save the urls for later
    print ('Writing urls down...')
    pageFile = open(os.path.join('cnn', 'urls.txt'), 'w')
    for line in final_urls:
        pageFile.write(line)
        pageFile.write('\n')

    pageFile.close()
            
'''
# Create and start the Thread objects.
pageThreads = []             # a list of all the Thread objects
for i in range(0, 140, 10):    # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1 # There is no comic 0, so set it to 1.
    pageThread = threading.Thread(target=downloadPage, args=(start, end))
    pageThreads.append(pageThread)
    pageThread.start()
    
# Wait for all threads to end.
for pageThread in pageThreads:
    pageThread.join()
'''
downloadPage()

print('\nDone.')