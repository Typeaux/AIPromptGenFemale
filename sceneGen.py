import tkinter as tk
from tkinter import ttk, messagebox
import random
import json
import os

# Define your categories and their items
categories = {
    "Occupation": ["Athlete", "Nun", "Priest", "Shaman", "Cheerleader", "Engineer", "Explorer", "Gamer", "Scientist", "Librarian", "Artist", "Pilot", "Bounty Hunter", "Trail Guide", "Surgeon", "Trader", "Banker", "Biologist", "Oracle", "Potion Master", "Dragon Trainer", "Spell Weaver", "Knight", "Court Magician", "Treasure Hunter", "Beastmaster", "Guild Leader", "Diplomat to the Fae", "Sorceress", "Sky Pirate", "Necromancer", "Wizard", "Wandering Minstrel", "Elemental Shaman", "Shadow Assassin"],
    "Background": ["Fantasy World Background", "Cityscape Background", "Nature Setting Background", "Sci-Fi Universe Background", "Historical Era Background", "Underwater World Background", "Space Station Background", "Cyberpunk City Background", "Magical Forest Background", "Post-Apocalyptic Landscape Background", "Bedroom Background", "Downtown Background"],
    "Background Color": ["aqua background", "black background", "blue background", "brown background", "green background", "grey background", "orange background", "pink background", "purple background", "red background", "sepia background", "white background", "yellow background", "gradient background", "multicolored background", "rainbow background", "heaven condition", "two-tone background", "argyle background", "checkered background", "dotted background", "food-themed background", "grid background", "halftone background", "honeycomb background", "paw print background", "plaid background", "polka dot background", "simple background", "snowflake background", "spiral background", "strawberry background", "striped background", "sunburst background", "marble background", "abstract background", "animal background", "text background", "backlighting", "blending", "blurry background", "card background", "chibi inset", "drama layer", "fiery background", "flag background", "floral background", "fruit background", "heart background", "imageboard colors", "lace background", "mosaic background", "paneled background", "photo background", "projected inset", "sofmap background", "starry background", "transparent background"],
    "Camera/View Angle": ["dutch angle", "from above", "from behind", "from below", "from side", "sideways", "straight-on", "atmospheric perspective", "fisheye", "panorama", "perspective", "vanishing point", "face", "portrait", "upper body", "lower body", "cowboy shot", "feet out of frame", "full body", "wide shot", "very wide shot"],
    "Scene lighting": ["Bright Lighting", "Dim Lighting", "Natural Lighting", "Soft Lighting", "Warm Lighting", "Cool Lighting", "Spotlight", "Backlighting", "Candlelight"],
    "Age": ["Age 20", "Age 25", "Age 30"],
    "Character Pose": ["kneeling", "on one knee", "lying", "crossed legs", "on back", "on side", "on stomach", "sitting", "butterfly sitting", "crossed legs", "figure four sitting", "indian style", "hugging own legs", "lotus position", "seiza", "sitting on lap", "straddling", "thigh straddling", "upright straddle", "wariza", "yokozuwari", "standing", "balancing", "crossed legs", "legs apart", "standing on one leg"],
    "Hair Length": ["Short Hair", "Medium Hair", "Long Hair", "Pixie Hair", "Bob Hair", "Shoulder-length Hair", "Chin-length Hair", "Shaved Hair", "Waist-length Hair"],
    "Hair Style": ["bob cut", "inverted bob", "bowl cut", "buzz cut", "chonmage", "crew cut", "flattop", "okappa", "pixie cut", "undercut", "flipped hair", "wolf cut", "cornrows", "dreadlocks", "hime cut", "mullet", "bow-shaped hair", "braid", "braided bangs", "front braid", "side braid", "french braid", "crown braid", "single braid", "multiple braids", "twin braids", "low twin braids", "tri braids", "quad braids", "flower-shaped hair", "hair bun", "braided bun", "single hair bun", "double bun", "cone hair bun", "doughnut hair bun", "heart hair bun", "triple bun", "cone hair bun", "hair rings", "single hair ring", "half updo", "one side up", "two side up", "low-braided long hair", "low-tied long hair", "mizura", "multi-tied hair", "nihongami", "ponytail", "folded ponytail", "front ponytail", "high ponytail", "short ponytail", "side ponytail", "split ponytail", "star-shaped hair", "topknot", "twintails", "low twintails", "short twintails", "uneven twintails", "tri tails", "quad tails", "quin tails", "twisted hair", "afro", "huge afro", "beehive hairdo", "crested hair", "pompadour", "quiff", "shouten pegasus mix mori", "curly hair", "drill hair", "twin drills", "tri drills", "hair flaps", "messy hair", "pointy hair", "ringlets", "spiked hair", "straight hair", "wavy hair", "arched bangs", "asymmetrical bangs", "bangs pinned back", "blunt bangs", "crossed bangs", "choppy bangs", "diagonal bangs", "dyed bangs", "fanged bangs", "hair over eyes", "hair over one eye", "long bangs", "parted bangs", "curtained hair", "wispy bangs", "short bangs", "swept bangs", "hair between eyes", "single hair intake", "asymmetrical sidelocks", "drill sidelocks", "low-tied sidelocks", "sidelocks tied back", "single sidelock", "widow's peak", "heart ahoge", "huge ahoge", "heart antenna hair", "comb over", "hair pulled back", "hair slicked back", "mohawk", "oseledets"],
    "Hair Color": ["aqua hair", "black hair", "blonde hair", "blue hair", "light blue hair", "dark blue hair", "brown hair", "light brown hair", "green hair", "dark green hair", "light green hair", "grey hair", "orange hair", "pink hair", "purple hair", "light purple hair", "red hair", "white hair", "colored inner hair", "colored tips", "roots", "gradient hair", "print hair", "rainbow hair", "split-color hair", "spotted hair", "streaked hair", "two-tone hair"],
    "Eye Shape": ["Round Eyes", "Almond Eyes", "Cat-like Eyes", "Upturned Eyes", "Downturned Eyes", "Hooded Eyes", "Monolid Eyes", "Deep-set Eyes", "Wide-set Eyes", "Close-set Eyes"],
    "Eye Color": ["Blue Eyes", "Green Eyes", "Brown Eyes", "Hazel Eyes", "Gray Eyes", "Amber Eyes", "Violet Eyes", "Red Eyes", "Pink Eyes", "Turquoise Eyes"],
    "Face Shape": ["Round Face", "Oval Face", "Square Face", "Diamond Face", "Rectangular Face", "Triangular Face", "Long Face", "Circular Face"],
    "Lip Shape": ["Full Lips", "Thin Lips", "Bow-shaped Lips", "Heart-shaped Lips", "Round Lips", "Wide Lips", "Cupid's Bow Lips", "Flat Lips", "Defined Lips", "Plump Lips"],
    "Lip Color": ["Aqua lips", "Black lips", "Blue lips", "Grey lips", "Green lips", "Orange lips", "Pink lips", "Purple lips", "Red lips", "Shiny lips", "Yellow lips"],
    "Lip Action": ["Closed mouth", "Licking lips", "Biting own lip", "Open mouth", "Parted lips", "Puckered lips", "Pursed lips", "Spread lips"],
    "Skin Tone": ["Fair Skin", "Tan Skin", "Dark Skin", "Pale Skin", "Olive Skin", "Golden Skin", "Caramel Skin", "Ebony Skin", "Ivory Skin", "Rosy Skin"],
    "Body Type": ["Slim Body", "Curvy Body", "Athletic Body", "Petite Body", "Tall Body", "Muscular Body", "Hourglass Body", "Voluptuous Body"],
    "Bust Size": ["Small Bust", "Medium Bust", "Large Bust", "Flat Bust", "Full Bust", "Average Bust", "Tiny Bust", "Well-endowed Bust", "Modest Bust", "Plentiful Bust"],
    "Waist Size": ["Slim Waist", "Average Waist", "Hourglass Waist", "Narrow Waist", "Curvy Waist", "Thick Waist", "Tapered Waist", "Defined Waist", "Tiny Waist", "Broad Waist"],
    "Hip Size": ["Narrow Hips", "Average Hips", "Wide Hips", "Curvy Hips", "Slim Hips", "Full Hips", "Tapered Hips", "Defined Hips", "Tiny Hips", "Voluptuous Hips"],
    "Facial Expression": ["Smiling Expression", "Serious Expression", "Shy Expression", "Confident Expression", "Happy Expression", "Sad Expression", "Angry Expression", "Surprised Expression", "Neutral Expression", "Mischievous Expression"],
    "Mood": ["Happy Mood", "Sad Mood", "Excited Mood", "Anxious Mood", "Relaxed Mood", "Angry Mood", "Playful Mood", "Serene Mood", "Confused Mood", "Mischievous Mood"],
    "Clothing Style": ["School Uniform", "Casual Wear", "Formal Attire", "Gothic Outfit", "Lolita Fashion", "Sportswear", "Kimono", "Swimsuit", "Vintage Clothing", "Fantasy Armor", "Steampunk Ensemble", "Bohemian Attire", "Retro Fashion", "Punk Rock Outfit", "Business Suit", "Cosplay Costume", "Ethnic Attire", "Military Uniform", "Fairy Tale Dress", "Futuristic Outfit"],
    "Clothing Color": ["Black Outfit", "White Outfit", "Red Outfit", "Blue Outfit", "Green Outfit", "Pink Outfit", "Purple Outfit", "Yellow Outfit", "Orange Outfit", "Gray Outfit"],
    "Clothing Details": ["Frills and Bows", "Lace and Ribbons", "Sequins and Beads", "Embroidery and Appliqué", "Ruffles and Tassels", "Prints and Patterns", "Pleats and Drapes", "Buttons and Zippers", "Belts and Buckles", "Chains and Studs"],
    "Clothing Accessories": ["Glasses and Sunglasses", "Headbands and Hair Clips", "Scarves and Shawls", "Hats and Caps", "Gloves and Mittens", "Belts and Suspenders", "Jewelry and Watches", "Bags and Purses", "Socks and Stockings", "Shoes and Boots"],
}

