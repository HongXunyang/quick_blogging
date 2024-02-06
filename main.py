import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Initialize the main window
root = tk.Tk()
root.title('Blog Updater')

# Time
current_time = datetime.now().strftime("%d-%b %H:%M")

# Define the list of .html files
html_files = {
    'STO Blog' : '_research/beamtime-2024-02-diamond-blogging.md', 
    'Random Blog' :'_notes/blog-and-giberish.md'
  }  # Add your file names here

# Create a dropdown menu for .html files
selected_file = tk.StringVar()
file_selector = ttk.Combobox(root, textvariable=selected_file, values=list(html_files.keys()), state='readonly', font=('Helvetica', 14), width=20)
file_selector.pack(padx=20, pady=20)
file_selector.current(0)  # Optionally set a default value

# Add enlarged text input field
entry = tk.Entry(root,width=50, font=('Helvetica', 16))
entry.pack(padx=20, pady=20)



html_folder_path = 'C:/Users/51910/OneDrive/Blog_Jeklly/Hongxys-Jeklly-Blog/'


def submit_action():
    # Get the input text
    input_text = entry.get()
    input_text = current_time + ": <b>" + input_text + "</b>"
    # Get the selected alias from the dropdown and the corresponding .html file
    selected_alias = selected_file.get()
    selected_html_file = html_folder_path + html_files[selected_alias]

    # Ensure that the user has selected a file
    if not selected_html_file:
        messagebox.showerror("Error", "Please select an HTML file.")
        return

    try:
        # Read the current contents of the selected .html file
        with open(selected_html_file, 'r') as file:
            blog_contents = file.read()

        # Find the position of the second '---'
        first_delimiter_pos = blog_contents.find('---')
        second_delimiter_pos = blog_contents.find('---', first_delimiter_pos + 3)
        
        # Ensure that two '---' delimiters are found
        if first_delimiter_pos == -1 or second_delimiter_pos == -1:
            messagebox.showerror("Error", f"Could not find two '---' delimiters in {selected_html_file}.")
            return

        # Insert the new text after the second '---', with '\n' above and below the text
        insertion_point = second_delimiter_pos + 3  # 3 characters for the length of '---'
        new_blog_contents = blog_contents[:insertion_point] + '\n' + input_text + '\n' + blog_contents[insertion_point:]

        # Write the new blog contents back to the selected .html file
        with open(selected_html_file, 'w') as file:
            file.write(new_blog_contents)

        # Show a message box upon success
        entry.delete(0, 'end')
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



# Add enlarged Submit button
submit_button = tk.Button(root, text='Submit', command=submit_action, height=2, width=20, font=('Helvetica', 14))
submit_button.pack(pady=20)
"""
def run_script_action():
    try:
        # Run the fast_push.sh script
        os.system("C:/Users/51910/OneDrive/Blog_Jeklly/Hongxys-Jeklly-Blog/fast_push.sh")
        messagebox.showinfo("Success", "Script executed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Add enlarged Run Script button
run_script_button = tk.Button(root, text='Run Script', command=run_script_action, height=2, width=20, font=('Helvetica', 14))
run_script_button.pack(pady=20)
"""
# Start the main loop
root.mainloop()
