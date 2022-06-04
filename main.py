import webscraper
from selenium import webdriver

DRIVER_PATH = '.Desktop/Project/Web-Scraping/chromedriver'
THRESHOLD = 70

def main():
    query = ""
    img_url = ""
    min_img = 10

    images = run_script(query, img_url, min_img)
    #do something with images

def run_script(query, sample_img, min_img):
    foundImages = set()
    urls_seen = set()

    while len(foundImages) < min_img:
        with webdriver.Chrome(executable_path=DRIVER_PATH) as wd:
            image_urls_to_check = webscraper.fetch_image_urls(query, urls_seen, min_img * 2, wd=wd, sleep_between_interactions=0.5)

            check_similarity(image_urls_to_check, sample_img, foundImages)

    return foundImages

def check_similarity(images_to_check, sample_img, foundImages):
    
    for image in images_to_check:
        image_file = webscraper.download_image(image)

        #check similarity
        score = get_similarity_score(sample_img, image_file)

        if score >= THRESHOLD:
            foundImages.add(image_file)

def get_similarity_score(sample_img, image_file):
    pass

if __name__== "__main__":
    main()