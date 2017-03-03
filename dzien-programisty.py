import datetime

today = datetime.datetime.now().timetuple().tm_yday

if today == 0x100:
    print("dzisiaj jest dzien programisty")

