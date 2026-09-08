import tkinter as tk
from tkinter import messagebox


# ==============================
# GAUSS-SEIDEL CALCULATION
# ==============================

def calculate():

    try:
        # Get matrix A
        A = [
            [float(a11.get()), float(a12.get()), float(a13.get())],
            [float(a21.get()), float(a22.get()), float(a23.get())],
            [float(a31.get()), float(a32.get()), float(a33.get())]
        ]

        # Get constants
        b = [
            float(b1.get()),
            float(b2.get()),
            float(b3.get())
        ]

        # Check diagonal elements
        if A[0][0] == 0 or A[1][1] == 0 or A[2][2] == 0:
            messagebox.showerror(
                "Error",
                "Diagonal elements cannot be zero."
            )
            return

        # Initial guesses
        x = 0.0
        y = 0.0
        z = 0.0

        # Get tolerance and maximum iterations
        tolerance = float(tol.get())
        max_iter = int(iterations.get())

        # Clear previous result
        result.delete("1.0", tk.END)

        # Result heading
        result.insert(
            tk.END,
            "Iteration\tX\t\tY\t\tZ\t\tError\n"
        )

        result.insert(
            tk.END,
            "-" * 80 + "\n"
        )

        # ==============================
        # GAUSS-SEIDEL ITERATION
        # ==============================

        for i in range(1, max_iter + 1):

            old_x = x
            old_y = y
            old_z = z

            # Calculate X
            x = (
                b[0]
                - A[0][1] * y
                - A[0][2] * z
            ) / A[0][0]

            # Calculate Y using NEW X
            y = (
                b[1]
                - A[1][0] * x
                - A[1][2] * z
            ) / A[1][1]

            # Calculate Z using NEW X and NEW Y
            z = (
                b[2]
                - A[2][0] * x
                - A[2][1] * y
            ) / A[2][2]

            # Calculate error
            error = max(
                abs(x - old_x),
                abs(y - old_y),
                abs(z - old_z)
            )

            # Display iteration
            result.insert(
                tk.END,
                f"{i}\t"
                f"{x:.6f}\t\t"
                f"{y:.6f}\t\t"
                f"{z:.6f}\t\t"
                f"{error:.6f}\n"
            )

            # Check convergence
            if error < tolerance:

                result.insert(
                    tk.END,
                    "\n========================================\n"
                )

                result.insert(
                    tk.END,
                    "          CONVERGED!\n"
                )

                result.insert(
                    tk.END,
                    "========================================\n\n"
                )

                result.insert(
                    tk.END,
                    f"X = {x:.6f}\n"
                )

                result.insert(
                    tk.END,
                    f"Y = {y:.6f}\n"
                )

                result.insert(
                    tk.END,
                    f"Z = {z:.6f}\n"
                )

                result.insert(
                    tk.END,
                    f"\nNumber of iterations = {i}\n"
                )

                return

        # If not converged
        result.insert(
            tk.END,
            "\nMaximum number of iterations reached.\n"
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )

    except ZeroDivisionError:

        messagebox.showerror(
            "Error",
            "Diagonal elements cannot be zero."
        )


# ==============================
# CLEAR FUNCTION
# ==============================

def clear():

    all_entries = [
        a11, a12, a13,
        a21, a22, a23,
        a31, a32, a33,
        b1, b2, b3
    ]

    for entry in all_entries:
        entry.delete(0, tk.END)

    # Put default values again
    a11.insert(0, "10")
    a12.insert(0, "1")
    a13.insert(0, "1")

    a21.insert(0, "2")
    a22.insert(0, "10")
    a23.insert(0, "1")

    a31.insert(0, "2")
    a32.insert(0, "2")
    a33.insert(0, "10")

    b1.insert(0, "12")
    b2.insert(0, "13")
    b3.insert(0, "14")

    tol.delete(0, tk.END)
    tol.insert(0, "0.000001")

    iterations.delete(0, tk.END)
    iterations.insert(0, "100")

    result.delete("1.0", tk.END)


# ==============================
# MAIN WINDOW
# ==============================

window = tk.Tk()

window.title("Gauss-Seidel Calculator")

window.geometry("850x700")


# ==============================
# TITLE
# ==============================

title = tk.Label(
    window,
    text="GAUSS-SEIDEL CALCULATOR",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)


