# determine time of day
import datetime
import random
from inky import InkyWHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
import textwrap

# setting inky variables
inky_display = InkyWHAT("red")
inky_display.set_border(inky_display.WHITE)

# setting PIL image classes
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 24)

# morning, evening, sabbath, midday verse databases
morning = {
    "Psalm 143:8":"Let me hear in the morning of your steadfast love, for in you I trust. Make me know the way I should go, for to you I lift up my soul.",
    "Psalm 3:5":"I lay down and slept; I woke again, for the Lord sustained me.",
    "Psalm 5:3":"O Lord, in the morning you hear my voice; in the morning I prepare a sacrifice for you and watch.",
    "Psalm 90:12":"So teach us to number our days that we may get a heart of wisdom.",
    "Psalm 90:14":"Satisfy us in the morning with your steadfast love, that we may rejoice and be glad all our days."
}

evening = {
    "Psalm 4:4":"Be angry, and do not sin; ponder in your own hearts on your beds and be silent.",
    "Psalm 91:9":"Because you have made the Lord your dwelling place - the most High, who is my refuge - no evil shall be allowed to befall you, no plague come near your tent.",
    "Psalm 13:3":"Consider and answer me, O Lord my God; light up my eyes, lest I sleep the sleep of death.",
    "Psalm 121:3":"He will not let your foot be moved; he who keeps Israel will neither slumber nor sleep.",
    "Psalm 121:7":"The Lord will keep you from all evil; he will keep your life. The Lord will keep your going out and coming in from this time forth and forevermore."
}

midday = {
    "Psalm 110:1":"The Lord says to my Lord: 'Sit at my right hand, until I make your enemies your footstool.'",
    "Psalm 119:15":"I will meditate on your precepts and fix my eyes on your ways. I will delight in your statutes; I will not forget your word.",
    "Psalm 119:27":"Make me understand the way of your precepts, and I will meditate on your wondrous works."
}

# set current hour to varaiable
t = datetime.datetime.now()
currenthour = t.hour

# select random verse depending on time of day, set message and psalm variables
if currenthour <= 10:
    verse = list(morning.items())[random.randrange(0,4)]
    message = verse[1]
    psalm = verse[0]
elif currenthour <= 16:
    verse = list(midday.items())[random.randrange(0,2)]
    message = verse[1]
    psalm = verse[0]
elif currenthour > 16:
    verse = list(evening.items())[random.randrange(0,4)]
    message = verse[1]
    psalm = verse[0]

# wrap text and draw verse and psalm on display
wrap = textwrap.wrap(message,width=20)
wrappedmessage = "\n".join(wrap)

draw.multiline_text((5, 5), wrappedmessage, inky_display.BLACK, font, align="left")
draw.text((265,265),psalm,inky_display.RED, font, align="left")

inky_display.set_image(img)
inky_display.show()