theme_value = True

def theme_change():
    global theme_value
    if theme_value:
        root.config(bg="#26242f")
        button_frame.config(bg="#26242f")
        preset_frame.config(bg="#26242f")
        scene_frame.config(style="Dark.TLabelframe")
        hair_frame.config(style="Dark.TLabelframe")
        face_frame.config(style="Dark.TLabelframe")
        clothing_frame.config(style="Dark.TLabelframe")
        body_frame.config(style="Dark.TLabelframe")
        style.configure("TCombobox", fieldbackground="#26242f", background="#26242f", foreground="black")
        style.configure("TLabel", background="#26242f", foreground="white")
        style.configure("TCheckbutton", background="#26242f", foreground="white")
        style.configure("TEntry", fieldbackground="#26242f", foreground="white", insertcolor="white")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Text):
                widget.config(bg="#26242f", fg="white", insertbackground="white")
        theme_value = False
    else:
        root.config(bg="white")
        button_frame.config(bg="white")
        preset_frame.config(bg="white")
        scene_frame.config(style="Light.TLabelframe")
        hair_frame.config(style="Light.TLabelframe")
        face_frame.config(style="Light.TLabelframe")
        clothing_frame.config(style="Light.TLabelframe")
        body_frame.config(style="Light.TLabelframe")
        style.configure("TCombobox", fieldbackground="white", background="white", foreground="black")
        style.configure("TLabel", background="white", foreground="black")
        style.configure("TCheckbutton", background="white", foreground="black")
        style.configure("TEntry", fieldbackground="white", foreground="black", insertcolor="black")
        for widget in root.winfo_children():
            if isinstance(widget, tk.Text):
                widget.config(bg="white", fg="black", insertbackground="black")
        theme_value = True

