import pickle
with open(r"C:\Users\lenovo\OneDrive\Desktop\Lumiq\Sprint_7_DS\model_final.pkl", 'rb') as file:
    model = pickle.load(file)

data = [[11001,55912,26000,7866,201,6,54,0,15,1,706,1,0,36000,3204,60,70,7]]
prediction = model.predict(data)
print(prediction)