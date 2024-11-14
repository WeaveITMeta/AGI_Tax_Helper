import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample Data for Initial Categorization
	data = [
	{"description": "Apple Subscription", "amount": -6.99, "category": "Subscriptions"},
	{"description": "Gas Station", "amount": -45.20, "category": "Fuel"},
	{"description": "Office Supplies", "amount": -89.50, "category": "Business Expense"},
	# Add more samples as needed
	]

	df = pd.DataFrame(data)

	# Text Vectorization
	tfidf = TfidfVectorizer(stop_words='english')
	X = tfidf.fit_transform(df['description'])
	y = df['category']

	# Split Data
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	# Model Training
	model = RandomForestClassifier()
	model.fit(X_train, y_train)

	# Prediction and Accuracy
	y_pred = model.predict(X_test)
	print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

	def categorize_expense(description):
		"""Categorize a new transaction based on description."""
	description_vector = tfidf.transform([description])
	category = model.predict(description_vector)[0]
	return category