import os
import gdown
print(os.getcwd())
os.chdir("checkpoints/i2v")
print(os.getcwd())
url='https://www.googleapis.com/drive/v3/files/1nFX0Nbt2UhUP1RNEiLC7QYoNtGku0_dd?alt=media&key=AIzaSyCU0oV3GFzGvNeB2LOb3Ycrg789vDtwwZE'
id='1nFX0Nbt2UhUP1RNEiLC7QYoNtGku0_dd'
output='model.ckpt'
api='AIzaSyCU0oV3GFzGvNeB2LOb3Ycrg789vDtwwZE'
gdown.download(url=url,output=output,quiet=False)