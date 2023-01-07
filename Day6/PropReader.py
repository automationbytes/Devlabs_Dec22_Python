from jproperties import Properties

profile = Properties()

with open("Config.properties","rb") as configfile:
    profile.load(configfile)
print(profile.get("fruit").data)
