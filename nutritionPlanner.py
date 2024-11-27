from nutritionPlanner import nutrition_health, calculate_macros

def nutrition_health(age, weight, gender, height, activity, user_conditions, goals):
  
  if gender == "male":
    bmr = 10*weight + 6.25*height - 5*age + 5
  if gender == "female":
    bmr = 10*weight + 6.25*height - 5*age -161
  
  if activity.lower() == "none":
    maintenace_Cal = bmr * 1.2
  if activity.lower() == "little":
    maintenace_Cal = bmr * 1.375
  if activity.lower() == "moderate":
    maintenace_Cal = bmr * 1.55
  if activity.lower() == "very active":
    maintenace_Cal = bmr * 1.725
  if activity.lower() == "extra active":
    maintenace_Cal = bmr * 1.94
    
  if goals.lower() == "bulk":
    intake_cal = maintenace_Cal + 500
  if goals.lower() == "cut":
    intake_cal = maintenace_Cal - 500

    
  return maintenace_Cal, intake_cal


def calculate_macros(intake_cal):
  P = intake_cal/4 * 0.35
  C = intake_cal/4 * 0.4
  F = intake_cal/9 * 0.25
  
  return P,C,F




def print_dietplan_diabetes():
  return

def print_dietplan_obesity():
  return

def print_dietplan_heart_disease():
  return

def print_dietplan_anorexia():
  return

def print_dietplan_arthritis():
  return

def print_dietplan_cancer():
  return