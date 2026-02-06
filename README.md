# SPAM-DETECTION
This is a simple and practical SMS Spam Detection web application built using Machine Learning and Flask.
The goal of this project is to automatically identify whether a message is Spam or Not Spam (Ham) in real time.
The model is trained once using real-world SMS data and then reused for predictions, making the application fast and efficient.

1. Why This Project?
Spam messages are something we all deal with promotions, fake offers, and suspicious links.
This project shows how machine learning can be used to solve this everyday problem by analyzing the text of a message and predicting whether it’s spam or not.

2. How It Works
  -You type an SMS message into the web interface.
  -The message is sent to the backend using a POST request.
  -The text is converted into numerical form using TF-IDF.
  -A Naive Bayes model analyzes the text.
  -The app instantly tells you whether the message is spam or safe.
  -All of this happens in just a fraction of a second.

3. Dataset Used
Dataset: SMS Spam Collection Dataset
Source: UCI Machine Learning Repository
Messages: 5,574 real SMS messages
Labels: 0 → Ham (Not Spam), 1 → Spam

4. Running the Project Locally
  i. Install dependencies: pip install -r requirements.txt
  ii. Train the model: python train_model.py
  iii. Start the Flask app: python app.py
  iv. Open your browser and visit: http://127.0.0.1:5000/

5. Deployment
  -This application is deployed using Render.
  -The trained model is loaded when the server starts.
  -No retraining is required during deployment.
  -The app is production-ready using Gunicorn.

6. Features
  -Real-time spam detection
  -Clean and simple user interface
  -Character counter for input text
  -Handles multiple requests without refreshing
  -Lightweight and fast predictions