def generate_prompt():
    selected_categories = {category: (var.get(), disable_vars[category].get()) for category, var in category_vars.items()}
    prompt = []
    for category, (value, enabled) in selected_categories.items():
        if not enabled:
            continue  # Skip disabled categories
        if value:
            prompt.append(value)
        else:
            prompt.append(random.choice(categories[category]))
    prompt_text = ', '.join(prompt)
    prompt_display.config(state=tk.NORMAL)
    prompt_display.delete('1.0', tk.END)
    prompt_display.insert(tk.END, prompt_text)
    prompt_display.config(state=tk.DISABLED)

def copy_to_clipboard():
    prompt_text = prompt_display.get('1.0', tk.END)
    root.clipboard_clear()
    root.clipboard_append(prompt_text.strip())

def reset_defaults():
    for category, var in category_vars.items():
        var.set("")  # Reset dropdowns
    for disable_var in disable_vars.values():
        disable_var.set(True)  # Check checkboxes
    prompt_display.config(state=tk.NORMAL)
    prompt_display.delete('1.0', tk.END)
    prompt_display.config(state=tk.DISABLED)

def save_preset():
    preset_name = preset_entry.get().strip()
    if not preset_name:
        messagebox.showerror("Error", "Preset name cannot be empty")
        return

    preset_data = {
        "selected_categories": {category: var.get() for category, var in category_vars.items()},
        "disabled_categories": {category: disable_var.get() for category, disable_var in disable_vars.items()},
        "prompt": prompt_display.get('1.0', tk.END).strip()
    }

    # Check if the file exists and create it if it doesn't
    if not os.path.exists("presets.json"):
        with open("presets.json", "w") as file:
            json.dump({}, file)

    # Open the file and update it
    with open("presets.json", "r+") as file:
        try:
            presets = json.load(file)
        except json.JSONDecodeError:
            presets = {}
        presets[preset_name] = preset_data
        file.seek(0)
        json.dump(presets, file, indent=4)

    update_presets_list()
    preset_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"Preset '{preset_name}' saved successfully")

