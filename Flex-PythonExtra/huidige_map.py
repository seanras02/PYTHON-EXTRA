import os

werkmap = os.getcwd()

print("De huidige map is:" + werkmap)

os.mkdir("Een nieuwe map")

mapnaam = input("Welke naam wil je voor je map?")

lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map" + mapnaam + "is gemaakt")
else:
    print("je hebt geen naam ingevoerd")
