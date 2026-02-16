import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

print("================================================================")
model1 = load_model("model/model_vscode_10epoch.h5",compile=False)
if model1:print("model loaded successfully : model_vscode_10epoch.h5")
model2 = load_model("model/model_vscode_20epoch.h5",compile=False)
if model2:print("model loaded successfully : model_vscode_20ep0ch.h5")
model3 = load_model("model/model_colab.h5",compile=False)
if model3:print("model loaded successfully : model_colab.h5")
model4 = load_model("model/model_windows_15epoch.h5",compile=False)
if model4:print("model loaded successfully : model_windows_15epoch.h5")
model5 = load_model("model/model_128_20epoch.h5",compile=False)
if model5:print("model loaded successfully : model_128_20epoch.h5")
print("================================================================")

a=b=c=d=e=n=0
for file in os.listdir("img"):
    print("Real Image" , file[:3])
    path="img/"+file
    img_display = image.load_img(path)
    plt.imshow(img_display)
    plt.title(file[:3])
    plt.axis("off")
    plt.show()
    
    img=image.load_img(path,target_size=(64,64))
    img_array = image.img_to_array(img)
    img_array=np.expand_dims(img_array,axis=0)
    img_array/=255.0
    
    img128=image.load_img(path,target_size=(128,128))
    img_array128 = image.img_to_array(img128)
    img_array128=np.expand_dims(img_array128,axis=0)
    img_array128/=255.0

    p1="Dog" if model1.predict(img_array)[0][0]>0.5 else "Cat"
    p2="Dog" if model2.predict(img_array)[0][0]>0.5 else "Cat"
    p3="Dog" if model3.predict(img_array)[0][0]>0.5 else "Cat"
    p4="Dog" if model4.predict(img_array)[0][0]>0.5 else "Cat"
    p5="Dog" if model5.predict(img_array128)[0][0]>0.5 else "Cat"
    print("-----------------Result-------------------")
    print("Prediction of Model 1 (model_vscode_10epoch.h5) :",p1)
    print("Prediction of Model 2 (model_vscode_20epoch.h5) :",p2)
    print("Prediction of Model 3 (model_colab.h5)          :",p3)
    print("Prediction of Model 4 (model_windows_15epoch.h5):",p4)
    print("Prediction of Model 5 (model_128_20epoch.h5)    :",p5)
    if(file[:3].lower()=="man"):print(model1.predict(img_array),model2.predict(img_array),model3.predict(img_array),model4.predict(img_array),model5.predict(img_array128),sep="\n")
    print("--------------------------------------")
    if p1.lower()==file[:3].lower():a+=1
    if p2.lower()==file[:3].lower():b+=1
    if p3.lower()==file[:3].lower():c+=1
    if p4.lower()==file[:3].lower():d+=1
    if p5.lower()==file[:3].lower():e+=1
    n+=1
    print("================================================================\n\n\n")
print("\n\n")
print("==============================Report================================")
print(f"Model 1 (model_vscode_10epoch.h5)   : predicted {a} out off {n}")
print(f"Model 2 (model_vscode_20ep0ch.h5)   : predicted {b} out off {n}")
print(f"Model 3 (model_colab.h5)            : predicted {c} out off {n}")
print(f"Model 4 (model_windows_15epoch.h5)  : predicted {d} out off {n}")
print(f"Model 5 (model_128_20epoch.h5)      : predicted {e} out off {n}")
print("==============================Report================================")
