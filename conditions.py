class DefiningCondition:
    anorexia = False
    diabetes = False
    heart_disease = False
    cancer = False
    arthritis = False

    def has_anorexia(self):
        print("Anorexia is an eating disorder characterized by an extreme fear of gaining weight, often leading to self-starvation and excessive weight loss.")
        print("Lifestyle and Dietary Changes:")
        print("- Focus on eating balanced meals with proper nutritional intake.")
        print("- Work with a mental health professional to address underlying psychological issues.")
        print("- Gradually reintroduce healthy foods and a positive relationship with food.")
        print("- Regular exercise can help improve body image and overall health, but avoid excessive or extreme exercises.")
        print("Consult a healthcare provider to create a personalized nutrition plan to regain healthy weight.")
        self.anorexia = True

    def has_diabetes(self):
        print("Diabetes is a condition that affects how the body processes blood sugar (glucose). Type 1 is usually inherited, while Type 2 is related to lifestyle factors.")
        print("Lifestyle and Dietary Changes:")
        print("- Regularly monitor your blood sugar levels.")
        print("- Maintain a healthy diet, focusing on low-glycemic foods (whole grains, vegetables, lean proteins).")
        print("- Regular exercise helps regulate blood sugar levels and improve insulin sensitivity.")
        print("- Avoid sugary drinks and foods with refined carbohydrates.")
        print("Consult a healthcare provider to develop a personalized meal plan and exercise routine tailored to your needs.")
        self.diabetes = True

    def has_heart_disease(self):
        print("Heart disease refers to various types of conditions affecting the heart, including coronary artery disease, heart attacks, and heart failure.")
        print("Lifestyle and Dietary Changes:")
        print("- Engage in regular physical activity such as walking, swimming, or cycling.")
        print("- Adopt a heart-healthy diet rich in fruits, vegetables, whole grains, and lean proteins.")
        print("- Reduce the intake of saturated fats, trans fats, and processed foods.")
        print("- Avoid smoking and excessive alcohol consumption.")
        print("- Manage stress and get enough sleep.")
        print("Consult a cardiologist for tailored advice on physical activity and dietary changes.")
        self.heart_disease = True

    def has_cancer(self):
        print("Cancer is a group of diseases involving abnormal cell growth with the potential to spread to other parts of the body.")
        print("Lifestyle and Dietary Changes:")
        print("- Eating a well-balanced diet, rich in antioxidants, fruits, and vegetables may help support overall health.")
        print("- Stay physically active and maintain a healthy weight.")
        print("- Avoid smoking and limit alcohol consumption, both of which are known risk factors for many cancers.")
        print("- Regular check-ups and screenings (as recommended by your doctor) can help detect cancer early.")
        print("Consult with an oncologist for guidance on specific treatments, physical activity, and diet based on your type of cancer.")
        self.cancer = True

    def has_arthritis(self):
        print("Arthritis is inflammation of one or more joints, causing pain and stiffness. The two main types are osteoarthritis and rheumatoid arthritis.")
        print("Lifestyle and Dietary Changes:")
        print("- Regular low-impact exercise such as walking, swimming, or cycling to maintain joint function and reduce stiffness.")
        print("- Maintain a healthy weight to reduce strain on joints, especially weight-bearing joints like the knees.")
        print("- A diet rich in omega-3 fatty acids, antioxidants, and anti-inflammatory foods may help reduce joint pain and swelling.")
        print("- Consider working with a physical therapist to develop exercises that improve flexibility and strength.")
        print("Consult with a rheumatologist for specific treatment plans, including medications and physical therapy.")
        self.arthritis = True
        

def handle_conditions(user_conditions):
    for condition in user_conditions:
        if condition == 'anorexia':
           return DefiningCondition().has_anorexia()
        elif condition == 'diabetes':
            return DefiningCondition().has_diabetes()
        elif condition == 'heart disease':
            return DefiningCondition().has_heart_disease()
        elif condition == 'cancer':
            return DefiningCondition().has_cancer()
        elif condition == 'arthritis':
            return DefiningCondition().has_arthritis()
        else:
            print(f"No information available for {condition}.")