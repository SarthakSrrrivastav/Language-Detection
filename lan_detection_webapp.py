import numpy as np

import streamlit as st
import pickle



# loading the saved model

load_model=pickle.load(open('trainedmodel.sav','rb'))


# creating the function for lan_detection


def predict(text):
    lang=load_model.predict([text])
    return 'THE LANGUAGE IS : ',lang[0]


def main():


	# giving the title

	st.title('LANGUAGE DETECTION')


	# getting the input from the user


	text=st.text_input('Type the language to detect')

	if st.button('DETECT THE LANGUAGE'):
		result=predict(text)
		st.success(result)

		

	




	# result=''

 
  # 
  # 	
	 #  	

if __name__=='__main__':
	main()

			
