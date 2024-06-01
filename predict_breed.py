from fastai.learner import load_learner


# Function to make predictions
def predict(image):
    model = load_learner('pet_breed_model.pkl')
    _, idx, probabilities = model.predict(image)
    predicted_class = model.dls.vocab[idx[0]]
    probability = probabilities[idx[0]].item() * 100
    return predicted_class, probability

# def predict(image):
#     learn = load_learner('pet_breed_model.pkl')
#     breed, _, probs = learn.predict(image)
#     return breed
