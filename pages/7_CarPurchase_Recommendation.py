import streamlit as st
import sys
import os
#from crew import Car
#from car.src.car.crew import Car
from car.src.car.utils import run_ai
from dotenv import load_dotenv
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import os

load_dotenv()


def main():
    st.set_page_config(page_title='AI Car Purchase Recommendation Engine',page_icon="🚗")
    st.title='🚗 AI-Powered Car Purchase Recommendation Engine'

    st.markdown("""
Welcome to your intelligent car buying assistant.
                
                Based on your financial profile ,lifestyle, and preferences,our we recommend the best vehicles for you by analyzing:

                💰 Affodability & Loan Eligibility
                📊 Buyer Trends & Market Insights
                🛠️ Reliability & Repair History
                🛡️ Insurance Cost Factors
                 🚘New vs Used Car Value Comparison
                
                Fill in your deatils below to get started.
                
""")
    with st.sidebar:
        st.header('Buyer Profile')
        col1,col2 = st.columns(2)

        with col1:
            name = st.text_input('👤 Full Name')
            age = st.number_input('🎂Age',min_value=18,max_value=80,step=1)
            gender = st.selectbox('⚧ Gender',['Male','Female','Prefer not to say'])
            country = st.text_input('🌍 Country',placeholder='Kenya')

            annual_salary = st.number_input('💼Annual Salary ($)',min_value=0.0,step=1000.00)
            credit_card_debt = st.number_input('💳Credit Card Debt ($)', min_value=0.0, step=500.0)
            net_worth = st.number_input('🏦Net Worth ($)', min_value=0.0, step=5000.0)

        with col2:
            cibil_score = st.number_input('📊 Credit Score',min_value=300,max_value=900,step=1)
            dependents = st.number_input('👨‍👩‍👧Number of Dependents',min_value=0,step=1)
            employment_status = st.selectbox('🧑‍💼Employment Type',['Employed','Self-Employed','Business Owner'])

            loan_term = st.selectbox('🏦Preferred Loan Term (Years)',[1,3,5,7])
            budget = st.number_input('💰Budget for Car ($)',min_value=0.0, step=1000.0)
            car_condition = st.selectbox('🚘Car Condition Preference',['New','Used','Either'])

        st.header('Vehicle Preferences')

        col3, col4 = st.columns(2)

        with col3:
            transmission = st.selectbox('⚙️ Transmission Type',['Automatic','Manual','Any'])
            fuel_type = st.selectbox('⛽Fuel Type',['Petrol','Diesel','Hybrid','Electric','Any'])
            body_type = st.selectbox('🚙Body Type',['Sedan','SUV','Hatchback','Truck','Coupe','Any'])
            seats = st.number_input('🪑 Minimum Number of seats',min_value=2,max_value=10,step=1)

        with col4:
            usage = st.selectbox('🛣️Primary Usage',['Personal','Family','Business','Commercial'])
            mileage_preference = st.selectbox('📉Mileage Preference',['Low Mileage','Moderate','No Preference'])
            insurance_sensitivity = st.selectbox('🛡️Insurance Cost Sensitivity',['Low Premium Preferred','Not a Concern'])
            reliability_priority = st.selectbox('🛠️Reliability Importance',['Very Important','Moderate','Not a Priority'])
        
    if st.button('🔍 Generate Car Recommendation'):
        required_fields = [
            name,age,gender,country,annual_salary,net_worth,cibil_score,budget,transmission,fuel_type
        ]

        if not all(required_fields):
            st.error('Please fill in all required fileds to generate recommendation')
        else:
            inputs = {
                'name':name,
                'age':age,
                'gender':gender,
                'annual_salary':annual_salary,
                'credit_card_debt':credit_card_debt,
                'net_worth':net_worth,
                'credit_score':cibil_score,
                'dependents':dependents,
                'employment_status':employment_status,
                'loan_term':loan_term,
                'budget':budget,
                'car_condition':car_condition,
                'transmission':transmission,
                'fuel_type':fuel_type,
                'body_type':body_type,
                'seats':seats,
                'usage':usage,
                'mileage_preference':mileage_preference,
                'insurance_sensitivity':insurance_sensitivity,
                'reliability_priority':reliability_priority
            }

            with st.spinner('Analyzing financial profile, market trends,insurance risk and repair history...'):
                try:
                    # my_crew_instance = Car()
                    # crew_instance = my_crew_instance.crew()
                    # crew_result = crew_instance.kickoff(inputs={'inputs':inputs})

                    crew_result = run_ai(inputs)

                    st.subheader('🚘 Your Personalized Car Recommendations')
                    st.markdown(crew_result)

                    st.write('---')
                    st.header('📊 Detailed Analysis Reports')

                    files = [
                        'affordability_analysis.md',
                        'car_market.md',
                        'loan_eligibility.md',
                        'market_trends.md',
                        'insurance_estimate.md',
                        'reliability_report.md',
                        'final_recommendations.md'
                    ]

                    combined_content = ""

                    for file in files:
                        try:
                            with open(file,'r') as f:
                                content = f.read()
                                st.subheader(file.replace(".md","").replace("_"," ").title())
                                st.markdown(content)
                                combined_content += content + "\n\n"
                        except FileNotFoundError:
                            st.warning(f"{file} not found.")
                        except Exception as e:
                            st.error(f"Error reading {file}: {e}")

                    if combined_content:
                        st.download_button(
                            label='📥 Download Full Recommendation Report',
                            data=combined_content,
                            file_name='car_recommendation_report.md',
                            mime='text/markdown'
                        )
                except Exception as e:
                    st.error(f"An unexpected error occured: {e}")


if __name__=='__main__':
    main()