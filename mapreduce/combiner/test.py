import sys

testval = "Music	GB=13754,US=6472,FR=3946,RU=1873,CA=3731,KR=1806,JP=1261,DE=2372,IN=3792,MX=3330"
category, countrycounts = testval.strip().split("\t", 1)
values = []
values = values.append(lambda x: x.split("=")[0] for country in countrycounts.split(","))
#print(values)
print([country.split("=")[1] for country in countrycounts.split(",")])
