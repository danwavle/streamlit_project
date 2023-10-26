import streamlit as st
from streamlit import session_state as ss

if 'running' not in ss:
    ss['running'] = False
    
if 'answered' not in ss:
    ss['answered'] = False
    
if 'factors' not in ss:
    ss['factors'] = []
    
if 'output' not in ss:
    ss['output'] = []
    
if 'number' not in ss:
    ss['number'] = None
    
def run_switch():
    if ss.running:
        ss.running = False
    else:
        ss.running = True
    
def prompt():
    st.write("Please type an integer, and I will tell you if it is prime.")
    st.write("If the integer is not prime, I will list its positive factors for you.")
    st.write("Enter 'q' to end the program:")
    st.text_input("Type your integer here:",key='num_input',on_change=answered)
    
def answered():
    ss.answered = True
    ss.number = ss['num_input']
    if ss.num_input == 'q':
        reset()
    
    
def num_check():
    try:
        ss.number = int(ss.num_input)
        return True
    except:
        return False

def quit_check():
    if ss.num_input == 'q':
        return True
    else:
        return False
    
def prime_check():
    # checks if number is prime. Assumes number is greater than 2 or less than -2
    # If not prime, appends unique factors to ss.factors list
    ss.factors = []
    prime = True
    if ss.number < 0:
        ss.number *= -1
    for x in range(2,ss.number):
        if ss.number%x == 0 and int(ss.number/x) not in ss.factors:
            prime = False
            ss.factors.append(x)
    return prime
    
def reset():
    ss.output = []
    ss.factors = []
    ss.running = False
    ss.answered = False
    
def main():
    st.title("Mr. Wavle's Factor Program")
    if not ss['running']:
        st.button("Begin Program",on_click=run_switch)
    else:
        prompt()
        if ss.answered:
            if not num_check():
                st.write("You did not type an integer. Try again.")
            elif ss.number == 1 or ss.number == -1:
                st.write("1 is not a prime number and has no factors")
            elif prime_check():
                st.write(f"{ss.number} is a prime number")
            else:
                st.write(f"{ss.number} is a not prime number")
                for factor in ss.factors:
                    st.write(f"{factor} and {int(ss.number/factor)} are factors of {ss.number}")
            
        
if __name__ =='__main__':
    main()

