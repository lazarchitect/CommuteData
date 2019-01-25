# CommuteData
Simple Python Script for gathering data for my daily commute and adding it to a database for later analysis. Mostly intended to be a project where I work with some advanced data processing tools, but it's also something I'd like to know more about, considering it affects a huge part of my day, every day.

The work is done with Selenium to access Google Maps' regular directions data. 
Unfortunately, simple web scraping with BeautifulSoup didn't work due to the nature of the JavaScript-based containers, so Selenium actually loads up a browser, gets the data, and closes the browser. 
Then, the data is written to a CSV with Python's file writing tools. Repeat ad infinitum, every 5 minutes. 
I plan to leave the program running on my Raspberry Pi for several weeks to gather data.
