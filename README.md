# 🎬 Predicting OTT Content Fatigue

### *A Data-Driven Subscription Retention Strategy*

> **Mini Project | Data Mining and Business Intelligence (DMBI)**
> **Tools Used:** Python 🐍 · RapidMiner ⚙️ · Power BI 📊

---

## 🚀 Project Overview

This project focuses on predicting **content fatigue** among OTT users — the gradual decline in user engagement that often precedes subscription cancellations.

By leveraging **K-Means Clustering** and **Decision Tree Modeling**, we uncover behavioral patterns, identify high-risk users, and provide actionable **business intelligence** to improve retention strategies.

---

## 🎯 Objective

To shift from **reactive churn management** to **proactive risk prediction** by identifying early signs of user disengagement and enabling targeted interventions.

---

## 🧠 Project Workflow

### 🔹 1. Data Source

* OTT user dataset containing **100,000+ ratings**.
* Features include user ratings, number of movies rated, and engagement behavior.

### 🔹 2. Feature Engineering (via RapidMiner)

* Extracted and normalized key metrics:

  * **Average Rating (Satisfaction)** 🎞️
  * **Total Movies Rated (Activity)** 🎬
  * **Standard Deviation of Ratings (Consistency)** 📈
* Applied **Z-score normalization** for consistent scaling.

### 🔹 3. Modeling (via Python)

* **K-Means Clustering** (K=4) to segment users into behavioral groups:

  1. Happy Regulars 😄
  2. Volatile Viewers ⚠️
  3. Casual Majority 🙂
  4. Dormant Users 💤
* **Decision Tree Classifier** for predicting high/low future activity.

📊 **Model Accuracy:** `61.20%`
💡 **Key Insight:** Predictable (consistent) users are loyal users.

### 🔹 4. Business Intelligence Dashboard (via Power BI)

* Interactive dashboard for:

  * Predictive alerts ⚡
  * Segmentation reports 📑
  * Retention performance metrics 📉

---

## 🔍 Key Insights

* **Volatile Viewers** and **Dormant Users** show the highest risk of churn.
* **Rating Consistency** emerged as the strongest predictor of loyalty.
* Retaining users is **5x cheaper** than acquiring new ones.

---

## 💡 Strategic Recommendations

1. **Proactive Alerting:**
   Flag users matching the Volatile Viewer profile for personalized recommendations.
2. **Incentivize Consistency:**
   Reward structured feedback to promote stable viewing patterns.
3. **Optimize Acquisition:**
   Target marketing channels yielding “Happy Regular” type users.

---

## 📈 Results & Impact

| Metric             | Value              | Description                             |
| :----------------- | :----------------- | :-------------------------------------- |
| **Model Accuracy** | 61.20%             | Decision Tree performance               |
| **Retention ROI**  | 5×                 | Savings from retention over acquisition |
| **Key Insight**    | Rating Consistency | Strongest predictor of loyalty          |

---

## 🧩 Tech Stack

| Category                                | Tools Used                           |
| :-------------------------------------- | :----------------------------------- |
| **Data Cleaning & Feature Engineering** | RapidMiner                           |
| **Modeling & Analysis**                 | Python (pandas, sklearn, matplotlib) |
| **Visualization & BI**                  | Power BI                             |
| **Dataset**                             | OTT Usage Dataset                    |

---

## 🏆 Project Value Delivered

* Moved from **reactive churn management** to **proactive risk detection**.
* Provided management with **data-driven intelligence dashboards**.
* Built a framework that supports **scalable subscription retention strategies**.

---

## 📚 Authors

👤 **Siddharth Jogi**
🎓 IT Student @ VESIT, Chembur

---

## 🌟 Preview

📊 *BI Dashboard Snapshot*
📈 *Cluster Segmentation Plot*
🧩 *Decision Tree Visualization*

---

## 🏁 Conclusion

This mini-project demonstrates how **machine learning + BI tools** can work together to generate actionable insights in the OTT industry — helping platforms **understand users, prevent churn, and enhance loyalty**.

