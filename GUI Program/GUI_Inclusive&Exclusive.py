import tkinter as tk
from tkinter import messagebox, ttk

# Calculates the total number of unique members in two
def count_two_sets(first_size, second_size, shared_size):
	"""Unique members across two overlapping sets (inclusion-exclusion)."""
	return first_size + second_size - shared_size

# Calculates the total number of unique members in three
def count_three_sets(
	first_size,
	second_size,
	third_size,
	first_second_size,
	first_third_size,
	second_third_size,
	all_three_size,
):
	"""Unique members across three overlapping sets (inclusion-exclusion)."""
	return (
		first_size
		+ second_size
		+ third_size
		- first_second_size
		- first_third_size
		- second_third_size
		+ all_three_size
	)

class InclusionExclusionApp: # The main application of the program
	def __init__(self, root):
		self.root = root
		self.root.title("Club Memberships - Inclusion-Exclusion")
		self.root.geometry("850x780")
		self.root.minsize(700, 680)

		self.mode = tk.StringVar(value="2 clubs")  # Stores whether the user selected two or three clubs.
		self.entries = {} # Dictionary used to keep track of the input fields.
		self.result_text = tk.StringVar(value="—")
		self.formula_text = tk.StringVar(value="")

		# Set up the visual style and create the interface.
		self.configure_styles()
		self.build_interface()
		self.update_fields()

	# The background styling function
	def configure_styles(self):
		self.root.configure(background="#0B1120")
		style = ttk.Style(self.root)
		style.theme_use("clam")

		style.configure("App.TFrame", background="#0B1120")
		style.configure("App.TLabel", background="#111827", foreground="#F8FAFC", font=("Segoe UI", 12))

		style.configure("Section.TLabelframe", background="#111827", foreground="#F8FAFC",
						bordercolor="#334155", relief="solid")
		style.configure("Section.TLabelframe.Label", background="#111827", foreground="#E2E8F0",
						font=("Segoe UI", 12, "bold"))

		style.configure("Result.TLabelframe", background="#172554", foreground="#F8FAFC",
						bordercolor="#2563EB", relief="solid", borderwidth=2)
		style.configure("Result.TLabelframe.Label", background="#172554", foreground="#DBEAFE",
						font=("Segoe UI", 12, "bold"))

		style.configure("App.TRadiobutton", background="#111827", foreground="#F8FAFC", font=("Segoe UI", 12))
		style.map("App.TRadiobutton",
				  background=[("active", "#1E293B")],
				  foreground=[("active", "#FFFFFF")])

		style.configure("App.TEntry", fieldbackground="#0F172A", foreground="#FFFFFF", insertcolor="#FFFFFF",
						bordercolor="#64748B", lightcolor="#64748B", darkcolor="#334155",
						font=("Segoe UI", 16), padding=(8, 6))
		style.map("App.TEntry",
				  bordercolor=[("focus", "#93C5FD"), ("active", "#94A3B8")],
				  lightcolor=[("focus", "#93C5FD"), ("active", "#94A3B8")],
				  darkcolor=[("focus", "#475569")])

		style.configure("Action.TButton", background="#2563EB", foreground="#FFFFFF",
						font=("Segoe UI", 12, "bold"), padding=(16, 9), borderwidth=0)
		style.map("Action.TButton",
				  background=[("active", "#1D4ED8"), ("pressed", "#1E40AF")],
				  foreground=[("disabled", "#CBD5E1")])

		style.configure("Secondary.TButton", background="#1E293B", foreground="#F8FAFC",
						font=("Segoe UI", 12), padding=(16, 9), borderwidth=0)
		style.map("Secondary.TButton",
				  background=[("active", "#334155"), ("pressed", "#475569")],
				  foreground=[("active", "#FFFFFF")])

		style.configure("ResultTitle.TLabel", background="#172554", foreground="#4ADE80",
						font=("Segoe UI", 11, "bold"))
		style.configure("ResultValue.TLabel", background="#172554", foreground="#F8FAFC",
						font=("Segoe UI", 26, "bold"))
		style.configure("Formula.TLabel", background="#172554", foreground="#CBD5E1", font=("Segoe UI", 12))

		style.configure("Chip.TLabel", background="#111827", foreground="#93C5FD",
						font=("Segoe UI", 10, "bold"))

	# The interface layout 
	def build_interface(self):
		header = tk.Frame(self.root, background="#172554", padx=24, pady=12)
		header.pack(fill="x")
		tk.Frame(header, background="#3B82F6", width=42, height=3).pack(anchor="w")
		tk.Label(header, text="INCLUSION-EXCLUSION PRINCIPLE", background="#172554",
				 foreground="#60A5FA", font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(6, 0))
		tk.Label(header, text="Club Membership Calculator", background="#172554",
				 foreground="#FFFFFF", font=("Segoe UI", 22, "bold")).pack(anchor="w", pady=(2, 0))
		tk.Label(header, text="Calculate the number of unique students when memberships overlap.",
				 background="#172554", foreground="#CBD5E1", font=("Segoe UI", 11)).pack(anchor="w", pady=(4, 0))

		main = ttk.Frame(self.root, padding=(20, 14), style="App.TFrame")
		main.pack(fill="both", expand=True)
		content = ttk.Frame(main, width=780, style="App.TFrame")
		content.pack(anchor="n", fill="x")

		mode_frame = ttk.LabelFrame(content, text="Number of clubs", padding=10, style="Section.TLabelframe")
		mode_frame.pack(fill="x", pady=(0, 10))
		ttk.Radiobutton(mode_frame, text="Two clubs", variable=self.mode, value="2 clubs",
						 command=self.update_fields, style="App.TRadiobutton").pack(side="left", padx=(0, 28))
		ttk.Radiobutton(mode_frame, text="Three clubs", variable=self.mode, value="3 clubs",
						 command=self.update_fields, style="App.TRadiobutton").pack(side="left")

		self.input_frame = ttk.LabelFrame(content, text="Membership counts", padding=(16, 12), # Input fields are rebuilt whenever the user changes
										   style="Section.TLabelframe")
		self.input_frame.pack(fill="x", pady=(0, 10))

		button_frame = ttk.Frame(content, style="App.TFrame")
		button_frame.pack(fill="x", pady=(0, 10))
		ttk.Button(button_frame, text="Calculate", command=self.calculate,
				   style="Action.TButton").pack(side="left")
		ttk.Button(button_frame, text="Clear", command=self.clear,
				   style="Secondary.TButton").pack(side="left", padx=10)

		result_frame = ttk.LabelFrame(content, text="Result", padding=12, style="Result.TLabelframe")
		result_frame.pack(fill="x")
		ttk.Label(result_frame, text="TOTAL UNIQUE STUDENTS", style="ResultTitle.TLabel").pack(anchor="w")
		ttk.Label(result_frame, textvariable=self.result_text, style="ResultValue.TLabel",
				  wraplength=680).pack(anchor="w", pady=(3, 0))
		ttk.Label(result_frame, textvariable=self.formula_text, style="Formula.TLabel",
				  wraplength=680).pack(anchor="w", pady=(6, 0))

	def update_fields(self):
		"""Rebuild the input fields based on the selected number of clubs."""
		for child in self.input_frame.winfo_children():
			child.destroy()
		self.entries.clear()

		club_fields = [("math", "Math Club"), ("science", "Science Club")]
		overlap_fields = [("math_science", "Math and Science overlap")]

		if self.mode.get() == "3 clubs":
			club_fields.append(("literature", "Literature Club"))
			overlap_fields.extend([
				("math_literature", "Math and Literature overlap"),
				("science_literature", "Science and Literature overlap"),
				("all_three", "All three clubs overlap"),
			])

		row = 0
		row = self.add_section_label("● CLUB TOTALS", row, top_pad=0)
		row = self.add_field_grid(club_fields, row)

		ttk.Separator(self.input_frame, orient="horizontal").grid(
			row=row, column=0, columnspan=4, sticky="ew", pady=(10, 0)
		)
		row += 1
		row = self.add_section_label("● OVERLAPS", row, top_pad=10)
		self.add_field_grid(overlap_fields, row)

		self.input_frame.columnconfigure(1, weight=1)
		self.input_frame.columnconfigure(3, weight=1)
		if club_fields:
			self.entries[club_fields[0][0]].focus_set()

	def add_section_label(self, text, row, top_pad):
		"""Place a small accent-colored section heading, returning the next free row."""
		ttk.Label(self.input_frame, text=text, style="Chip.TLabel").grid(
			row=row, column=0, columnspan=4, sticky="w", pady=(top_pad, 6)
		)
		return row + 1

	def add_field_grid(self, fields, start_row):
		"""Place a two-column grid of labeled entry fields, returning the next free row."""
		for index, (key, label) in enumerate(fields):
			row = start_row + index // 2
			column = (index % 2) * 2
			ttk.Label(self.input_frame, text=label, style="App.TLabel").grid(
				row=row, column=column, sticky="w", pady=4
			)
			entry = ttk.Entry(self.input_frame, width=11, style="App.TEntry", justify="center")
			entry.grid(row=row, column=column + 1, sticky="w", padx=(10, 24), pady=4)
			self.entries[key] = entry
		return start_row + (len(fields) + 1) // 2

	# Data handling 
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
				values["math_science"], values["math_literature"], values["science_literature"]
			):
				raise ValueError("The all-three intersection cannot exceed any pairwise intersection.")

			if values["math_science"] - values["all_three"] < 0:
				raise ValueError("Math ∩ Science only is negative; check Math ∩ Science and the all-three intersection.")
			if values["math_literature"] - values["all_three"] < 0:
				raise ValueError("Math ∩ Literature only is negative; check Math ∩ Literature and the all-three intersection.")
			if values["science_literature"] - values["all_three"] < 0:
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
				values["math"], values["science"], values["literature"],
				values["math_science"], values["math_literature"],
				values["science_literature"], values["all_three"],
			)
			if total < 0:
				raise ValueError("The calculated union of the three clubs cannot be negative.")

	# The calculative actions 

	def calculate(self):
		try:
			values = self.read_values()
			self.validate_values(values)
		except ValueError as error:
			messagebox.showerror("Check your inputs", str(error), parent=self.root)
			return

		if self.mode.get() == "2 clubs": # Validate the calculated total for two-club mode.
			total = count_two_sets(values["math"], values["science"], values["math_science"])
			formula = f"{values['math']} + {values['science']} - {values['math_science']} = {total}"
		else:
			total = count_three_sets(
				values["math"], values["science"], values["literature"],
				values["math_science"], values["math_literature"],
				values["science_literature"], values["all_three"],
			)
			formula = (
				f"{values['math']} + {values['science']} + {values['literature']} - "
				f"{values['math_science']} - {values['math_literature']} - "
				f"{values['science_literature']} + {values['all_three']} = {total}"
			)

		self.result_text.set(f"{total} students")
		self.formula_text.set(f"Inclusion-Exclusion: {formula}")

	def clear(self):
		for entry in self.entries.values():
			entry.delete(0, tk.END)
		self.result_text.set("—")
		self.formula_text.set("")

# The main program
def main():
	root = tk.Tk()
	InclusionExclusionApp(root)
	root.mainloop()
if __name__ == "__main__":
	main()
