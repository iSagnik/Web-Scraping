from scipy import spatial
import numpy as np

#https://towardsdatascience.com/what-is-cosine-similarity-how-to-compare-text-and-images-in-python-d2bb6e411ef0

# frog = Image.open('frog.jpg')
# frog_reshape = frog.resize((round(dog1.size[0]*0.5), round(dog1.size[1]*0.5)))
# frog_array = np.array(frog_reshape)
# frog_array = frog_array.flatten()
# frog_array = frog_array/255

# similarity = -1 * (spatial.distance.cosine(dog_array1, frog_array) - 1)

def get_similarity_score(sample_img, image_file):
    sample_reshape = image_file.resize((round(sample_img.size[0]*0.5), round(sample_img.size[1]*0.5)))
    sample_array = np.array(sample_reshape).flatten()
    sample_array = sample_array / 255

    image_reshape = image_file.resize((round(sample_img.size[0]*0.5), round(sample_img.size[1]*0.5)))
    image_array = np.array(image_reshape).flatten()
    image_array = image_array / 255

    similarity = -1 * (spatial.distance.cosine(sample_array, image_array) - 1)

    return similarity * 100
