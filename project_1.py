#### collect contents from website and store it in database

import requests
from bs4 import BeautifulSoup
import sqlite3

# connect to SQLite, create new db if not exists
conn = sqlite3.connect('r_brookyln.db')
# print("Successfully connected")

# create a table
conn.execute(''' Create table if not exists res_data(Name, Contact, Address);''')
# print("Table created successfully")


# using yellowpages as url
url = "https://www.yellowpages.com/brooklyn-ny/restaurants"

# sending response
response = requests.get(url)

# parsing
soup = BeautifulSoup(response.content, 'html.parser')

# finding location
name = soup.find_all("a", class_ = "business-name")
contact = soup.find_all("div", class_ ="phones phone primary")
address = soup.find_all("div", class_ ="adr")


for names, contacts, address_s in zip(name, contact, address):
    name_text = names.text.strip()
    contact_text = contacts.text.strip()
    address_text = address_s.text.strip()

    print(name_text, contact_text, address_text)

 # insert data in database
    conn.execute("INSERT INTO res_data VALUES(?, ?, ?)", (name_text, contact_text, address_text))

    # commit changes
    conn.commit()


# close connection
conn.close()
