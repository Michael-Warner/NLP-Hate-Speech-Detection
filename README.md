# Hate Speech Detection App

## Purpose:
The purpose of the project was to develop and deploy a live service app where a person would be able to check if something written was hate speech, offensive speech or neither.

![hate speech](https://media.wired.com/photos/5ba2d81dbc9a294fa13c6198/2:1/w_2400,h_1200,c_limit/hate%20speech%20algorithm.jpg)   

For a summary of this project please check out the powerpoint [here](https://drive.google.com/file/d/1Hu2-sBuX_hv26S0p7lo9mtt5IeB5_FUN/view?usp=sharing).   

View the Web APP [here](https://hate-speech-detection-tbs.herokuapp.com).

## Dataset:
There were three datasets used to train the model. The base dataset was from [Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber(2017)](https://data.world/thomasrdavidson/hate-speech-and-offensive-language). The second dataset was from [Jing Qian, Anna Bethke, Yinyin Liu, Elizabeth Belding, William Yang Wang(2019)](https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech). The last dataset was from [Kaggle](https://www.kaggle.com/dv1453/twitter-sentiment-analysis-analytics-vidya?select=train_E6oV3lV.csv) provided by [Analytics Vidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-twitter-sentiment-analysis/#LeaderBoard).

The original dataset, from Davidson et al., had labeled each tweet in one of three ways, hate speech, offensive speech or neither. The other two datasets were labelled only as hate speech or not hate speech. The reason for adding the other two datasets was because the original dataset was unbalanced.
![unbalanced dataset](/Images/unbalanced_dataset.png)
After adding the other two datasets it became more balanced, which helped correctly train the models.

## Method:
The methodology used in this project was an EDA on the tweets, cleaning of the datasets, creation of the online app, creation of the models and then the testing of the app.

## Result:
After trying multiple models, Random Forest, Naive Bayes, Logistic Regression, Support Vector Machine (SVM) and a Neural Network, the best result was from the SVM model with an TF-IDF Vectorization. It had an F1 score of 0.89 and a Recall score of 0.897.
![Confusion Matrix_SVM](/webapp/visualization/svm_model.png) 

Recall was chosen as the benchmark as it was more important to get as many potential hate or offense tweets as possible.  

The results of all the models are seen here.
![Model result](/Images/model_result.png)

The results from the [Neural Network](https://colab.research.google.com/drive/1Bd0-Mg-XdyyzLHc9j6rIYKy6tSDALUhY?usp=sharing).

## Conclusion:
A larger dataset would make the model more effective but the debate of what is considered hate speech, offensive or neither is very subjective and changes per person. This makes it difficult to label datasets correctly.

## Appendix 
There are 4 pages of the application : Classification of the Tweets/Sentences, Business Problem, Exploratory Data Analysis and our model deployed. 
### Screenshots of the APP :
![App Screenshot 1](/Images/app_screenshot_1.png)
![App Screenshot 2](/Images/app_screenshot_2.png)
![App Screenshot 3](/Images/app_screenshot_3.png)
![App Screenshot 4](/Images/app_screenshot_4.png)

## Build on :
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Heroku](https://www.heroku.com)  

## Acknowledgements :


[Davidson, T., D. Warmsley, et al. (2017). "Automated Hate Speech Detection and the Problem of Offensive Language.](https://www.researchgate.net/publication/314942659_Automated_Hate_Speech_Detection_and_the_Problem_of_Offensive_Language)  
For Dataset of this paper : https://data.world/thomasrdavidson/hate-speech-and-offensive-language 
	
[Qian, J., A. Bethke, et al. (2019). A Benchmark Dataset for Learning to Intervene in Online Hate Speech.](https://www.researchgate.net/publication/336997246_A_Benchmark_Dataset_for_Learning_to_Intervene_in_Online_Hate_Speech)  
For Dataset of this paper : https://github.com/jing-qian/A-Benchmark-Dataset-for-Learning-to-Intervene-in-Online-Hate-Speech
	
[Analytics Vidhya](https://datahack.analyticsvidhya.com/contest/practice-problem-twitter-sentiment-analysis/#LeaderBoard)  
For Dataset of this Hackathon : https://www.kaggle.com/dv1453/twitter-sentiment-analysis-analytics-vidya?select=train_E6oV3lV.csv 

