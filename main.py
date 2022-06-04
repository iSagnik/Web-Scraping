import webscraper
import model
from selenium import webdriver
from PIL import Image

DRIVER_PATH = '.Desktop/Project/Web-Scraping/chromedriver'
FOLDER_PATH = './images'
THRESHOLD = 70

def user_inputs():
    query = input("Enter search term")
    img_path = input("Enter image path")
    min_img = int( input("Enter images to be found") )

    return (query, img_path, min_img)


def main():
    query, img_path, min_img = user_inputs()

    sample_img = Image.open(img_path)

    images = run_script(query, sample_img, min_img)
    #do something with images
    webscraper.store_images(images, FOLDER_PATH)

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
        score = model.get_similarity_score(sample_img, image_file)

        if score >= THRESHOLD:
            foundImages.add(image_file)

if __name__== "__main__":
    main()