# ==============================
# MATRIX FRAME
# ==============================

matrix_frame = tk.Frame(window)

matrix_frame.pack(pady=10)


tk.Label(
    matrix_frame,
    text="Coefficient Matrix",
    font=("Arial", 14, "bold")
).grid(
    row=0,
    column=0,
    columnspan=3,
    pady=10
)


# Column headings

tk.Label(
    matrix_frame,
    text="X",
    font=("Arial", 11, "bold")
).grid(row=1, column=0)

tk.Label(
    matrix_frame,
    text="Y",
    font=("Arial", 11, "bold")
).grid(row=1, column=1)

tk.Label(
    matrix_frame,
    text="Z",
    font=("Arial", 11, "bold")
).grid(row=1, column=2)

tk.Label(
    matrix_frame,
    text="Constant (b)",
    font=("Arial", 11, "bold")
).grid(row=1, column=3)


# ==============================
# ENTRY BOXES
# ==============================

a11 = tk.Entry(matrix_frame, width=8)
a12 = tk.Entry(matrix_frame, width=8)
a13 = tk.Entry(matrix_frame, width=8)

a21 = tk.Entry(matrix_frame, width=8)
a22 = tk.Entry(matrix_frame, width=8)
a23 = tk.Entry(matrix_frame, width=8)

a31 = tk.Entry(matrix_frame, width=8)
a32 = tk.Entry(matrix_frame, width=8)
a33 = tk.Entry(matrix_frame, width=8)

b1 = tk.Entry(matrix_frame, width=10)
b2 = tk.Entry(matrix_frame, width=10)
b3 = tk.Entry(matrix_frame, width=10)


# Row 1

a11.grid(row=2, column=0, padx=5, pady=5)
a12.grid(row=2, column=1, padx=5, pady=5)
a13.grid(row=2, column=2, padx=5, pady=5)
b1.grid(row=2, column=3, padx=10, pady=5)


# Row 2

a21.grid(row=3, column=0, padx=5, pady=5)
a22.grid(row=3, column=1, padx=5, pady=5)
a23.grid(row=3, column=2, padx=5, pady=5)
b2.grid(row=3, column=3, padx=10, pady=5)


# Row 3

a31.grid(row=4, column=0, padx=5, pady=5)
a32.grid(row=4, column=1, padx=5, pady=5)
a33.grid(row=4, column=2, padx=5, pady=5)
b3.grid(row=4, column=3, padx=10, pady=5)


# ==============================
# DEFAULT VALUES
# ==============================

a11.insert(0, "10")
a12.insert(0, "1")
a13.insert(0, "1")
b1.insert(0, "12")

a21.insert(0, "2")
a22.insert(0, "10")
a23.insert(0, "1")
b2.insert(0, "13")

a31.insert(0, "2")
a32.insert(0, "2")
a33.insert(0, "10")
b3.insert(0, "14")


# ==============================
# SETTINGS
# ==============================

settings = tk.Frame(window)

settings.pack(pady=20)


tk.Label(
    settings,
    text="Tolerance:"
).grid(
    row=0,
    column=0,
    padx=5
)


tol = tk.Entry(
    settings,
    width=12
)

tol.insert(
    0,
    "0.000001"
)

tol.grid(
    row=0,
    column=1,
    padx=5
)


tk.Label(
    settings,
    text="Maximum Iterations:"
).grid(
    row=0,
    column=2,
    padx=5
)


iterations = tk.Entry(
    settings,
    width=10
)

iterations.insert(
    0,
    "100"
)

iterations.grid(
    row=0,
    column=3,
    padx=5
)


# ==============================
# BUTTONS
# ==============================

button_frame = tk.Frame(window)

button_frame.pack(pady=10)


calculate_button = tk.Button(
    button_frame,
    text="CALCULATE",
    command=calculate,
    font=("Arial", 12, "bold"),
    width=15
)

calculate_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    command=clear,
    font=("Arial", 12, "bold"),
    width=15
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# ==============================
# RESULT
# ==============================

tk.Label(
    window,
    text="Iteration Results",
    font=("Arial", 14, "bold")
).pack(pady=10)


result = tk.Text(
    window,
    width=95,
    height=18,
    font=("Courier New", 10)
)

result.pack(
    padx=10,
    pady=5
)


# ==============================
# START PROGRAM
# ==============================

window.mainloop()
