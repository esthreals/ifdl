import urllib.request
from time import sleep
import numpy as np
import pyperclip



def get_sleep_time(avg):
	return np.random.uniform(0.5*avg, 1.5*avg)


def main():
	AVG_SLEEP_TIME = 2 # You can play around with this value and see how bot detection reacts.

	url = input("Url of the gallery (https://www.imagefap.com/pictures/12345678/Gallery%20Name):\n")

	url = url.split("?")[0]
	url += "?view=2&page=0"
	page_number = 0
	group_links = []

	print("Scanning pages...")
	while True:
		request =  urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
		response = str(urllib.request.urlopen(request).read())
		splitstring = "/photo/"
		response = response.split(splitstring)

		if len(response) == 1:
			break

		for i in range(1, len(response), 24):
			group_link = "https://www.imagefap.com/photo/" + response[i].split("\"")[0]
			if (group_link in group_links):
				break
			group_links.append(group_link)
		else:
			print("Page", page_number+1, "is scanned", end='\r')
			page_number += 1
			url = url.split("page=")[0] + "page=" + str(page_number)
			sleep(get_sleep_time(AVG_SLEEP_TIME))
			continue

		break

	image_links = ""
	image_links_short = []

	print("\nGetting image links...")
	for i in range(0, len(group_links)):
		request =  urllib.request.Request(group_links[i], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
		while True:
			response = str(urllib.request.urlopen(request).read())
			splitstring = "https://cdn.imagefap.com/images/full/"
			response = response.split(splitstring)
			if len(response) == 1:
				sleep(get_sleep_time(AVG_SLEEP_TIME))
				continue
			break
		
		for j in range(1, len(response), 2):
			image_link = "https://cdn.imagefap.com/images/full/" + response[j].split("\"")[0]
			image_link_short = image_link.split("?")[0]
			if image_link_short not in image_links_short:
				image_links_short.append(image_link_short)
				image_links += image_link + "\n"

		print("Progress: " + str(round((i+1)/len(group_links)*100, 2)) + "% ", end='\r')

		sleep(get_sleep_time(AVG_SLEEP_TIME))

	print(len(image_links_short), "image links are collected and copied to your clipboard.")
	pyperclip.copy(image_links)
	spam = pyperclip.paste()

	print("You can now close this window.")

	while True:
		# Wait until application is closed. 
		continue


if __name__ == "__main__":
	main()
