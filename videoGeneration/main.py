from renderReddit import * 
from redditParser import Scraper

s = Scraper(
		"TiktokAdBot19",
		"blueblanket",
		"SMBZQHgBa7urm4vjwvJXCA",
		"nD1mufVJdBtLR4KGHVhs8xe9HMx4Lg",
		"Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0")


with open("newLinks.txt", "r") as f:
	for line in f.readlines():
		# lines have link, number of comments

		content = line.split(",")

		link = content[0].replace(" ", "")
		num = int(content[1].replace(" ", ""))

		if num == -1:
			askRedditComment(
				link,
				"C:\\Users\\pging\\Desktop\\Ad Automator\\videoGeneration\\assets\\videos\\minecraft_parkour_3.mp4",
				"video0" 
			)
		else:
			askReddit(
				link, 
				num,	
				"C:\\Users\\pging\\Desktop\\Ad Automator\\videoGeneration\\assets\\videos\\minecraft_parkour_3.mp4",
				"video0" 
				)

		with open("listoflinks.txt", "a") as f:
			f.write(link)
			
