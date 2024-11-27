from flask import Flask, render_template, request
from nutritionPlanner import nutrition_health, calculate_macros

app = Flask(__name__)

class DefiningCondition:
    anorexia = False
    diabetes = False
    heart_disease = False
    cancer = False
    arthritis = False

    def has_anorexia(self):
        print("Anorexia is an eating disorder characterized by an extreme fear of gaining weight...")
        self.anorexia = True

    def has_diabetes(self):
        print("Diabetes is a condition that affects how the body processes blood sugar...")
        self.diabetes = True

    def has_heart_disease(self):
        print("Heart disease refers to various types of conditions affecting the heart...")
        self.heart_disease = True

    def has_cancer(self):
        print("Cancer is a group of diseases involving abnormal cell growth...")
        self.cancer = True

    def has_arthritis(self):
        print("Arthritis is inflammation of one or more joints, causing pain and stiffness...")
        self.arthritis = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        age = int(request.form['age'])
        weight = int(request.form['weight'])
        gender = request.form['gender']
        height = float(request.form['height'])
        activity = request.form['activity']
        user_conditions = request.form.getlist('conditions')
        gym_goals = request.form['goals']

        # Call nutrition and macro calculation functions
        maintenace_Cal, intake_cal = nutrition_health(age, weight, gender, height, activity, user_conditions, gym_goals)
        P, C, F = calculate_macros(intake_cal)

        # Handle conditions directly here
        condition_handler = DefiningCondition()
        for condition in user_conditions:
            if condition == 'anorexia':
                condition_handler.has_anorexia()
            elif condition == 'diabetes':
                condition_handler.has_diabetes()
            elif condition == 'heart disease':
                condition_handler.has_heart_disease()
            elif condition == 'cancer':
                condition_handler.has_cancer()
            elif condition == 'arthritis':
                condition_handler.has_arthritis()
            else:
                print(f"No information available for {condition}.")

        # Return the results to the HTML page
        return render_template('index.html', maintenace_Cal=maintenace_Cal, intake_cal=intake_cal, P=P, C=C, F=F)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
