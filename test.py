from LCSMap import LCSMap


fName = "/home/carlo/Documenti/Progetti/tesi/appLog/ArsAlimentaria.log"
with open(fName) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

map = LCSMap()
for line in content:
    map.insert(line)
print "Test Results:"
print map.toString()
