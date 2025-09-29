# collaborative-movie-recommender
# 🎬 Collaborative Movie Recommender System

A simple **user-based collaborative filtering** movie recommender system using **cosine similarity**. This script recommends movies to a user based on the ratings of other users with similar preferences.

---

## 📌 Features

- Calculates **user-user similarity** using cosine similarity
- Builds a **user-item matrix** from movie ratings
- Generates personalized movie recommendations for a given user
- Built using Python, pandas, NumPy, and scikit-learn

---

## 🧠 How It Works

1. User ratings are transformed into a **user-item matrix**.
2. The system computes **cosine similarity** between users.
3. Based on the similarity scores, the system estimates ratings for movies the target user hasn't seen.
4. It recommends the **top N movies** with the highest predicted scores.

---

## 🛠️ Technologies Used

- Python 3
- pandas
- NumPy
- scikit-learn

---

## 📂 Project Structure


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install Dependencies

Make sure you have Python 3 and pip installed.

pip install pandas numpy scikit-learn

3. Run the Recommender
python recommender.py


You will see output like this:

Top 1 recommended movies for User 1:
movieId
104    4.818182
Name: 104, dtype: float64
