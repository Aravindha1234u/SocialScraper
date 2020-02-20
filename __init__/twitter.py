import requests
from bs4 import BeautifulSoup

def ScrapTweets(user):
    print (W + '[+]' + G + ' Fetching Data From Twitter...' + '\n')
    link = "https://twitter.com/" + user
    the_client = uReq(link)
    page_html = the_client.read()
    the_client.close()

    soup = BeautifulSoup(page_html, 'html.parser')

    try:
        full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        print("User Name --> " + W + str(full_name.text))
    except:
        print("User Name -->"+ R +" Not Found")
    print()

    try:
        user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
        print("User Id --> "+W + str(user_id.text))
    except:
        print("User Id --> "+R+"Not Found")
    print()

    try:
        decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
        print("Description --> "+W + str(decription.text))
    except:
        print(R+"Decription not provided by the user")
    print()

    try:
        user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
        print("Location -->  " +  str(user_location.text.strip()))
    except:
        print(R+"Location not provided by the user")
    print()

    try:
        connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
        title = connectivity.a["title"]
        print("Link provided by the user --> " + str(title))
    except:
        print(R+"No contact link is provided by the user")
    print()

    try:
        join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        print("The user joined twitter on --> " + str(join_date.text))
    except:
        print(R+"The joined date is not provided by the user")
    print()

    try:
        birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        print("Date of Birth:"+str(birth_date.strip()))
    except:
        print(R+"Birth Date not provided by the user")
    print()

    try:
        span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
        print("Total tweets --> " + span_box[0].text)
    except:
        print(R+"Total Tweets --> Zero")
    print()

    try:
        print("Following --> " +span_box[1].text)
    except:
        print(R+"Following --> Zero")
    print()

    try:
        print("Followers --> " + span_box[2].text)
    except:
        print(R+"Followers --> Zero")
    print()

    try:
        print("Likes send by him --> " + span_box[3].text)
    except:
        print(R"Likes send by him --> Zero")
    print()

    try:
        if span_box[4].text != "More ":
            print("No. of parties he is Subscribed to --> " + span_box[4].text)
        else:
            print("No. of parties he is Subscribed to --> Zero")
    except:
        print("No. of parties he is Subscribed to --> Zero")
    print(W)

    spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

    print("Tweets by "+ str(username) + " are --> ")
    # TweetTextSize TweetTextSize--normal js-tweet-text tweet-text
    for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        print(tweets.text)
        print()
