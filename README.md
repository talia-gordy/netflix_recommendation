# 🎬 Netflix Movie and TV show reccomendation ML project

## 📝 Description:

### A ML (Machine Learning) project written in Google Collab and Visual Stuido Code with Python and ML libaries, to provide suggestions on a users next favorite movie or TV show within Netflix! 
- [Google Collab](https://colab.google/) was used to create the trained model as it's a free and widely used notebook that allows people to train complex machine-learning models efficently in a collabrative environment.
- [Streamlit](https://streamlit.io/) was used to provide a visual UI and deploy the app.
- [Visual Studio Code](https://code.visualstudio.com/download) was the second coding environment used in this porgramm. 
- The dataset used in this project titled, 'titles.csv' was dowloaded from Kaggle, you can acces it via this [link](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies). The downloaded dataset is located withing my respitory labled 'downloaded-datasets' you can acces it [here](https://github.com/talia-gordy/downloaded-datasets) as well.

## 🤔 How to use this project? 

### 
1. Download both [netflix_recommendation.py](https://github.com/talia-gordy/netflix-movie-tvshow-recommendation/blob/main/netflix_recommendation.py) and [recommendation_app.py](https://github.com/talia-gordy/netflix-movie-tvshow-recommendation/blob/main/recommendation_app.py) within this respitory.
2. Open in any coding environment you like.
3. Open terminal and type the following code:

```
streamlit run recommend.py 
```
4. Program should run and open streamlit in your browser as shown:

   ![streamlit visual](https://github.com/talia-gordy/netflix-movie-tvshow-recommendation/blob/main/streamlit_visual.png)

## 👀 Want to simply view it? 

This application has been deployed via Streamlit, to acces it click on this [link](https://tgnetflix-recommendation.streamlit.app/) to view the app in your browser! 

   
## ❔Common Issues and Must Knows

###  1. In order to run the program, you must download all of the following libaries: numpy, pandas, sklearn, difflib, requests, streamlit and recommend. 

- Why? -> Google collab has all but streamlit installed, this project comes with a simple interface and in order for the model and the interface to work together, they must both be downloaded in python.
- These steps don't apply if you plan on simply viewing the program via the streamlit link.

### 2. The dataset used in this model, is for movies and shows released in 2022 and earlier.
- This project was created in Janurary 2026, the dataset despite being made in 2022 was choosen for its usabiity. 
 



