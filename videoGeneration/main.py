from renderReddit import * 
from redditParser import Scraper


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
			
/////
