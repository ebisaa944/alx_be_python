#!/usr/bin/python3
"""
Bank Account Class
Implements basic banking operations with encapsulation
"""

class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, initial_balance=0):
        """Initialize account with optional starting balance"""
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """Add funds to the account"""
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """Remove funds from account if available"""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Show current balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")
