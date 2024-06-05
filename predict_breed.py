from fastai.learner import load_learner
from PIL import Image


def predict(image):
    learn = load_learner('pet_breed_model.pkl')
    breed, _, probs = learn.predict(image)
    # return breed
    breed_idx = learn.dls.vocab.o2i[breed]  # Get the index of the predicted breed
    breed_prob = probs[breed_idx].item()  # Get the probability of the predicted breed
    return [breed, breed_prob]

# if __name__ == '__main__':
#     image = Image.open('test_image.jpeg')
#     print(predict(image))