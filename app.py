from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Define dropdown values
industries = ['Technology', 'Healthcare', 'Education', 'Finance',
              'E-commerce', 'Real Estate', 'Travel', 'Gaming',
              'Food & Beverage', 'Logistics', 'Agriculture', 'Media']

investment_types = ['Seed Funding', 'Series A', 'Series B', 'Series C',
                    'Pre-Seed', 'Angel Investment', 'Venture Round',
                    'Private Equity', 'Debt Financing', 'Convertible Note',
                    'Crowdfunding', 'Incubation Grant']

cities = ['Bangalore', 'Mumbai', 'Delhi', 'Hyderabad', 'Chennai', 'Pune',
          'Gurgaon', 'Kolkata', 'Ahmedabad', 'Noida', 'Jaipur']

# Load model and encoders
knn_model = pickle.load(open('knn_model.pkl', 'rb'))
industry_encoder = pickle.load(open('industry_encoder.pkl', 'rb'))
investment_encoder = pickle.load(open('investment_encoder.pkl', 'rb'))
city_encoder = pickle.load(open('city_encoder.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', industries=industries,
                           investment_types=investment_types, cities=cities)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        industry = request.form['industry']
        investment_type = request.form['investment_type']
        city = request.form['city']

        # Encode input
        i = industry_encoder.transform([industry])[0]
        iv = investment_encoder.transform([investment_type])[0]
        c = city_encoder.transform([city])[0]

        input_data = np.array([[i, iv, c]])
        prediction = knn_model.predict(input_data)[0]

        return render_template('result.html', prediction=f"${prediction:,.2f}")
    except Exception as e:
        return f"❌ Prediction failed: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
