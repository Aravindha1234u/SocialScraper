<h1 align="center">SocialScraper</h1><br>
<p align="center">
  <img src="https://img.shields.io/badge/build-passed-brightgreen" alt="build status">
  <img src="https://img.shields.io/badge/analyze-passed-rightgreen" alt="Analyze">
  <img src="https://img.shields.io/badge/tests-477%20passed%2C%202%20failed-red" alt="version">
  <img src="https://img.shields.io/badge/coverage-75%25-green" alt="Coverage"></br>
  <img src="https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen" alt="Test">
  <img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python V3.7">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Status-up-brightgreen" alt="status-up"><br><br>
Social Scraper is a python tool meant for Detection of Child Predators/Cyber Harassers on Social Media
</p><br>

Tool intends to identify the cyber predators/child harassers on social media with a malevolent intend. The posts, comments and followers on the social media are subjected to analysis using **Artificial Intelligence**, **Machine Learning** with IGPL and **NSFW(Not Safe For Work)** to categorise the offensive contents.

This system is capable of analyzing all social media platforms like **Instagram, Twitter, Facebook,** etc., and other outlets seeking the same suspect. If the suspect doesn’t have the same user ID on different platforms, then Reverse Image Searching is done to identify the suspect. A set of user_id is used as a key to grab their personal information and their **post information(Post ID, Comments, Timestamp, location, Captions)** from multiple social platforms using ​ **OSINT(Open Source INTelligence)** and **Beautifulsoup** Python Package. The above data of various posts are subjected to analyze malevolent contents using Machine Learning and Pandas Python library.Based on the statistical analysis, suspects are categorized based on their behavior(also Polite harassment). The users whose suspect level is greater than the threshold value will be scrutinized and monitored for further analysis. The suspected user’s post information(media like Image, Audio, and Video) is retrieved and analyzed using the ​ **IGPL** Python package, ​ Urllib and ​ Artificial Intelligence with ​ NSFW (Not Safe For Work) library to make them fall under the category 'suspects/predators'. Finally, the Child grooming patterns followers and statistical results that are generated are analyzed and the concerned person is classified as predator and reported to the law enforcement authorities

![Tool UI](https://drive.google.com/uc?export=view&id=1e5smGCgv0GavbmotU3_ntOpo1FNGUez0)
***

**Creators:**  :bust_in_silhouette:
> [Aravindha Hariharan M](https://github.com/Aravindha1234u)  
> [Kabilan S](https://github.com/kabilan1290)  
> [Gowtham G](https://github.com/Gowtham-18)  
> [Giridhara Prasath G](https://github.com/giridhar30)   



### Prerequisites  :package:
1.Python 3.X with pip3 Installed  
If not then, pip3 installation  
```
apt install python3-pip
```  
To Check pip versioon  
```
pip3 --version
```

2.Geckodriver for Mozilla Firefox  
If you havn't installed then,
Visit the link below, Download the required file for resepective operating system and install.
```
https://github.com/mozilla/geckodriver/releases
```

### User List Creation
Tool can handle N-number of user account scrapping which can be given a user.txt
 
You can use any kind of text editor to edit user.txt
```
gedit user.txt | vim user.txt
```
### Installation  :floppy_disk:
**Python Direct module Installation**

```
python3 -m pip install SocialScraper
```

**From Source Package**

Open Terminal and type
```
git clone https://github.com/Aravindha1234u/SocialScraper

cd SocialScraper
```
**Automatic Setup**

```
chmod +x setup

./setup
```

**Manual Setup**

To Install required Python package

```
pip3 install -r requirements.txt
```
or
```
python3 -m pip install -r requirements.txt
```
### Api Keys
We haven't included our keys for usage. Add your respective api keys to SocialScraper/social/api.py and replace the google credentials.json and client_secret.json to sample directory and facebook credentials in credentials.yaml for scrappering the accounts.

** Google API ** <br>

Get it signed in and once you get your API key, make sure that you have enabled gmail service to this.So that automatic mail can function.
    [Gmail API](https://developers.google.com/gmail/api)

** Imagga API ** <br>

Sign up as a hacker and get the API key.
    [Imagga API](https://imagga.com/auth/signup/hacker)
    
** DeepAI ** <br>

Sign up and get the API key 
    [DeepAI API](https://deepai.org/)

### Execution  :+1:
To Run SocialScraper
```
python3 main.py
```
### Issues
Feel free to express any kind of bug or error in this tool by reporting it in issues, So that it can be fixed soon.<br>
<a href="https://github.com/Aravindha1234u/SocialScraper/issues"><img src="https://img.shields.io/badge/issues-33-yellow" /></a>

### Important Message  :warning:

>This tool is for research purposes only. Hence, the developers of this tool won't be responsible for any misuse of data collected using this tool. Used by many researchers and open source intelligence (OSINT) analysts.

### License  :page_facing_up:
SocialScraper is licensed under GNU General Public License v3.0. Take a look at the [License](https://github.com/Aravindha1234u/SocialScraper/blob/master/LICENSE)

***
# Tool Working :flower_playing_cards:
![Tool Working](https://drive.google.com/uc?export=view&id=1y2SVImVtBh_kviigOfFg2Sj2NP98i7Wr)
