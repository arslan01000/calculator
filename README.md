# **Arithmetic Expression Solver**

## **Overview**
This Python program solves arithmetic expressions, handling basic operations such as addition, subtraction, multiplication, division, square root calculations, and exponentiation. It simplifies expressions step-by-step and provides the final result interactively.


---

## **Features**
- **Supported Operations**:
  - `+` Addition
  - `-` Subtraction
  - `*` Multiplication
  - `/` Division
  - `^` Exponentiation
  - `sqrt()` Square root
  - Handles nested operations like `(10 + 5) * sqrt(16)`
- **Input Validation**:
  - Prevents invalid inputs, including division by zero.
- **Interactive**:
  - Continuously prompts for expressions until the user exits.
- **Custom Behavior**:
  - Rejects negative results (e.g., `10 - 20`).

---

## **How to Use**
1. **Run the Program**:  
   Execute the Python script.
2. **Input an Expression**:  
   Enter a valid mathematical expression. Examples:
   - `10+12`
   - `sqrt(100)*10`
   - `(99/3)`
   - `sqrt(100)+(10/2)^2`
3. **View the Result**:  
   The program displays the evaluated result.
4. **Exit**:  
   Type `n` when prompted to stop the program.

---

## **Code Structure**
- **Key Functions**:
  - `sqrt_check(s)`: Processes square root operations (`sqrt()`).
  - `solve_for_degree(s, pos)`: Handles exponentiation (`^`).
  - `four_function(a, b, c)`: Performs basic arithmetic operations.
  - `solve_it(s)`: Resolves expressions with `*`, `/`, `+`, `-`.
  - `solve_for_bracket(s, pos)`: Processes brackets with exponents.
  - `solve_for_bracket_only(s, pos)`: Resolves simple bracketed expressions.
- **Interactive Loop**:
  - Continuously processes user input and solves it step-by-step.

---

## **Examples**
### **Input**:  
`sqrt(100)+(10/2)^2`  
### **Output**:  
`The result is: 35`  

### **Input**:  
`(10+5)*sqrt(16)`  
### **Output**:  
`The result is: 60`  

---

## **Limitations**
- Does not handle negative results or inputs.
- Division only returns integers (uses floor division).
- May struggle with very large or deeply nested expressions.

---

## **Future Improvements**
- Support floating-point calculations.
- Handle negative numbers and results.
- Improve efficiency for complex expressions.
