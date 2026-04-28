#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mortgage Simulator: Loan Repayment Schedule with Extra Payments.
Analyzes the impact of early principal payments on total interest and duration.
"""

def simulate_mortgage(principal, annual_rate, monthly_payment, 
                      extra_pay_start=0, extra_pay_end=0, extra_pay_amount=0):
    """
    Simulates a loan repayment schedule.
    Returns total paid and total months.
    """
    total_paid = 0.0
    month = 0
    current_balance = principal
    monthly_rate = annual_rate / 12

    print(f"{'Month':<8} | {'Total Paid':<15} | {'Remaining Balance':<18}")
    print("-" * 45)

    while current_balance > 0:
        month += 1
        interest_accrued = current_balance * monthly_rate
        
        # Determine if an extra payment is applicable this month
        current_extra = extra_pay_amount if extra_pay_start <= month <= extra_pay_end else 0
        
        # Check if it's the last payment
        if current_balance + interest_accrued < (monthly_payment + current_extra):
            last_payment = current_balance + interest_accrued
            total_paid += last_payment
            current_balance = 0
        else:
            current_balance = current_balance + interest_accrued - monthly_payment - current_extra
            total_paid += (monthly_payment + current_extra)
            
        print(f"{month:<8} | {total_paid:<15.2f} | {current_balance:<18.2f}")

    return total_paid, month

if __name__ == "__main__":
    # Initial Configuration
    INITIAL_LOAN = 500000.0
    ANNUAL_INTEREST = 0.05
    MONTHLY_BASE_PAYMENT = 2684.11
    
    # Extra payment settings (Exercise 1.11)
    START_EXTRA = 61
    END_EXTRA = 108
    EXTRA_AMOUNT = 1000

    final_total, total_months = simulate_mortgage(
        INITIAL_LOAN, ANNUAL_INTEREST, MONTHLY_BASE_PAYMENT,
        START_EXTRA, END_EXTRA, EXTRA_AMOUNT
    )

    print("-" * 45)
    print(f"Final Summary:")
    print(f"Total Amount Paid: ${final_total:,.2f}")
    print(f"Total Duration: {total_months} months ({total_months/12:.1f} years)")
