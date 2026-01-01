import pickle

#loading the model
with open('models/lr_model.pkl','rb') as f:
    model=pickle.load(f)

MODEL_VERSION='1.0.0'