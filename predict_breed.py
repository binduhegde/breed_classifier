from fastai.learner import load_learner


def predict(image):
    learn = load_learner('pet_breed_model.pkl')
    breed, _, probs = learn.predict(image)
    return breed