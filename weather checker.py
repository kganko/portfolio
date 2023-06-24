# idea behind the project: you can check if you can go for a date today

# find where I am
g = geocoder.ip('me')
print(g.latlng)

geoLoc = Nominatim(user_agent="GetLoc")

locname = geoLoc.reverse(g.latlng)
print(locname.address)


# find our city
myaddress = locname.address
sub_str = ","
occurrence = 4

val = -1
for i in range(0, occurrence):
    val = myaddress.find(sub_str, val + 1)

mycity = locname.address[val+2:80]


# use Google to check weather
query = "weather in " + mycity
print(f"Searching for the query : {query}")
search(query)

# save screenshot
screenshot = pyautogui.screenshot()
screenshot.save(r"C:\Users\kinga\Desktop\wszystko\materiały\screenshot.png")

# sending an email to some mailtrap address. Why? Because I can't use gmail, that's why

sender = "Me <from@example.com>"
receiver = "My Beloved Boyfriend <to@example.com>"

message = f"""\
Subject: Weather for today
To: {receiver}
From: {sender}
Attachment: {screenshot}

Oh honey, did you see the weather for today?"""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("64a41c570be75b", "d45fd632ec4183")
    server.sendmail(sender, receiver, message)
