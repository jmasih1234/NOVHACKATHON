from nutritionPlanner import ( nutriton_health, calculate_macros)


health_conditions = ['Anorexia', 'Diabetes', 'Obesity', 'Heart Disease', 'Cancer', 'Arthritis']
goals = ["bulking", "cutting", "maintaining"]

class main:
  
  age = int(input("What is your age?: ")) # If have time, error handle these
  weight = int(input("What is your weight in Kilograms?: "))
  gender = input("What is your gender?: ")
  height = float(input("What is your height in cm?: "))
  activity = input("What is your activity level?:\n ‣None \n ‣Little \n ‣Moderate(3-5 Days/Week) \n ‣Very Active(5-6 Days/Week) \n ‣Extra Active(Very Active & Physical Job) \n")
  
  user_conditions = []
  
  print(health_conditions,"\n")
  while True:
    condition = input("Do you have any of the following conditions:\n Type 'done' when no conditions left to enter: \n")
    if condition.lower() != 'done':  
        user_conditions.append(condition)
    else:
        break
    # account for users entering other condition
  
  print(goals, "\n")
  gym_goals = ""
  while gym_goals not in goals:
    gym_goals= input("From the following, what are your gym goals? (Lowercase only)\n")
    
    
  maintenace_Cal, intake_cal = nutriton_health(age, weight, gender, height, activity, user_conditions, goals)
  P,C,F = calculate_macros()


  print ("Your maintance calories is:\n",maintenace_Cal,"\nYour intake calories based on your goals are:\n",intake_cal)
  print ("Your macro intake is:\n","F:",F,"\nC:",C,"\nF:",F)
