# Project-3 Rescue Dog Outcomes

## Table of contents
* [Motivation](##Motivation)
* [Topic](##Topic)
* [Outcome](##Outcome)
* [Technologies](##Technologies)
* [Setup](##Setup)
* [Methodology](##Methodology)
* [Project_Status](##Project_Status)
* [Credits](##Credits)

## Motivation 
This is a group project for the University Of Oregon Data Analytics Bootcamp. The animal rescue community is always trying to find ways to advocate for their animals. This project attempts to develop a Machine Learning algorithm that rescue shelters may use as a part of the decision making process at intake. 

## Topic
The question we hope to be able to answer: 
<br>
&nbsp; &nbsp; &nbsp; _Can our Machine Learning model help a rescue shelter assess a dog's adoptability? Should the shelter take in the dog or not?_

## Outcome
This project group achieved the following:
1. Developed a Machine Learning model to help predict a dog's adoptability outcome at intake based on 6 features (Breed, Color, Sex, Age, Behavior, Pure vs Mix). This tool will hopefully help rescue shelters decided whether or not to accept/deny a dog based on those 6 features. 
2. Developed a website to link a user intake form (Prediction Form) to a Flask app that uses a ML model to predict an outcome based on the user's new input.  
3. Created basic charts that visualizes the Louisville dataset after data munging.

## Technologies
The project is created with:
* Python===3.6
* Bootstrap===4.3.1
* Flask==1.1.1
* jupyter-client==5.3.4
* jupyter-core==4.6.1
* jupyterlab==1.2.5
* jupyterlab-server==1.0.6
* pandas==1.0.0
* scikit-learn==0.23.1
* Keras==2.3.0
* Tableau Public==2020.2

## Setup
1. Jupyter Notebook installation: (https://jupyter.org/install)
2. Pandas installation: pip install pandas or conda install pandas
3. Scikit-learn installation: (https://scikit-learn.org/stable/install.html)
4. Tableau Public installation: (https://public.tableau.com/en-us/s/download)

## Methodology
1.  Data gathering    
    * We were able to find a dataset to test our predictive models from the Department of Animal Services Louisville Kentucky (https://data.louisvilleky.gov/dataset/animal-service-intake-and-outcome).  This dataset is unique.  It was the only free dataset we could find with dog behavior information.
    * Finding a data source with sufficient data proved to be a difficult task. There is not a standard set for recues to track intake and outake data. 

2. Data munging
    * Find the original csv file (example: Animal_Shelter_Louisville.csv) and cleaned csv file (example: LouisvilleCleanFinal.csv) in Resources folder. 
    * All of the data cleaning was completed via pandas.
    * To review detailed logic for creating/organzing ML model features, run jupyter notebook file
    (Final_DataCleaning.ipynb):
    * 
    * ![jupyter_notebook](/images/jupyterNotebookDataCleaning.PNG "jupyter_notebook").  

3. Creating Flask App
    * Flask App converts the user input via a form using Python's post method and leveraging flask libraries.  That user input gets changed into a 52 digit binary code (to match OneHot Encoding format) which then gets passed into a random forest model.
    * To activate the Flask App (under webpage), in the terminal, execute the comand 'python app.py' and this will then launch the API and return the predicted outcome into the result.html.

5. Creating charts using Tableau Public
    * To share Tableau charts on the website, we simply copied the embed code into a chart.html page. 
    * 
    * ![Tableau_Public](/images/TableauTopBreedChart.PNG "Tableau_Public")

6. Designing the look of the website
    * Bootstrap powerful and interactive tool (https://www.layoutit.com/build) were used to build the bones of the html.
    * CSS and Bootstrap built in tools were used to create the simple and clean design of the websites. 
    * Please review the website after launching the Flask app (using localhost:5000).  Otherwise, the style attributes will not be activated.
    * Need to credit Karl Unverfeth for solely creating the layout/look out the webpage.

7. Creating ML model
    * Several models (Random Forest, Logistic Regression, SVM, NN) were created each time a feature was organized/cleaned or created.  Accuracy scores were tracked for each model to see how it performed.
    * To review results of each model, see Results.xlsx in Resources folder.
    * For the final project, we chose to use the Random Forest model to predict the outcome of the dog. Due to time constraints, we wanted to take a deeper dive to learn more about the evaluation tools within Random Forest method. To review the logic/tools of the Random Forest model method, run jupyter notebook file (Final_RFModel.ipynb):
    * 
    * ![jupyter_notebook](/images/jupyterNotebook_RF_Model.PNG "jupyter_notebook")  

## Project_Status
* Future Updates for Project 3:
1.  Take a deeper dive into SVM amd NN models.
2.  Create an intake form that continues to collect data and stores it in a database. The goal is to make it a system for rescues to track their own shelter's data and feed that data into the model to make the model stronger.
3.  Create another ML model to predict how long a dog would stay in the shelter.

## Credits
* @KellyPriest - Subject matter expert, Data munging 
* @KarlUnverfeth - Webpage layout and design, Data munging
* @SpencerLaFarge - ML model, Data munging
* @AngieOng - Data munging, ML model, Flask app, Html form

























