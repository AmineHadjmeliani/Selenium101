## Web Scraping Using Selenium

In this code we use the Selenium and Pandas libraries to scrape the football match results from a website. The script starts by creating a Chrome options object and a Chrome driver object, setting the window to be maximized, and opening the URL of the website to scrape. The user is then prompted to input the desired country, league, and season for which they want to scrape the results.

A function named load_data is defined to automate the scraping process. This function clicks on the "All matches" button, selects the country, league, and season using the Select class, waits for 6 seconds to allow the table to load, and finally, locates all the matches in the table and extracts the relevant information (i.e. the date, home team, score, and away team) into separate lists.

Finally, the extracted information is stored in a Pandas dataframe and can be further processed or saved to a file.


