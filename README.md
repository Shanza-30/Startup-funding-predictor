This project is a machine learning-powered web application that predicts the estimated funding amount a startup may receive based on three key inputs: industry, investment type, and city. It is designed to help startup founders, investors, and analysts make informed funding estimates by leveraging historical trends and machine learning techniques.

The core of the application is a K-Nearest Neighbors (KNN) regression model, which makes predictions by analyzing similar past data points and averaging their results. To work with categorical inputs, the project uses Label Encoding to convert strings (like city or industry names) into numeric form for processing.

The machine learning model and encoders are saved using pickle and loaded during runtime for real-time predictions. The app is built using Flask, providing a clean and user-friendly interface where users can select options from dropdown menus and receive instant funding predictions.

This project illustrates the practical integration of machine learning into web development. It is ideal for those interested in applied ML, especially in the startup ecosystem, and offers a great starting point for building intelligent, data-driven web tools.