def load_preset():
    preset_name = presets_listbox.get(tk.ACTIVE)
    if not preset_name:
        messagebox.showerror("Error", "No preset selected")
        return

    with open("presets.json", "r") as file:
        presets = json.load(file)
        preset_data = presets.get(preset_name, {})

    for category, value in preset_data.get("selected_categories", {}).items():
        category_vars[category].set(value)
    for category, value in preset_data.get("disabled_categories", {}).items():
        disable_vars[category].set(value)
    prompt_display.config(state=tk.NORMAL)
    prompt_display.delete('1.0', tk.END)
    prompt_display.insert(tk.END, preset_data.get("prompt", ""))
    prompt_display.config(state=tk.DISABLED)
    messagebox.showinfo("Success", f"Preset '{preset_name}' loaded successfully")

def update_presets_list():
    try:
        with open("presets.json", "r") as file:
            presets = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        presets = {}

    presets_listbox.delete(0, tk.END)
    for preset_name in presets.keys():
        presets_listbox.insert(tk.END, preset_name)

def fill_dropdowns_from_prompt():
    prompt_text = prompt_display.get('1.0', tk.END).strip()
    prompt_values = [value.strip() for value in prompt_text.split(',')]

    for category, items in categories.items():
        for value in prompt_values:
            if value in items:
                category_vars[category].set(value)
                break

# Initialize category variables
category_vars = {}
disable_vars = {}

# Set up the GUI
root = tk.Tk()
root.title("Character Generator")
root.geometry("1000x700")  # Increased window size
root.minsize(1000, 1100)  # Set minimum window size
root.config(bg="white")

