# 🚀 Startup Funding Prediction using Machine Learning

This project is a **machine learning–powered web application** that predicts the **estimated funding amount** a startup may receive based on three key factors: **industry**, **investment type**, and **city**. It is designed to support **startup founders, investors, and analysts** in making data-driven funding estimates by leveraging historical startup funding trends.


## 🎯 Project Objective

The goal of this project is to demonstrate how **machine learning models** can be effectively integrated into **real-world web applications** to generate meaningful business insights. By analyzing patterns from past funding data, the system provides quick and approximate funding predictions for new startups.


## 🧠 Machine Learning Approach

* The core prediction engine uses a **K-Nearest Neighbors (KNN) Regression model**.
* KNN predicts funding amounts by identifying startups with similar characteristics in historical data and averaging their funding values.
* This approach works well for capturing localized patterns and similarities within the startup ecosystem.


## 🔢 Feature Engineering & Encoding

Since the input features are categorical in nature, the following preprocessing steps are applied:

* **Label Encoding** is used to convert categories such as **industry**, **investment type**, and **city** into numerical representations.
* Encoders are saved to ensure consistency between training and real-time predictions.


## 💾 Model Persistence

* The trained KNN model and label encoders are saved using **pickle**.
* During runtime, these saved files are loaded to enable **fast, real-time predictions** without retraining the model.


## 🌐 Web Application (Flask)

The application is built using **Flask**, providing a clean and intuitive user interface:

* Dropdown menus for selecting **industry**, **investment type**, and **city**
* One-click prediction of estimated funding amount
* Instant results displayed on the same page

This makes the application lightweight, interactive, and easy to deploy.


## 🛠️ Tools & Technologies

* Python
* Pandas & NumPy
* scikit-learn
* KNN Regression
* Flask
* Pickle
* HTML & CSS


## 🔮 Future Enhancements

 📈 Add numerical features such as **startup age**, **team size**, or **revenue**
🤖 Experiment with advanced models like **Random Forest, XGBoost, or Linear Regression**
 📊 Display prediction confidence or range estimates
 🌐 Deploy the app on cloud platforms (Render, Heroku)
 📁 Enable bulk predictions using CSV upload


## 📌 Conclusion

This project highlights the **practical application of machine learning in the startup ecosystem**, showcasing how predictive models can be combined with web technologies to build intelligent, data-driven tools. It serves as an excellent project for learning **applied ML, regression modeling, and ML deployment using Flask**.
