import tkinter as tk
from tkinter import messagebox

# testing PR 
# Function to perform the analysis
def perform_analysis():
    try:
        score = 0

        # Get values from the fields
        user_name = entry_name.get()
        user_monthly_income = float(entry_income.get())
        user_net_worth = float(entry_net_worth.get())
        user_debt = float(entry_debt.get())
        user_amount_needed = float(entry_amount_needed.get())

        # Monthly Income Analysis
        if user_monthly_income <= 1800:
            score += 1
        elif user_monthly_income > 1800 and user_monthly_income <= 3500:
            score += 2
        else:
            score += 3

        # Net Worth Analysis
        if user_net_worth <= user_monthly_income * 0.5:
            score = score
        elif user_net_worth > user_monthly_income * 0.5 and user_net_worth <= user_monthly_income * 1.5:
            score += 1
        elif user_net_worth > user_monthly_income * 1.5 and user_net_worth <= user_monthly_income * 2.5:
            score += 2
        else: 
            score += 3

        # Debt Analysis
        if user_debt > user_net_worth * 2:
            score += 0
        elif user_debt <= user_net_worth * 2 and user_debt > user_net_worth:
            score += 1
        elif user_debt <= user_net_worth and user_debt > user_net_worth * 0.5:
            score += 2
        else:
            score += 3

        # Amount Requested Analysis
        if user_amount_needed > (user_net_worth + user_debt) * 2:
            score += -1
        elif user_amount_needed > user_net_worth + user_debt and user_amount_needed <= (user_net_worth + user_debt) * 2:
            score += 0
        elif user_amount_needed == user_net_worth or user_monthly_income == user_debt:
            score += 1
        elif user_amount_needed <= (user_net_worth + user_debt) and user_amount_needed > (user_net_worth + user_debt) * 0.5:
            score += 2
        else:
            score += 3

        # Display the analysis result
        if score >= 10:
            result = "Low Risk"
        elif score <= 6 and score < 10:
            result = "Moderate Risk"
        else:
            result = "High Risk"
        
        result_label.config(text=f"Analysis Result: {result} (Score: {score})")
        new_analysis_button.grid(row=7, column=0, columnspan=2, pady=20)  # Change here: move the button to row 7
    
    except ValueError:
        messagebox.showerror("Error", "Please fill in all fields correctly.")

# Function to restart the application
def new_analysis():
    entry_name.delete(0, tk.END)
    entry_income.delete(0, tk.END)
    entry_net_worth.delete(0, tk.END)
    entry_debt.delete(0, tk.END)
    entry_amount_needed.delete(0, tk.END)
    result_label.config(text="")
    new_analysis_button.grid_forget()

# Create the main window
root = tk.Tk()
root.title("Credit Analysis")
root.geometry("500x600")
root.config(bg="#f5f5f5")

# Set a default font
font = ("Arial", 12)

# Titles and Labels
title = tk.Label(root, text="Welcome to the Bank!", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333333")
title.grid(row=0, column=0, columnspan=2, pady=20)

label_name = tk.Label(root, text="Name", font=font, bg="#f5f5f5", fg="#555555")
label_name.grid(row=1, column=0, padx=20, pady=10, sticky="w")

label_income = tk.Label(root, text="Monthly Income", font=font, bg="#f5f5f5", fg="#555555")
label_income.grid(row=2, column=0, padx=20, pady=10, sticky="w")

label_net_worth = tk.Label(root, text="Net Worth", font=font, bg="#f5f5f5", fg="#555555")
label_net_worth.grid(row=3, column=0, padx=20, pady=10, sticky="w")

label_debt = tk.Label(root, text="Debt Amount", font=font, bg="#f5f5f5", fg="#555555")
label_debt.grid(row=4, column=0, padx=20, pady=10, sticky="w")

label_amount_needed = tk.Label(root, text="Loan Amount Requested", font=font, bg="#f5f5f5", fg="#555555")
label_amount_needed.grid(row=5, column=0, padx=20, pady=10, sticky="w")

# Data entry fields
entry_name = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=2)
entry_name.grid(row=1, column=1, padx=20, pady=10)

entry_income = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=2)
entry_income.grid(row=2, column=1, padx=20, pady=10)

entry_net_worth = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=2)
entry_net_worth.grid(row=3, column=1, padx=20, pady=10)

entry_debt = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=2)
entry_debt.grid(row=4, column=1, padx=20, pady=10)

entry_amount_needed = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=2)
entry_amount_needed.grid(row=5, column=1, padx=20, pady=10)

# Result of the analysis
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f5f5f5", fg="#333333")
result_label.grid(row=6, column=0, columnspan=2, pady=20)

# Button to perform analysis
analysis_button = tk.Button(root, text="Perform Analysis", font=("Arial", 14), command=perform_analysis, bg="#3f7cac", fg="white", relief="flat", width=20, height=2)
analysis_button.grid(row=7, column=0, columnspan=2, pady=20)

# Button for new analysis
new_analysis_button = tk.Button(root, text="New Analysis", font=("Arial", 14), command=new_analysis, bg="#ff9800", fg="white", relief="flat", width=20, height=2)

# Start the graphical interface
root.mainloop()
