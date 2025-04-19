import joblib as jb
import pandas as pd

model = jb.load("model_knnfix.pkl")

age = int(input("Your age : "))
gender = input("Your gender (male/female) : ")
study_hours_per_day = float(input("How much in hours per day you study : "))
social_media_hours = float(input("How much in hour on a day you spent scrolling sosial media : "))
netflix_hours = float(input("How much hours in a day did you spent on netflix : "))
part_time_job = input("Did you have part time job (Yes/No):")
attendance_percentage = float(input("How much your attedance percentage: "))
sleep_hours = float(input("How much hours sleep in a night: "))
diet_quality = input("How is your diet quality (Poor, Good, Fair) :")
exercise_frequency = int(input("How was your exercise frequency level (1-6): "))
parental_education_level = input("How is your parent education level (Master, Bachelor, High school, None): ")
internet_quality = input("How was your internet quality (Average, Poor, Good): ")
mental_health_rating = int(input("How was your mental health score (1 - 8) : "))
extracurricular_participation = input("Did you take extracurricular (Yes/No) : ")


new_data = [[age, gender, study_hours_per_day,social_media_hours,netflix_hours,part_time_job,attendance_percentage,sleep_hours, diet_quality, exercise_frequency, parental_education_level, internet_quality, mental_health_rating, extracurricular_participation]]


columns = ['age', 'gender', 'study_hours_per_day', 'social_media_hours',
           'netflix_hours', 'part_time_job', 'attendance_percentage', 
           'sleep_hours', 'diet_quality', 'exercise_frequency', 
           'parental_education_level', 'internet_quality', 
           'mental_health_rating', 'extracurricular_participation']

df = pd.DataFrame(new_data, columns=columns)
prediction = model.predict(df)

print (f"Your exam is {prediction[0]} ")