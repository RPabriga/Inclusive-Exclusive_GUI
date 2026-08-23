import tkinter as tk
from tkinter import messagebox, ttk # GUI module for python

# Calculates the total number of unique members in two overlapping clubs
def count_two_sets(first_size, second_size, shared_size):
	"""Return the number of unique members in two overlapping sets."""
	return first_size + second_size - shared_size # Add both club totals, then subtract the overlap, because students in both clubs would otherwise be counted twice

# Calculates the total number of unique members in three overlapping clubs
def count_three_sets(
	first_size,
	second_size,
	third_size,
	first_second_size,
	first_third_size,
	second_third_size,
	all_three_size,
):
	"""Return the number of unique members in three overlapping sets."""
	# Inclusion-Exclusion formula for three sets:
    # Add the three club totals
    # Subtract the three pairwise overlaps
    # Add the students who belong to all three clubs
	return (
		first_size
		+ second_size
		+ third_size
		- first_second_size
		- first_third_size
		- second_third_size
		+ all_three_size
	)

# Main class that contains the GUI and all of its functions
class InclusionExclusionApp:
	# Initializes the application
	def __init__(self, root): # Sets the title and size of the application window
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

	# Configures the colors, fonts, buttons, and other GUI styles
	def configure_styles(self):
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
		style.configure("App.TEntry", fieldbackground="#0F172A", foreground="#FFFFFF", insertcolor="#FFFFFF", bordercolor="#64748B", lightcolor="#64748B", darkcolor="#334155", font=("Segoe UI", 18), padding=(8, 9))
		style.map("App.TEntry", bordercolor=[("focus", "#93C5FD"), ("active", "#94A3B8")], lightcolor=[("focus", "#93C5FD"), ("active", "#94A3B8")], darkcolor=[("focus", "#475569")])
		style.configure("Action.TButton", background="#2563EB", foreground="#FFFFFF", font=("Segoe UI", 11, "bold"), padding=(12, 7), borderwidth=1)
		style.map("Action.TButton", background=[("active", "#1D4ED8"), ("pressed", "#1E40AF")], foreground=[("disabled", "#CBD5E1")])
		style.configure("Secondary.TButton", background="#1E293B", foreground="#F8FAFC", font=("Segoe UI", 11), padding=(10, 7), borderwidth=1)
		style.map("Secondary.TButton", background=[("active", "#334155"), ("pressed", "#475569")], foreground=[("active", "#FFFFFF")])
		style.configure("ResultTitle.TLabel", background="#172554", foreground="#4ADE80", font=("Segoe UI", 11, "bold"))
		style.configure("ResultValue.TLabel", background="#172554", foreground="#F8FAFC", font=("Segoe UI", 24, "bold"))
		style.configure("Formula.TLabel", background="#172554", foreground="#CBD5E1", font=("Segoe UI", 12))

	# Creates the main GUI interface
	def build_interface(self):
		header = tk.Frame(self.root, background="#172554", padx=24, pady=12)
		header.pack(fill="x")
		tk.Label(
			header,
			text="INCLUSION-EXCLUSION PRINCIPLE",
			background="#172554",
			foreground="#FFFFFF",
			font=("Segoe UI", 12, "bold"),
		).pack(anchor="w")
		tk.Label(
			header,
			text="Club Membership Calculator",
			background="#172554",
			foreground="#FFFFFF",
			font=("Segoe UI", 22, "bold"),
		).pack(anchor="w", pady=(3, 0))
		tk.Label(
			header,
			text="Calculate the number of unique students when memberships overlap.",
			background="#172554",
			foreground="#CBD5E1",
			font=("Segoe UI", 12),
		).pack(anchor="w", pady=(4, 0))

		main = ttk.Frame(self.root, padding=(24, 16), style="App.TFrame")
		main.pack(fill="both", expand=True)
		content = ttk.Frame(main, width=780, style="App.TFrame")
		content.pack(anchor="n")

		mode_frame = ttk.LabelFrame(content, text="Number of clubs", padding=9, style="Section.TLabelframe")
		mode_frame.pack(fill="x", pady=(0, 8))
		ttk.Radiobutton(
			mode_frame,
			text="Two clubs",
			variable=self.mode,
			value="2 clubs",
			command=self.update_fields,
			style="App.TRadiobutton",
		).pack(side="left", padx=(0, 24))
		ttk.Radiobutton(
			mode_frame,
			text="Three clubs",
			variable=self.mode,
			value="3 clubs",
			command=self.update_fields,
			style="App.TRadiobutton",
		).pack(side="left")

		self.input_frame = ttk.LabelFrame(content, text="Membership counts", padding=(16, 14), style="Section.TLabelframe")
		self.input_frame.pack(fill="x", pady=(0, 8))

		button_frame = ttk.Frame(content, style="App.TFrame")
		button_frame.pack(fill="x", pady=(0, 8))
		tk.Button(
			button_frame,
			text="Calculate",
			command=self.calculate,
			background="#2563EB",
			foreground="#FFFFFF",
			activebackground="#1D4ED8",
			activeforeground="#FFFFFF",
			font=("Segoe UI", 11, "bold"),
			padx=14,
			pady=6,
			relief="solid",
			borderwidth=1,
		).pack(side="left")
		ttk.Button(button_frame, text="Clear", command=self.clear, style="Secondary.TButton").pack(side="left", padx=8)
		ttk.Button(button_frame, text="Load Case 2", command=self.load_case_two, style="Secondary.TButton").pack(side="right", padx=8)
		ttk.Button(button_frame, text="Load Case 1", command=self.load_case_one, style="Secondary.TButton").pack(side="right")

		result_frame = ttk.LabelFrame(content, text="Result", padding=10, style="Result.TLabelframe")
		result_frame.configure(style="Result.TLabelframe")
		result_frame.pack(fill="x", pady=(0, 8))
		ttk.Label(
			result_frame,
			text="TOTAL UNIQUE STUDENTS",
			style="ResultTitle.TLabel",
		).pack(anchor="w")
		ttk.Label(
			result_frame,
			textvariable=self.result_text,
			style="ResultValue.TLabel",
			wraplength=650,
		).pack(anchor="w", pady=(2, 0))
		ttk.Label(
			result_frame,
			textvariable=self.formula_text,
			style="Formula.TLabel",
			wraplength=650,
		).pack(anchor="w", pady=(6, 0))

	# Updates the input fields depending on whether
    # the user selected two clubs or three clubs
	def update_fields(self):
		for child in self.input_frame.winfo_children():
			child.destroy()
		self.entries.clear()

		club_fields = [
			("math", "Math Club"),
			("science", "Science Club"),
		]
		if self.mode.get() == "3 clubs":
			club_fields.append(("literature", "Literature Club"))

		overlap_fields = [
			("math_science", "Math and Science overlap"),
		]
		if self.mode.get() == "3 clubs":
			overlap_fields.extend(
				[
					("math_literature", "Math and Literature overlap"),
					("science_literature", "Science and Literature overlap"),
					("all_three", "All three clubs overlap"),
				]
			)
        # Starting row for the input fields
		row = 0
		ttk.Label(self.input_frame, text="CLUB TOTALS", style="App.TLabel", font=("Segoe UI", 10, "bold")).grid(
			row=row, column=0, columnspan=4, sticky="w", pady=(0, 8)
		)
		row += 1
		row = self.add_field_grid(club_fields, row)

		ttk.Label(self.input_frame, text="OVERLAPS", style="App.TLabel", font=("Segoe UI", 10, "bold")).grid(
			row=row, column=0, columnspan=4, sticky="w", pady=(12, 6)
		)
		row += 1
		self.add_field_grid(overlap_fields, row)

		self.input_frame.columnconfigure(1, weight=1)
		self.input_frame.columnconfigure(3, weight=1)
		if club_fields:
			self.entries[club_fields[0][0]].focus_set()

	 # Creates the input boxes and labels dynamically
	def add_field_grid(self, fields, start_row):
		for index, (key, label) in enumerate(fields):
			row = start_row + index // 2
			column = (index % 2) * 2
			ttk.Label(self.input_frame, text=label, style="App.TLabel").grid(
				row=row, column=column, sticky="w", pady=5
			)
			entry = ttk.Entry(self.input_frame, width=11, style="App.TEntry", justify="center")
			entry.grid(row=row, column=column + 1, sticky="w", padx=(8, 22), pady=5)
			self.entries[key] = entry

		return start_row + (len(fields) + 1) // 2

	# Reads all values entered by the user
	def read_values(self):
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

	# Checks whether the entered membership values are valid
	def validate_values(self, values):
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
				values["math_science"],
				values["math_literature"],
				values["science_literature"],
			):
				raise ValueError("The all-three intersection cannot exceed any pairwise intersection.")

			math_science_only = values["math_science"] - values["all_three"]
			math_literature_only = values["math_literature"] - values["all_three"]
			science_literature_only = values["science_literature"] - values["all_three"]
			if math_science_only < 0:
				raise ValueError("Math ∩ Science only is negative; check Math ∩ Science and the all-three intersection.")
			if math_literature_only < 0:
				raise ValueError("Math ∩ Literature only is negative; check Math ∩ Literature and the all-three intersection.")
			if science_literature_only < 0:
				raise ValueError("Science ∩ Literature only is negative; check Science ∩ Literature and the all-three intersection.")

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
				values["math"],
				values["science"],
				values["literature"],
				values["math_science"],
				values["math_literature"],
				values["science_literature"],
				values["all_three"],
			)
			if total < 0:
				raise ValueError("The calculated union of the three clubs cannot be negative.")

	# Performs the main calculation when the Calculate button is clicked
	def calculate(self):
		try:
			values = self.read_values()
			self.validate_values(values)
		except ValueError as error:
			messagebox.showerror("Check your inputs", str(error), parent=self.root)
			return

		if self.mode.get() == "2 clubs":
			total = count_two_sets(values["math"], values["science"], values["math_science"])
			formula = (
				f"{values['math']} + {values['science']} - {values['math_science']} "
				f"= {total}"
			)
		else:
			total = count_three_sets(
				values["math"],
				values["science"],
				values["literature"],
				values["math_science"],
				values["math_literature"],
				values["science_literature"],
				values["all_three"],
			)
			formula = (
				f"{values['math']} + {values['science']} + {values['literature']} - "
				f"{values['math_science']} - {values['math_literature']} - "
				f"{values['science_literature']} + {values['all_three']} = {total}"
			)

		self.result_text.set(f"{total} students")
		self.formula_text.set(f"Inclusion-Exclusion: {formula}")

	# Clears all input fields and resets the result
	def clear(self):
		for entry in self.entries.values():
			entry.delete(0, tk.END)
		self.result_text.set("—")
		self.formula_text.set("")

	 # Loads a set of predefined values into the input fields
	def load_values(self, values):
		for key, value in values.items():
			if key in self.entries:
				self.entries[key].delete(0, tk.END)
				self.entries[key].insert(0, str(value))
		self.calculate()

	# Loads Case 1
    # Case 1 uses two clubs
	def load_case_one(self):
		self.mode.set("2 clubs")
		self.update_fields()
		self.load_values({"math": 25, "science": 18, "math_science": 10})

	# Loads Case 2
    # Case 2 uses three clubs
	def load_case_two(self):
		self.mode.set("3 clubs")
		self.update_fields()
		self.load_values(
			{
				"math": 20,
				"science": 15,
				"literature": 10,
				"math_science": 5,
				"math_literature": 3,
				"science_literature": 2,
				"all_three": 1,
			}
		)

# Main function that starts the application
def main():
	root = tk.Tk() # Creates the main Tkinter window
	InclusionExclusionApp(root) # Creates the Inclusion-Exclusion application
	root.mainloop() # Keeps the GUI running and responsive

# Runs the main function only when this file
# is executed directly
if __name__ == "__main__":
	main()
