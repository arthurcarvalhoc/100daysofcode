
from datetime import date
from datetime import datetime

datetime.today()


today = datetime.today()

type(today)
# <class 'datetime.datetime'>


today_date = date.today()

today_date


type(today_date)
# <class 'datetime.date'>

today_date.month


today_date.year


today_date.day



christmas = date(today_date.year, 12, 25)
christmas
# datetime.date(2021, 12, 25)

# We need to use != & == rather than is / is not for comparison. Sorry for the mistake in the video.
if christmas != today_date:
    print("Sorry there are still " + str((christmas - today_date).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")