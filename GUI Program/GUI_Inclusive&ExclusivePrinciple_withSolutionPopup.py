import tkinter as tk
from tkinter import messagebox, ttk


# THIS IS THE MATHEMATICAL CALCULATION FUNCTIONS
def count_two_sets(first_size, second_size, shared_size):
    """Return the number of unique members in two overlapping sets.

    Formula: |A ∪ B| = |A| + |B| - |A ∩ B|
    """
    return first_size + second_size - shared_size

def count_three_sets(
    first_size,
    second_size,
    third_size,
    first_second_size,
    first_third_size,
    second_third_size,
    all_three_size,
):
    """Return the number of unique members in three overlapping sets.

    Formula: |A ∪ B ∪ C| = |A| + |B| + |C|
                          - |A ∩ B| - |A ∩ C| - |B ∩ C|
                          + |A ∩ B ∩ C|
    """
    return (
        first_size
        + second_size
        + third_size
        - first_second_size
        - first_third_size
        - second_third_size
        + all_three_size
    )

# MAIN APPLICATION CLASS
class InclusionExclusionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Club Memberships - Inclusion-Exclusion")
        self.root.geometry("850x850")
        self.root.minsize(720, 720)

        self.mode = tk.StringVar(value="2 clubs")
        self.entries = {}
        self.result_text = tk.StringVar(value="—")
        self.formula_text = tk.StringVar(value="")

        self.configure_styles()
        self.build_interface()
        self.update_fields()

    # THE STYLING OF THE GUI
    def configure_styles(self):
        """Defines the color palette and widget styles used throughout the app."""
        self.root.configure(background="#0B1120")
        style = ttk.Style(self.root)
        style.theme_use("clam")

        style.configure("App.TFrame", background="#0B1120")
        style.configure("App.TLabel", background="#111827", foreground="#F8FAFC", font=("Segoe UI", 12))
        style.configure("Section.TLabelframe", background="#111827", foreground="#F8FAFC", bordercolor="#334155", relief="solid")
        style.configure("Section.TLabelframe.Label", background="#111827", foreground="#E2E8F0", font=("Segoe UI", 12, "bold"))
        style.configure("Result.TLabelframe", background="#172554", foreground="#F8FAFC", bordercolor="#2563EB", relief="solid")
        style.configure("Result.TLabelframe.Label", background="#172554", foreground="#DBEAFE", font=("Segoe UI", 12, "bold"))
        style.configure("App.TRadiobutton", background="#111827", foreground="#F8FAFC", font=("Segoe UI", 12))
        style.map("App.TRadiobutton", background=[("active", "#1E293B")], foreground=[("active", "#FFFFFF")])
        style.configure("App.TEntry", fieldbackground="#0F172A", foreground="#FFFFFF", insertcolor="#FFFFFF",
                         bordercolor="#64748B", lightcolor="#64748B", darkcolor="#334155",
                         font=("Segoe UI", 18), padding=(8, 9))
        style.map("App.TEntry", bordercolor=[("focus", "#93C5FD"), ("active", "#94A3B8")],
                  lightcolor=[("focus", "#93C5FD"), ("active", "#94A3B8")], darkcolor=[("focus", "#475569")])
        style.configure("Secondary.TButton", background="#1E293B", foreground="#F8FAFC", font=("Segoe UI", 11),
                        padding=(10, 7), borderwidth=1)
        style.map("Secondary.TButton", background=[("active", "#334155"), ("pressed", "#475569")],
                  foreground=[("active", "#FFFFFF")])
        style.configure("ResultTitle.TLabel", background="#172554", foreground="#4ADE80", font=("Segoe UI", 11, "bold"))
        style.configure("ResultValue.TLabel", background="#172554", foreground="#F8FAFC", font=("Segoe UI", 24, "bold"))
        style.configure("Formula.TLabel", background="#172554", foreground="#CBD5E1", font=("Segoe UI", 12))

    # MAIN INTERFACE OF  THE PROGRAM
    def build_interface(self):
        """Builds the header, mode selector, input area, buttons, and result panel."""
        header = tk.Frame(self.root, background="#172554", padx=24, pady=12)
        header.pack(fill="x")
        tk.Label(header, text="INCLUSION-EXCLUSION PRINCIPLE", background="#172554",
                foreground="#FFFFFF", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        tk.Label(header, text="Club Membership Calculator", background="#172554",
                foreground="#FFFFFF", font=("Segoe UI", 22, "bold")).pack(anchor="w", pady=(3, 0))
        tk.Label(header, text="Calculate the number of unique students when memberships overlap.",
                background="#172554", foreground="#CBD5E1", font=("Segoe UI", 12)).pack(anchor="w", pady=(4, 0))

        main = ttk.Frame(self.root, padding=(24, 16), style="App.TFrame")
        main.pack(fill="both", expand=True)
        content = ttk.Frame(main, width=780, style="App.TFrame")
        content.pack(anchor="n")

        # Lets the user switch between Two Clubs mode and Three Clubs mode
        mode_frame = ttk.LabelFrame(content, text="Number of clubs", padding=9, style="Section.TLabelframe")
        mode_frame.pack(fill="x", pady=(0, 8))
        ttk.Radiobutton(mode_frame, text="Two clubs", variable=self.mode, value="2 clubs",
                        command=self.update_fields, style="App.TRadiobutton").pack(side="left", padx=(0, 24))
        ttk.Radiobutton(mode_frame, text="Three clubs", variable=self.mode, value="3 clubs",
                        command=self.update_fields, style="App.TRadiobutton").pack(side="left")

        # Input fields are rebuilt dynamically by update_fields() based on the selected mode
        self.input_frame = ttk.LabelFrame(content, text="Membership counts", padding=(16, 14), style="Section.TLabelframe")
        self.input_frame.pack(fill="x", pady=(0, 8))

        button_frame = ttk.Frame(content, style="App.TFrame")
        button_frame.pack(fill="x", pady=(0, 8))
        tk.Button(button_frame, text="Calculate", command=self.calculate, background="#2563EB",
                 foreground="#FFFFFF", activebackground="#1D4ED8", activeforeground="#FFFFFF",
                 font=("Segoe UI", 11, "bold"), padx=14, pady=6, relief="solid", borderwidth=1).pack(side="left")
        ttk.Button(button_frame, text="Clear", command=self.clear, style="Secondary.TButton").pack(side="left", padx=8)

        result_frame = ttk.LabelFrame(content, text="Result", padding=10, style="Result.TLabelframe")
        result_frame.pack(fill="x", pady=(0, 8))
        ttk.Label(result_frame, text="TOTAL UNIQUE STUDENTS", style="ResultTitle.TLabel").pack(anchor="w")
        ttk.Label(result_frame, textvariable=self.result_text, style="ResultValue.TLabel", wraplength=650).pack(anchor="w", pady=(2, 0))
        ttk.Label(result_frame, textvariable=self.formula_text, style="Formula.TLabel", wraplength=650).pack(anchor="w", pady=(6, 0))

    # INPUT HANDLING
    def update_fields(self):
        """Rebuilds the membership-count input fields to match Two Clubs or Three Clubs mode."""
        for child in self.input_frame.winfo_children():
            child.destroy()
        self.entries.clear()

        club_fields = [("math", "Math Club"), ("science", "Science Club")]
        if self.mode.get() == "3 clubs":
            club_fields.append(("literature", "Literature Club"))

        overlap_fields = [("math_science", "Math and Science overlap")]
        if self.mode.get() == "3 clubs":
            overlap_fields.extend([
                ("math_literature", "Math and Literature overlap"),
                ("science_literature", "Science and Literature overlap"),
                ("all_three", "All three clubs overlap"),
            ])

        row = 0
        ttk.Label(self.input_frame, text="CLUB TOTALS", style="App.TLabel",
                 font=("Segoe UI", 10, "bold")).grid(row=row, column=0, columnspan=4, sticky="w", pady=(0, 8))
        row += 1
        row = self.add_field_grid(club_fields, row)

        ttk.Label(self.input_frame, text="OVERLAPS", style="App.TLabel",
                 font=("Segoe UI", 10, "bold")).grid(row=row, column=0, columnspan=4, sticky="w", pady=(12, 6))
        row += 1
        self.add_field_grid(overlap_fields, row)

        self.input_frame.columnconfigure(1, weight=1)
        self.input_frame.columnconfigure(3, weight=1)
        if club_fields:
            self.entries[club_fields[0][0]].focus_set()

    def add_field_grid(self, fields, start_row):
        """Lays out a list of (key, label) fields two per row and stores their entry widgets."""
        for index, (key, label) in enumerate(fields):
            row = start_row + index // 2
            column = (index % 2) * 2
            ttk.Label(self.input_frame, text=label, style="App.TLabel").grid(row=row, column=column, sticky="w", pady=5)
            entry = ttk.Entry(self.input_frame, width=11, style="App.TEntry", justify="center")
            entry.grid(row=row, column=column + 1, sticky="w", padx=(8, 22), pady=5)
            self.entries[key] = entry
        return start_row + (len(fields) + 1) // 2

    def read_values(self):
        """Reads every entry box and converts it to a non-negative integer, or raises ValueError."""
        values = {}
        for key, entry in self.entries.items():
            text = entry.get().strip()
            if not text:
                raise ValueError("Please fill in every membership count.")
            try:
                value = int(text)
            except ValueError as error:
                raise ValueError("Membership counts must be whole numbers.") from error
            if value < 0:
                raise ValueError("Membership counts cannot be negative.")
            values[key] = value
        return values
    
    # VALIDATION
    def validate_values(self, values):
        """Checks that overlaps are logically possible given the club totals entered.

        These checks use the same "only in this region" math as the Venn diagram
        would have shown, even though no diagram is drawn.
        """
        if values["math_science"] > min(values["math"], values["science"]):
            raise ValueError("The Math and Science overlap cannot exceed either club total.")
        if self.mode.get() == "2 clubs" and count_two_sets(
            values["math"], values["science"], values["math_science"]
        ) < 0:
            raise ValueError("The two-club total cannot be negative.")

        if self.mode.get() == "3 clubs":
            if values["math_literature"] > min(values["math"], values["literature"]):
                raise ValueError("The Math and Literature overlap cannot exceed either club total.")
            if values["science_literature"] > min(values["science"], values["literature"]):
                raise ValueError("The Science and Literature overlap cannot exceed either club total.")
            if values["all_three"] > min(
                values["math_science"], values["math_literature"], values["science_literature"]
            ):
                raise ValueError("The all-three intersection cannot exceed any pairwise intersection.")

            # Students who belong to exactly two clubs (not all three)
            if values["math_science"] - values["all_three"] < 0:
                raise ValueError("Math ∩ Science only is negative; check Math ∩ Science and the all-three intersection.")
            if values["math_literature"] - values["all_three"] < 0:
                raise ValueError("Math ∩ Literature only is negative; check Math ∩ Literature and the all-three intersection.")
            if values["science_literature"] - values["all_three"] < 0:
                raise ValueError("Science ∩ Literature only is negative; check Science ∩ Literature and the all-three intersection.")

            # Students who belong to exactly one club
            math_only = values["math"] - values["math_science"] - values["math_literature"] + values["all_three"]
            science_only = values["science"] - values["math_science"] - values["science_literature"] + values["all_three"]
            literature_only = values["literature"] - values["math_literature"] - values["science_literature"] + values["all_three"]
            if math_only < 0:
                raise ValueError("Math-only students would be negative; check Math Club and its two overlaps.")
            if science_only < 0:
                raise ValueError("Science-only students would be negative; check Science Club and its two overlaps.")
            if literature_only < 0:
                raise ValueError("Literature-only students would be negative; check Literature Club and its two overlaps.")

            total = count_three_sets(
                values["math"], values["science"], values["literature"],
                values["math_science"], values["math_literature"], values["science_literature"],
                values["all_three"],
            )
            if total < 0:
                raise ValueError("The calculated union of the three clubs cannot be negative.")

    # CALCULATION
    def calculate(self):
        """Validates input, computes the union total, updates the result panel, and opens the solution popup."""
        try:
            values = self.read_values()
            self.validate_values(values)
        except ValueError as error:
            messagebox.showerror("Check your inputs", str(error), parent=self.root)
            return

        if self.mode.get() == "2 clubs":
            total = count_two_sets(values["math"], values["science"], values["math_science"])
            formula = f"{values['math']} + {values['science']} - {values['math_science']} = {total}"
        else:
            total = count_three_sets(
                values["math"], values["science"], values["literature"],
                values["math_science"], values["math_literature"], values["science_literature"],
                values["all_three"],
            )
            formula = (
                f"{values['math']} + {values['science']} + {values['literature']} - "
                f"{values['math_science']} - {values['math_literature']} - "
                f"{values['science_literature']} + {values['all_three']} = {total}"
            )

        self.result_text.set(f"{total} students")
        self.formula_text.set(f"Inclusion-Exclusion: {formula}")
        self.show_solution_popup(values, total)

    # CLEAR / RESET
    def clear(self):
        """Clears all input fields and resets the result panel to its initial state."""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.result_text.set("—")
        self.formula_text.set("")
      
    # STEP-BY-STEP SOLUTION POPUP
    def show_solution_popup(self, values, total):
        """Opens a scrollable Toplevel window explaining how the result was calculated."""
        popup = tk.Toplevel(self.root)
        popup.title("Step-by-Step Solution")
        popup.geometry("950x750")
        popup.minsize(800, 600)
        popup.resizable(True, True)          # the user can resize and use the native maximize button
        popup.configure(bg="#0B1120")
        popup.transient(self.root)
        self.center_popup(popup, 950, 750)

        # A Canvas + inner Frame is used so the content can scroll vertically
        canvas = tk.Canvas(popup, bg="#0B1120", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True, padx=(16, 0), pady=16)

        scrollbar = ttk.Scrollbar(popup, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y", pady=16)
        canvas.configure(yscrollcommand=scrollbar.set)

        content = tk.Frame(canvas, bg="#0B1120")
        content_width = 860
        window_id = canvas.create_window((0, 0), window=content, anchor="n", width=content_width)

        def recenter_content(event):
            canvas.coords(window_id, max(event.width, content_width) // 2, 0)
            canvas.configure(scrollregion=canvas.bbox("all"))

        canvas.bind("<Configure>", recenter_content)
        content.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        content.grid_columnconfigure(0, weight=1)

        self.build_solution_content(content, values, total)

        # Mouse-wheel scrolling is bound only while this popup is open, and removed when it closes
        popup.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event, canvas))
        popup.bind_all("<Button-4>", lambda event: self.on_mousewheel(event, canvas))
        popup.bind_all("<Button-5>", lambda event: self.on_mousewheel(event, canvas))
        popup.protocol("WM_DELETE_WINDOW", lambda: self.close_popup(popup))

        popup.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

    def build_solution_content(self, content, values, total):
        """Creates the title, formula, given values, step-by-step math, and final answer cards."""
        two_club_mode = self.mode.get() == "2 clubs"

        # Title shown at the top of the popup content 
        tk.Label(content, text="Step-by-Step Solution", bg="#0B1120", fg="#F8FAFC",
                font=("Segoe UI", 28, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 2), padx=4)
        subtitle = "Two-Club Inclusion-Exclusion" if two_club_mode else "Three-Club Inclusion-Exclusion"
        tk.Label(content, text=subtitle, bg="#0B1120", fg="#94A3B8",
                font=("Segoe UI", 18, "bold")).grid(row=1, column=0, sticky="w", pady=(0, 14), padx=4)

        if two_club_mode:
            formula_text = "|A ∪ B| = |A| + |B| − |A ∩ B|"
            value_rows = [
                ("Math Club", values["math"]),
                ("Science Club", values["science"]),
                ("Math ∩ Science", values["math_science"]),
            ]
            step_text = (
                "Step 1 — Add the club totals\n"
                f"{values['math']} + {values['science']} = {values['math'] + values['science']}\n\n"
                "Step 2 — Subtract the overlap\n"
                f"{values['math'] + values['science']} − {values['math_science']} = {total}"
            )
        else:
            formula_text = "|A ∪ B ∪ C| = |A| + |B| + |C|\n− |A ∩ B| − |A ∩ C| − |B ∩ C|\n+ |A ∩ B ∩ C|"
            value_rows = [
                ("Math Club", values["math"]),
                ("Science Club", values["science"]),
                ("Literature Club", values["literature"]),
                ("Math ∩ Science", values["math_science"]),
                ("Math ∩ Literature", values["math_literature"]),
                ("Science ∩ Literature", values["science_literature"]),
                ("Math ∩ Science ∩ Literature", values["all_three"]),
            ]
            step_total = values["math"] + values["science"] + values["literature"]
            pairwise_total = values["math_science"] + values["math_literature"] + values["science_literature"]
            step_text = (
                "Step 1 — Add all three club totals\n"
                f"{values['math']} + {values['science']} + {values['literature']} = {step_total}\n\n"
                "Step 2 — Subtract the three pairwise overlaps\n"
                f"{step_total} − {values['math_science']} − {values['math_literature']} − {values['science_literature']} = {step_total - pairwise_total}\n\n"
                "Step 3 — Add back the all-three overlap (it was subtracted three times in Step 2)\n"
                f"{step_total - pairwise_total} + {values['all_three']} = {total}"
            )

        sections = [
            ("Formula", formula_text),
            ("Given Values", value_rows),
            ("Step-by-Step Calculation", step_text),
            ("Final Answer", f"{total} students"),
        ]

        for offset, (section_name, section_data) in enumerate(sections):
            row = offset + 2  # rows 0 and 1 are used by the title and subtitle above
            card = tk.Frame(content, bg="#111827", bd=1, highlightthickness=1, highlightbackground="#334155",
                            padx=18, pady=16)
            card.grid(row=row, column=0, sticky="ew", pady=(0, 12), padx=4)
            card.grid_columnconfigure(0, weight=1)

            tk.Label(card, text=section_name, bg="#111827", fg="#F8FAFC",
                    font=("Segoe UI", 18, "bold"), anchor="w").grid(row=0, column=0, sticky="w", pady=(0, 10))

            if section_name == "Formula":
                tk.Label(card, text=section_data, bg="#111827", fg="#E2E8F0", font=("Segoe UI", 18, "bold"),
                        justify="left", wraplength=820, anchor="w").grid(row=1, column=0, sticky="w")

            elif section_name == "Given Values":
                values_frame = tk.Frame(card, bg="#111827")
                values_frame.grid(row=1, column=0, sticky="ew")
                for value_row, (name, value) in enumerate(value_rows):
                    tk.Label(values_frame, text=name, bg="#111827", fg="#E2E8F0", font=("Segoe UI", 15),
                            anchor="w").grid(row=value_row, column=0, sticky="w", padx=(0, 24), pady=4)
                    tk.Label(values_frame, text=str(value), bg="#111827", fg="#F8FAFC", font=("Segoe UI", 15, "bold"),
                            anchor="e").grid(row=value_row, column=1, sticky="e", pady=4)
                values_frame.grid_columnconfigure(0, weight=1)

            elif section_name == "Step-by-Step Calculation":
                tk.Label(card, text=section_data, bg="#111827", fg="#E2E8F0", font=("Segoe UI", 15),
                        justify="left", anchor="w", wraplength=820).grid(row=1, column=0, sticky="w")

            elif section_name == "Final Answer":
                final_frame = tk.Frame(card, bg="#172554", bd=1, highlightthickness=1, highlightbackground="#2563EB",
                                       padx=18, pady=16)
                final_frame.grid(row=1, column=0, sticky="ew")
                tk.Label(final_frame, text="FINAL ANSWER", bg="#172554", fg="#4ADE80",
                        font=("Segoe UI", 18, "bold")).pack(anchor="center")
                tk.Label(final_frame, text=section_data, bg="#172554", fg="#F8FAFC",
                        font=("Segoe UI", 28, "bold")).pack(anchor="center", pady=(8, 0))

        content.update_idletasks()

    def close_popup(self, popup):
        """Removes the popup-only mouse-wheel bindings so the main window is unaffected, then closes it."""
        popup.unbind_all("<MouseWheel>")
        popup.unbind_all("<Button-4>")
        popup.unbind_all("<Button-5>")
        popup.destroy()

    def center_popup(self, popup, width, height):
        """Positions the popup in the center of the main window when it first opens."""
        popup.update_idletasks()
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_w = self.root.winfo_width()
        root_h = self.root.winfo_height()
        x = root_x + (root_w - width) // 2
        y = root_y + (root_h - height) // 2
        popup.geometry(f"{width}x{height}+{x}+{y}")
    
    # FOR THE MOUSE-WHEEL SCROLLING
    def on_mousewheel(self, event, canvas):
        """Scrolls the given canvas up or down in response to the mouse wheel."""
        if event.delta:
            canvas.yview_scroll(int(-event.delta / 120), "units")   
        elif event.num == 4:
            canvas.yview_scroll(-1, "units")                        
        elif event.num == 5:
            canvas.yview_scroll(1, "units")                         
        return "break"
      
# THE PROGRAM STARTUP
def main():
    root = tk.Tk()
    InclusionExclusionApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
