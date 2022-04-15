# set the font
font('CondorVariable-VF.ttf', 200)
# query the font variations
print(listFontVariations())
print()
# now ask it about the width axis, which is a dictionary with attributes
print(listFontVariations()['wdth'])
print()

# what attributes do we have for the width axis
print(listFontVariations()['wdth'].keys())
print()
# now ask it about the minimum value specifcially 
print(listFontVariations()['wdth']['minValue'])

# set the font variations
myMinValue = listFontVariations()['wdth']['minValue']
fontVariations(wdth=myMinValue)
text('Hello world', (0, 0))
