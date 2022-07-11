import os 


def createAssets(paragraphs, dirr):

    for index, paragraph in enumerate(paragraphs):
        if os.name == "nt":
            command = f'magick -size 350x -font DejaVu-Sans -background none -undercolor white -gravity Center -pointsize 8 -fill black -stroke none caption:\"{paragraph}\" -bordercolor none -border 12 ^( +clone -morphology dilate disk:4 ^) +swap -composite {os.path.join(dirr, f"img{index}.png")}'
        else:
            command = f'magick -size 350x -font DejaVu-Sans -background none -undercolor white -gravity Center -pointsize 10 -fill black -stroke none caption:\"{paragraph}\" -bordercolor none -border 12 \( +clone -morphology dilate disk:5 \) +swap -composite {os.path.join(dirr, f"img{index}.png")}'

        os.system(command)          




'''

s = Scraper(
	"TiktokAdBot19",
	"blueblanket",
	"SMBZQHgBa7urm4vjwvJXCA",
	"nD1mufVJdBtLR4KGHVhs8xe9HMx4Lg",
	"Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0")
'''
'''
for index, item in enumerate(
    s.listParagraphs(
        s.scrapeTexts("tifu", "wife", 2)[0]
    )):

        createAssets(item, os.path.join(os.getcwd(), "test", f"image{index}.png" ))
'''
#createAssets(s.listParagraphs(s.scrapeTexts("shsat", "patch", 10)[0]), os.path.join("./test", "img.png"))
'''

p = "Yesterday I was getting ready for work and put on some brand new undies out of the package. I've always usually washed them first for fear that some weird detergent or something could harm my dong or make my butt itchy, but I was in a hurry and grabbed some and threw them on and headed to work."
createAssets([p],os.path.join("./test", "img.png"))'''