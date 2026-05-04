## **Part 1. Main Document.**

### **1. Title and Basic Information.**

• **Name:** Calculator v.1

• **Purpose:** Project No. 1. Product.

• **Project Phase:** Phase I.

• **Technology Stack:** Python

• **Project Status:** The first version is fully completed.

### **2. Brief Project Description.**

• The Calculator v.1 project is a multifunctional desktop application in Python with a graphical interface, designed to perform a wide range of mathematical operations.

• The program combines the functions of a basic, engineering, and scientific calculator, providing tools for arithmetic calculations, working with prime numbers, solving equations, trigonometric transformations, and other mathematical tasks in a convenient and modern interface with saved history.

### **3. Clear Project Goals.**

• Demonstrate NS work on projects.

• Create convenience and multifunctionality for the user.

• Expand the NS ecosystem in the project domain.

### **4. Project Components (Functions).**

• **What is already implemented:**

**4.1** Addition
(a + b)

**4.2** Subtraction
(a – b)

**4.3** Multiplication
(a × b)

**4.4** Division
(a : b)

**4.5** GCD Calculation
(Euclidean Algorithm)

**4.6** LCM Calculation
(Based on GCD)

**4.7** Factorial
(a! = 1 × 2 × 3 × ... × a)

**4.8** Double Factorial
(If a is even: a!! = 2 × 4 × 6 × ... × a)
(If a is odd: a!! = 1 × 3 × 5 × ... × a)

**4.9** Prime Factorization
(a = p₁ × p₂ × ...)

**4.10** Exponentiation
(a^b = a × a × ... × a)

**4.11** Primality Test
(If a number a has only divisors 1 and a, then it is prime; otherwise, it is composite)

**4.12** Logarithms
(logₐ(b))

**4.13** Square Root
(√a = a^0.5)

**4.14** Solving Linear Equations
(ax + b = 0)

**4.15** Solving Quadratic Equations
(ax² + bx + c = 0)

**4.16** Trigonometric Functions
(cos, sin, tg, ctg)

**4.17** Conversion Between Degrees and Radians
(a° = b (rad))

**4.18** Absolute Value, Integer Part, Fractional Part of a Number
(|a|, [a], {a})

• **What may be added in the future:**

**4.19** Graph Plotting

**4.20** Solving n-th Degree Equations

**4.21** Solving Parameters

**4.22** Solving Trigonometric Equations

**4.23** Representation of Irrational Numbers as Fractions (If possible)

**4.24** Derivatives and Integrals (Fundamentals of Mathematical Analysis)

### **5. User Guide.**

• Before using the application, it is important to understand how it works. First, you should familiarize yourself with the functions located in the left panel of the screen.

• After choosing, you need to click on the desired function and move to the right panel, where input fields will appear for entering numbers to perform the selected operation.

• To make it clearer what each input variable represents, there is a hint directly below the input fields in the form of a formula with the same variables set by the user.

• After entering the data, you need to perform the calculation by pressing the button below. After obtaining the result, you can choose a new function or clear the current calculations using the buttons in the bottom panel.

• All calculations are saved in the history, which is available in the top right corner. It can be copied or cleared.

## **Part 2. Technical Document.**

### **1. Development Goals.**

• Achieve a clear interface and convenient mechanics.

• Optimize complex parts of the code.

• Provide a reusable code template.

### **2. Technologies Used.**

• **Programming Language:** Python.

• **Libraries:** tkinter, math, json, os, typing.

### **3. Project Architecture.**

• The project uses the **Model-View-Controller (MVC)** approach within a single main class Calculator.

• **Model** – these are mathematical functions such as addition, GCD calculation, equation solving. They are implemented as class methods.

• **View** – this is the entire graphical interface: buttons, input fields, panels created using tkinter.

• **Controller** – this is the logic that connects the interface and computations. It processes button clicks, data input, and result display.

### **4. Project Structure.**

• The project consists of one main file: calculator.py.

• This file contains all the code: the Calculator class, interface settings, and all mathematical operations.

• Only the standard Python library is required to run it; no additional installation is needed.

### **5. Key System Components.**

• Main class Calculator – controls the entire application.

• Color scheme (colors dictionary) – stores all interface colors in a dark style.

• Current state: selected operation, list of input fields, calculation history.

• Special display variables (result_var, expression_var) – show the result and formula.

• History manager – saves history to calc_history.json and loads it at startup.

• Mathematical engine – more than 20 methods performing all operations from addition to solving quadratic equations.

### **6. User Interface Implementation.**

• The interface is built using the tkinter library.

• The style is defined manually through colors and fonts, without using themes.

• The interface is divided into three main parts:

• Top panel with the title and "Reset" and "History" buttons.

• Left panel with a list of all operations, grouped into categories.

• Right panel with input fields and a result display area.

• Interface elements are dynamic: the number of input fields changes depending on the selected operation.

• There are hover effects on buttons and support for hotkeys.

### **7. Development Process.**

• First, a basic window framework was created using tkinter.

• Then all mathematical functions were implemented step by step.

• After that, the interface was developed: layout, buttons, input fields.

• Next, the interface was connected to the mathematical functions.

• Finally, additional systems were added: history, error handling, dialog windows.

• The entire process was accompanied by testing and bug fixing.

### **8. Main Challenges and Solutions.**

• **(1)** Challenge: how to create different numbers of input fields for different operations.

Solution: the select_operation function dynamically creates the required number of input fields and stores them in a list.

• **(2)** Challenge: how to handle special input such as "pi" or fractions like "1/2".

Solution: validation is added in the calculate method before converting input into numbers.

• **(3)** Challenge: how to save calculation history between program runs.

Solution: history is saved to a JSON file after each calculation and loaded at startup.

• **(4)** Challenge: how to correctly handle all possible user errors.

Solution: all calculations are wrapped in a try-except block that catches errors and displays clear messages.

### **9. Current Project Limitations.**

• All code is contained in a single file and one class, which may complicate further scaling.

• Results are always displayed as decimal numbers; common fractions are not supported.

• The interface has a fixed dark theme; changing themes or colors is not supported.

• If a calculation takes too long, the interface will freeze during execution.

• Support for special input formats is limited (for example, complex expressions cannot be entered).

• The interface is only in Russian; switching to other languages is not supported.

### **10. Possible Improvements and Development Plans.**

• Split the code into multiple modules for easier maintenance.

• Add more advanced mathematical functions.

• Implement appearance settings: themes, colors, fonts.

• Improve the history system: add date and time, export to different formats.

• Add support for multiple interface languages.

• Use multithreading so that heavy calculations do not block the interface.

• Create an executable .exe file to run the program without installing Python.
