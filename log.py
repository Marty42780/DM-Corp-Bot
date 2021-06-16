import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gclient = gspread.authorize(creds)
sheet = gclient.open("BAP-Bot logs 1").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

def log(author, text, channel, args):
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime('%d/%m/%Y %H:%M:%S', named_tuple)
    col = sheet.col_values(1)  # Get a specific column
    sheet.update_cell(col.__len__()+1, 1, time_string) # Loger le Temps
    sheet.update_cell(col.__len__()+1, 2, author) # Loger le User
    sheet.update_cell(col.__len__()+1, 3, text) # Loger le Text
    sheet.update_cell(col.__len__()+1, 4, channel) # Loger le channel
    sheet.update_cell(col.__len__()+1, 5, args) # Loger les args
    print ('[' + time_string + ']', '{' + author + '}', text, 'in ' + channel, ':', args)

# https://www.youtube.com/watch?v=cnPlKLEGR7E