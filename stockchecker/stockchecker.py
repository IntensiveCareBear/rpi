import requests
from gpiozero import LED
from time import sleep

RED = 22
GREEN = 27
BLUE = 17
INTERVAL_S = 5*60
UDM_URL = 'https://store.ui.com/products/udm-pro'
NEEDLE = '<span class="text">Sold Out</span>'

def fetch_contents() -> str:
	request = requests.get(UDM_URL, headers={'Connection':'close'})
	return request.text

def check_stock(contents: str) -> bool:
	return NEEDLE in contents

def main():
	red = LED(RED)
	green = LED(GREEN)
	blue = LED(BLUE)
	while True:
		red.off()
		green.off()
		blue.off()
		sold_out = check_stock(fetch_contents())
		if sold_out:
			red.on()
		else:
			green.on()
		sleep(INTERVAL_S)
if __name__ == '__main__':
	main()