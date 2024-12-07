import pandas as pd
import numpy as np

# Імена сайтів
sites = [f"site{i+1}" for i in range(12)]

# Критерії
criteria = [
    "daily_users",
    "daily_purchases",
    "page_load_time",
    "bounce_rate",
    "average_session_duration",
    "conversion_rate",
    "cart_abandonment_rate",
    "customer_satisfaction",
    "returning_customers",
    "unique_visitors",
    "seo_score",
    "mobile_friendly_score",
    "ad_revenue",
    "email_subscription_rate",
    "social_media_shares",
    "customer_lifetime_value",
]

# Максимізовані критерії (1-6)
maximized_criteria = criteria[:6]

# Мінімізовані критерії (7-16)
minimized_criteria = criteria[6:]

# Генерація випадкових даних для кожного сайту (12 сайтів)
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

# Запис у CSV файл
df.to_csv("ecommerce_sites.csv", index=False)

print("CSV файл успішно створено та заповнено даними!")
