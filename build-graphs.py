import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Імена сайтів
sites = [f"site{i+1}" for i in range(12)]

# Критерії
criteria = [
    "daily_users",
    "daily_purchases",
    "average_session_duration",
    "conversion_rate",
    "returning_customers",
    "customer_lifetime_value",
    "page_load_time",
    "bounce_rate",
    "cart_abandonment_rate",
    "customer_satisfaction",
    "unique_visitors",
    "seo_score",
    "mobile_friendly_score",
    "ad_revenue",
    "email_subscription_rate",
    "social_media_shares",
]

# Ваги критеріїв
weights = [
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.05,
    0.05,
    0.05,
    0.05,
    0.05,
    0.05,
    0.05,
    0.05,
    0.05,
    0.05,
]

# Максимізовані критерії (1-6)
maximized_criteria = criteria[:6]

# Мінімізовані критерії (7-16)
minimized_criteria = criteria[6:]

# Генерація випадкових даних для кожного сайту
data = {"site": sites}

# Заповнення даних
for criterion in criteria:
    if criterion in maximized_criteria:
        data[criterion] = np.random.randint(
            50, 100, size=len(sites)
        )  # Випадкові значення для максимізації
    else:
        data[criterion] = np.random.randint(
            1, 50, size=len(sites)
        )  # Випадкові значення для мінімізації

# Створення DataFrame
df = pd.DataFrame(data)


# Функція для нормалізації та обчислення оцінки
def calculate_scores(data, weights):
    for col in maximized_criteria:
        data[col] = (
            data[col] / data[col].max()
        )  # Нормалізація до 1 (максимізовані критерії)
    for col in minimized_criteria:
        data[col] = (
            data[col].min() / data[col]
        )  # Нормалізація до 1 (мінімізовані критерії)
    data["total_score"] = (data[maximized_criteria + minimized_criteria] * weights).sum(
        axis=1
    )
    return data


# Обчислення оцінок
scores = calculate_scores(df, weights)

# Виведення результатів
print(scores[["site", "total_score"]])

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.bar(scores["site"], scores["total_score"], color="skyblue")
plt.xlabel("Сайти")
plt.ylabel("Загальна оцінка")
plt.title("Рейтинг ефективності сайтів")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(
    scores["site"], scores["total_score"], marker="o", linestyle="-", color="skyblue"
)
plt.xlabel("Сайти")
plt.ylabel("Загальна оцінка")
plt.title("Рейтинг ефективності сайтів")
plt.show()
