# Movie-Review-Classifier
A web app that uses Sentiment Analysis to classify inputted text (movie reviews).

![index-pg](https://user-images.githubusercontent.com/81686626/143426257-9f783a17-d81e-44be-bb08-92344138ad49.JPG)

## Web App Features
- The model predicts multiple phrases/sentences and calculates the negativity rate and positivity rate.
- The model was built with 84.06% accuracy. 

## Training & Building Features
Using LTSM/RNN, the prediction model made use of the [IMDB Dataset](https://mega.nz/file/OkUk2bDY#7B4n7j49ko159Mp3H5xM6HDaH6Wh40DvGdS9VDVykns) as its training and testing data. The texts were cleansed, converted into their respective tokens, and were inserted in an array while the phrases (sentiments) were labelled (positive or negative).

## Installation
Make sure to create a Virtual Environment within your folder/workspace. Open the terminal and run the following:

```sh
pip install -r requirements.txt
```
After installing the required dependencies and packages, just simply type in the following to run the app:

```sh
python app.py
```
Navigate to your server address in your preferred browser or click the address displayed in the terminal:

```sh
http://127.0.0.1:5000/
```