# Configure the grid
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)
root.grid_columnconfigure(6, weight=1)
root.grid_columnconfigure(7, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

# Add style for transparent Combobox
style = ttk.Style()
style.configure("TCombobox", fieldbackground="white", background="white")
style.configure("TLabel", background="white", foreground="black")
style.configure("TCheckbutton", background="white", foreground="black")
style.configure("TEntry", fieldbackground="white", foreground="black", insertcolor="black")

# Define styles for light and dark themes
style.configure("Light.TLabelframe", background="white", foreground="black")
style.configure("Light.TLabelframe.Label", background="white", foreground="black")
style.configure("Dark.TLabelframe", background="#26242f", foreground="white")
style.configure("Dark.TLabelframe.Label", background="#26242f", foreground="white")

# Grouping categories
def create_group(frame, categories_list):
    for i, category in enumerate(categories_list):
        label = ttk.Label(frame, text=category)
        label.grid(row=i, column=0, sticky="e", padx=5, pady=5)
        var = tk.StringVar(root)
        var.set("")  # Set default value to empty string
        dropdown = ttk.Combobox(frame, textvariable=var, values=[""] + categories[category], width=30, style="TCombobox")
        dropdown.grid(row=i, column=1, sticky="ew", padx=5, pady=5)
        category_vars[category] = var
        disable_var = tk.BooleanVar(root, value=True)  # Set default value to True
        checkbox = ttk.Checkbutton(frame, text="Enable/Disable", variable=disable_var, onvalue=True, offvalue=False)
        checkbox.grid(row=i, column=2, sticky="w", padx=5, pady=5)
        disable_vars[category] = disable_var

# Body Group
body_frame = ttk.LabelFrame(root, text="Body", padding=(10, 5), style="Light.TLabelframe")
body_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
body_categories = ["Body Type", "Bust Size", "Waist Size", "Hip Size", "Skin Tone", "Character Pose"]
create_group(body_frame, body_categories)

# Hair Group
hair_frame = ttk.LabelFrame(root, text="Hair", padding=(10, 5), style="Light.TLabelframe")
hair_frame.grid(row=0, column=4, columnspan=4, padx=10, pady=10, sticky="nsew")
hair_categories = ["Hair Length", "Hair Style", "Hair Color"]
create_group(hair_frame, hair_categories)

# Face Group
face_frame = ttk.LabelFrame(root, text="Face", padding=(10, 5), style="Light.TLabelframe")
face_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
face_categories = ["Eye Shape", "Eye Color", "Face Shape", "Lip Shape", "Lip Color", "Lip Action", "Facial Expression", "Mood"]
create_group(face_frame, face_categories)

# Clothing Group
clothing_frame = ttk.LabelFrame(root, text="Clothing", padding=(10, 5), style="Light.TLabelframe")
clothing_frame.grid(row=1, column=4, columnspan=4, padx=10, pady=10, sticky="nsew")
clothing_categories = ["Clothing Style", "Clothing Color", "Clothing Details", "Clothing Accessories","Occupation", ]
create_group(clothing_frame, clothing_categories)

# Scene Group
scene_frame = ttk.LabelFrame(root, text="Scene", padding=(10, 5), style="Light.TLabelframe")
scene_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
other_categories = ["Background", "Background Color", "Camera/View Angle", "Scene lighting"]
create_group(scene_frame, other_categories)

# Add a text widget to display the prompt
prompt_display = tk.Text(root, height=10, width=80, bg="white", wrap=tk.WORD)  # Enabled word wrapping
prompt_display.config(state=tk.DISABLED)
prompt_display.grid(row=3, columnspan=8, padx=5, pady=5, sticky="nsew")  # Added padding and made expandable

# Add a frame for presets and place it above the button frame
preset_frame = tk.Frame(root, bg="white")
preset_frame.grid(row=4, columnspan=8, pady=10, sticky="ew")  # Added padding and made expandable

# Entry to input preset name
preset_entry = ttk.Entry(preset_frame, width=30, style="TEntry")
preset_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# Button to save preset
save_preset_button = tk.Button(preset_frame, text="Save Preset", command=save_preset)
save_preset_button.grid(row=0, column=1, padx=5, pady=5)

# Listbox to display saved presets
presets_listbox = tk.Listbox(preset_frame, width=40, height=5)
presets_listbox.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

# Button to load selected preset
load_preset_button = tk.Button(preset_frame, text="Load Preset", command=load_preset)
load_preset_button.grid(row=0, column=3, padx=5, pady=5)

# Update the presets list on startup
update_presets_list()

# Add a frame to contain the buttons and keep it at the bottom
button_frame = tk.Frame(root, bg="white")
button_frame.grid(row=5, columnspan=8, padx=5, pady=5, sticky="ew")  # Added padding and made expandable

# Add a button to randomize the prompt
generate_button = tk.Button(button_frame, text="Randomize", command=generate_prompt)
generate_button.grid(row=0, column=0, padx=10)

# Add a button to fill dropdowns from the prompt
fill_dropdowns_button = tk.Button(button_frame, text="Fill from Prompt", command=fill_dropdowns_from_prompt)
fill_dropdowns_button.grid(row=0, column=1, padx=10)

# Add a copy to clipboard button
copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=0, column=2, padx=10)

# Add a reset button
reset_button = tk.Button(button_frame, text="Reset", command=reset_defaults)
reset_button.grid(row=0, column=3, padx=10)

# Add dark theme toggle to dark
theme_button = tk.Button(button_frame, text="Change light/dark", command=theme_change)
theme_button.grid(row=0, column=4, padx=10)

# Start the GUI
root.mainloop()
