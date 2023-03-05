# Gross Up Calculator

This is a simple Python script for calculating gross up amount for payroll. It takes into account the taxable gross salary, federal tax rate, state tax rate, local tax rate, OASDI and Medicare rates.

## Table of Contents
- [Introduction](#introduction)
- [How to Use](#how-to-use)
- [Output](#output)
- [Limitations](#limitations)

## Introduction

This Python script calculates the gross up amount for payroll based on the taxable gross salary and tax rates for federal, state, local, OASDI, and Medicare. It was created for use in the United States and uses California tax rates as the default.

## How to Use

1. Open the script in your preferred Python environment (e.g. IDLE, Jupyter Notebook, PyCharm, etc.).
2. Update the value of the `taxableGrossSalary` variable to match the amount you want to gross up.
3. Update the tax rates in the `federalTax`, `stateTax`, `localTax`, `oasdi`, and `medicare` variables to match the rates for your state and federal government.
4. Run the script and view the results.

## Output

The script outputs three values:
- **Total Gross Up Salary:** This is the new gross salary after grossing up the taxable gross salary.
- **Total Gross Up:** This is the difference between the new gross salary and the original taxable gross salary.
- **Individual Tax Gross Up Amount:** This is the amount of gross up for each tax category (federal, state, local, OASDI, Medicare).

## Limitations

- This script is only intended for use in calculating gross up amount for payroll in the United States.
- The tax rates are based on California and may not be applicable in other states.
- This script does not take into account any deductions or exemptions that may affect the tax rate.

