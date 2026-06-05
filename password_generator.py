import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        
        # Title Label
        title_label = tk.Label(
            root,
            text="Password Generator",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=20)
        
        # Frame for input
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10)
        
        # Length Label
        length_label = tk.Label(
            input_frame,
            text="Password Length:",
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#333333"
        )
        length_label.pack(side=tk.LEFT, padx=5)
        
        # Length Entry
        self.length_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=10,
            border=2
        )
        self.length_entry.pack(side=tk.LEFT, padx=5)
        self.length_entry.insert(0, "12")  # Default value
        
        # Generate Button
        self.generate_btn = tk.Button(
            root,
            text="Generate Password",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.generate_password
        )
        self.generate_btn.pack(pady=15)
        
        # Frame for password display
        display_frame = tk.Frame(root, bg="#f0f0f0")
        display_frame.pack(pady=15)
        
        # Password Label
        password_label = tk.Label(
            display_frame,
            text="Generated Password:",
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#333333"
        )
        password_label.pack(anchor=tk.W, padx=10)
        
        # Password Display (with border)
        self.password_display = tk.Entry(
            root,
            font=("Arial", 12, "bold"),
            width=40,
            border=2,
            state=tk.DISABLED,
            disabledbackground="#ffffff",
            disabledforeground="#000000"
        )
        self.password_display.pack(pady=5, padx=20)
        
        # Frame for buttons
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=15)
        
        # Copy Button
        self.copy_btn = tk.Button(
            button_frame,
            text="Copy to Clipboard",
            font=("Arial", 10, "bold"),
            bg="#2196F3",
            fg="white",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.copy_to_clipboard,
            state=tk.DISABLED
        )
        self.copy_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear Button
        self.clear_btn = tk.Button(
            button_frame,
            text="Clear",
            font=("Arial", 10, "bold"),
            bg="#f44336",
            fg="white",
            padx=15,
            pady=8,
            cursor="hand2",
            command=self.clear_fields
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
    
    def generate_password(self):
        try:
            # Get password length from entry
            length = int(self.length_entry.get())
            
            # Validate length
            if length < 4:
                messagebox.showwarning(
                    "Invalid Length",
                    "Password length must be at least 4 characters!"
                )
                return
            
            if length > 128:
                messagebox.showwarning(
                    "Invalid Length",
                    "Password length cannot exceed 128 characters!"
                )
                return
            
            # Define character sets
            lowercase = string.ascii_lowercase
            uppercase = string.ascii_uppercase
            digits = string.digits
            special_chars = string.punctuation
            
            # Combine all characters
            all_chars = lowercase + uppercase + digits + special_chars
            
            # Ensure password has at least one of each type
            password_chars = [
                random.choice(lowercase),
                random.choice(uppercase),
                random.choice(digits),
                random.choice(special_chars)
            ]
            
            # Fill remaining length with random characters
            for _ in range(length - 4):
                password_chars.append(random.choice(all_chars))
            
            # Shuffle to avoid predictable pattern
            random.shuffle(password_chars)
            
            # Join to create final password
            password = ''.join(password_chars)
            
            # Display password
            self.password_display.config(state=tk.NORMAL)
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state=tk.DISABLED)
            
            # Enable copy button
            self.copy_btn.config(state=tk.NORMAL)
            
            messagebox.showinfo(
                "Success",
                "Password generated successfully!"
            )
        
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number for password length!"
            )
    
    def copy_to_clipboard(self):
        self.password_display.config(state=tk.NORMAL)
        password = self.password_display.get()
        self.password_display.config(state=tk.DISABLED)
        
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo(
                "Success",
                "Password copied to clipboard!"
            )
        else:
            messagebox.showwarning(
                "Empty Password",
                "No password to copy!"
            )
    
    def clear_fields(self):
        self.length_entry.delete(0, tk.END)
        self.length_entry.insert(0, "12")
        self.password_display.config(state=tk.NORMAL)
        self.password_display.delete(0, tk.END)
        self.password_display.config(state=tk.DISABLED)
        self.copy_btn.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
