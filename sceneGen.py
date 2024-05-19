import tkinter as tk
from tkinter import ttk
import random

# Define your categories and their items
categories = {
    "Occupation": ["Athelete", "Nun", "Priest", "Shaman", "Cybersecurity Specialist", "Robotic Engineer", "Space Explorer", "Geneticist", "AI Ethicist", "Drone Pilot", "Virtual Reality Game Designer", "Quantum Computer Programmer", "Environmental Scientist", "Digital Artist", "Mecha Pilot", "Bounty Hunter", "Starship Mechanic", "Planetary Geologist", "Cybernetic Surgeon", "Interstellar Trader", "Cryptocurrency Broker", "Anti-Gravity Architect", "Holovid Producer", "Astrobiologist", "Terraforming Specialist", "Mystic Oracle", "Potion Master", "Dragon Trainer", "Spell Weaver", "Knight-Errant", "Court Magician", "Treasure Hunter", "Beastmaster", "Guild Leader", "Diplomat to the Fae", "Rune Engraver", "Sky Pirate", "Necromancer", "Crystal Harvester", "Wandering Minstrel", "Elemental Shaman", "Shadow Assassin", "Arcane Librarian", "Time Rift Monitor"],
    "Background": ["Fantasy World Background", "Cityscape Background", "Nature Setting Background", "Sci-Fi Universe Background", "Historical Era Background", "Underwater World Background", "Space Station Background", "Cyberpunk City Background", "Magical Forest Background", "Post-Apocalyptic Landscape Background"],
    "Background Color": ["aqua background", "black background", "blue background", "brown background", "green background", "grey background", "orange background", "pink background", "purple background", "red background", "sepia background", "white background", "yellow background", "gradient background", "multicolored background", "rainbow background", "heaven condition", "two-tone background", "argyle background", "checkered background", "dotted background", "food-themed background", "grid background", "halftone background", "honeycomb background", "paw print background", "plaid background", "polka dot background", "simple background", "snowflake background", "spiral background", "strawberry background", "striped background", "sunburst background", "marble background", "abstract background", "animal background", "text background", "backlighting", "blending", "blurry background", "card background", "chibi inset", "drama layer", "fiery background", "flag background", "floral background", "fruit background", "heart background", "imageboard colors", "lace background", "mosaic background", "paneled background", "photo background", "projected inset", "sofmap background", "starry background", "transparent background", "zoom layer"],
    "Camera/View Angle" : ["dutch angle", "from above", "from behind", "from below", "from side", "sideways", "straight-on", "atmospheric perspective", "fisheye", "panorama", "perspective", "vanishing point", "face", "portrait", "upper body", "lower body", "cowboy shot", "feet out of frame", "full body", "wide shot", "very wide shot"],
    "Scene lighting": ["Bright Lighting", "Dim Lighting", "Natural Lighting", "Soft Lighting", "Warm Lighting", "Cool Lighting", "Spotlight", "Backlighting", "Candlelight"],
    "Age": ["Age 20", "Age 25", "Age 30"],
    "Character Pose": ["kneeling","on one knee","lying","crossed legs","fetal position","on back","on side","on stomach","sitting","butterfly sitting","crossed legs","figure four sitting","indian style","hugging own legs","lotus position","seiza","sitting on lap","sitting on person","straddling","thigh straddling","upright straddle","wariza","yokozuwari","standing","balancing","crossed legs","legs apart","standing on one leg"],
    "Hair Length": ["Short Hair", "Medium Hair", "Long Hair", "Pixie Hair", "Bob Hair", "Shoulder-length Hair", "Chin-length Hair", "Shaved Hair", "Bald", "Waist-length Hair"],
    "Hair Style": ["bob cut", "inverted bob", "bowl cut", "buzz cut", "chonmage", "crew cut", "flattop", "okappa", "pixie cut", "undercut", "flipped hair", "wolf cut", "cornrows", "dreadlocks", "hime cut", "mullet", "bow-shaped hair", "braid", "braided bangs", "front braid", "side braid", "french braid", "crown braid", "single braid", "multiple braids", "twin braids", "low twin braids", "tri braids", "quad braids", "flower-shaped hair", "hair bun", "braided bun", "single hair bun", "double bun", "cone hair bun", "doughnut hair bun", "heart hair bun", "triple bun", "cone hair bun", "hair rings", "single hair ring", "half updo", "one side up", "two side up", "low-braided long hair", "low-tied long hair", "mizura", "multi-tied hair", "nihongami", "ponytail", "folded ponytail", "front ponytail", "high ponytail", "short ponytail", "side ponytail", "split ponytail", "star-shaped hair", "topknot", "twintails", "low twintails", "short twintails", "uneven twintails", "tri tails", "quad tails", "quin tails", "twisted hair", "afro", "huge afro", "beehive hairdo", "crested hair", "pompadour", "quiff", "shouten pegasus mix mori", "curly hair", "drill hair", "twin drills", "tri drills", "hair flaps", "messy hair", "pointy hair", "ringlets", "spiked hair", "straight hair", "wavy hair", "arched bangs", "asymmetrical bangs", "bangs pinned back", "blunt bangs", "crossed bangs", "choppy bangs", "diagonal bangs", "dyed bangs", "fanged bangs", "hair over eyes", "hair over one eye", "long bangs", "parted bangs", "curtained hair", "wispy bangs", "short bangs", "swept bangs", "hair between eyes", "single hair intake", "asymmetrical sidelocks", "drill sidelocks", "low-tied sidelocks", "sidelocks tied back", "single sidelock", "widow's peak", "heart ahoge", "huge ahoge", "heart antenna hair", "comb over", "hair pulled back", "hair slicked back", "mohawk", "oseledets"],
    "Hair Color": ["aqua hair", "black hair", "blonde hair", "blue hair", "light blue hair", "dark blue hair", "brown hair", "light brown hair", "green hair", "dark green hair", "light green hair", "grey hair", "orange hair", "pink hair", "purple hair", "light purple hair", "red hair", "white hair","colored inner hair", "colored tips", "roots", "gradient hair", "print hair", "rainbow hair", "split-color hair", "spotted hair", "streaked hair", "two-tone hair"],
    "Eye Shape": ["Round Eyes", "Almond Eyes", "Cat-like Eyes", "Upturned Eyes", "Downturned Eyes", "Hooded Eyes", "Monolid Eyes", "Deep-set Eyes", "Wide-set Eyes", "Close-set Eyes"],
    "Eye Color": ["Blue Eyes", "Green Eyes", "Brown Eyes", "Hazel Eyes", "Gray Eyes", "Amber Eyes", "Violet Eyes", "Red Eyes", "Pink Eyes", "Turquoise Eyes"],
    "Face Shape": ["Round Face", "Oval Face", "Square Face", "Heart-shaped Face", "Diamond Face", "Rectangular Face", "Triangular Face", "Pear-shaped Face", "Long Face", "Circular Face"],
    "Nose Shape": ["Button Nose", "Pointed Nose", "Upturned Nose", "Straight Nose", "Roman Nose", "Aquiline Nose", "Snub Nose", "Hawk Nose", "Rounded Nose", "Fleshy Nose"],
    "Lip Shape": ["Full Lips", "Thin Lips", "Bow-shaped Lips", "Heart-shaped Lips", "Round Lips", "Wide Lips", "Cupid's Bow Lips", "Flat Lips", "Defined Lips", "Plump Lips"],
    "Lip Color": ["Aqua lips", "Black lips", "Blue lips", "Grey lips", "Green lips", "Orange lips", "Pink lips", "Purple lips", "Red lips", "Shiny lips", "Yellow lips"],
    "Lip Action":["Closed mouth", "Licking lips", "Biting own lip", "Open mouth", "Parted lips", "Puckered lips", "Pursed lips", "Spread lips"],
    "Skin Tone": ["Fair Skin", "Tan Skin", "Dark Skin", "Pale Skin", "Olive Skin", "Golden Skin", "Caramel Skin", "Ebony Skin", "Ivory Skin", "Rosy Skin"],
    "Body Type": ["Slim Body", "Curvy Body", "Athletic Body", "Petite Body", "Tall Body", "Muscular Body", "Hourglass Body", "Pear-shaped Body", "Apple-shaped Body", "Voluptuous Body"],
    "Bust Size": ["Small Bust", "Medium Bust", "Large Bust", "Flat Bust", "Full Bust", "Average Bust", "Tiny Bust", "Well-endowed Bust", "Modest Bust", "Plentiful Bust"],
    "Waist Size": ["Slim Waist", "Average Waist", "Hourglass Waist", "Narrow Waist", "Curvy Waist", "Thick Waist", "Tapered Waist", "Defined Waist", "Tiny Waist", "Broad Waist"],
    "Hip Size": ["Narrow Hips", "Average Hips", "Wide Hips", "Curvy Hips", "Slim Hips", "Full Hips", "Tapered Hips", "Defined Hips", "Tiny Hips", "Voluptuous Hips"],
    "Facial Expression": ["Smiling Expression", "Serious Expression", "Shy Expression", "Confident Expression", "Happy Expression", "Sad Expression", "Angry Expression", "Surprised Expression", "Neutral Expression", "Mischievous Expression"],
    "Mood": ["Happy Mood", "Sad Mood", "Excited Mood", "Anxious Mood", "Relaxed Mood", "Angry Mood", "Playful Mood", "Serene Mood", "Confused Mood", "Mischievous Mood"],
    "Personality": ["Sweet Personality Trait", "Sassy Personality Trait", "Shy Personality Trait", "Confident Personality Trait", "Adventurous Personality Trait", "Caring Personality Trait", "Intellectual Personality Trait", "Energetic Personality Trait", "Gentle Personality Trait", "Fiery Personality Trait"],
    "Clothing Style": ["School Uniform", "Casual Wear", "Formal Attire", "Gothic Outfit", "Lolita Fashion", "Sportswear", "Kimono", "Swimsuit", "Vintage Clothing", "Fantasy Armor", "Steampunk Ensemble", "Bohemian Attire", "Retro Fashion", "Punk Rock Outfit", "Business Suit", "Cosplay Costume", "Ethnic Attire", "Military Uniform", "Fairy Tale Dress", "Futuristic Outfit"],
    "Clothing Color": ["Black Outfit", "White Outfit", "Red Outfit", "Blue Outfit", "Green Outfit", "Pink Outfit", "Purple Outfit", "Yellow Outfit", "Orange Outfit", "Gray Outfit"],
    "Clothing Details": ["Frills and Bows", "Lace and Ribbons", "Sequins and Beads", "Embroidery and Appliqué", "Ruffles and Tassels", "Prints and Patterns", "Pleats and Drapes", "Buttons and Zippers", "Belts and Buckles", "Chains and Studs"],
    "Clothing Accessories": ["Glasses and Sunglasses", "Headbands and Hair Clips", "Scarves and Shawls", "Hats and Caps", "Gloves and Mittens", "Belts and Suspenders", "Jewelry and Watches", "Bags and Purses", "Socks and Stockings", "Shoes and Boots"],
}

theme_value = True
def theme_change():
    global theme_value
    if theme_value == True:
        root.config(bg="#26242f")
        theme_value = False
    else:
        root.config(bg="white")
        theme_value = True

def generate_prompt():
    selected_categories = {category: (var.get(), disable_vars[category].get()) for category, var in category_vars.items()}
    prompt = []
    for category, (value, disabled) in selected_categories.items():
        if disabled:
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
        disable_var.set(False)  # Uncheck checkboxes
    prompt_display.config(state=tk.NORMAL)
    prompt_display.delete('1.0', tk.END)
    prompt_display.config(state=tk.DISABLED)

# Set up the GUI
root = tk.Tk()
root.title("Character Generator")
root.geometry("840x565")
root.config(bg="white")

# Add dropdown menus with checkboxes to disable categories
category_vars = {}
disable_vars = {}
for i, (category, items) in enumerate(categories.items()):
    col = i % 2  # Column number (0 or 1)
    row = i // 2  # Row number
    label = ttk.Label(root, text=category)
    label.grid(row=row, column=col * 4, sticky="e")
    var = tk.StringVar(root)
    var.set("")  # Set default value to empty string
    dropdown = ttk.Combobox(root, textvariable=var, values=[""] + items, width=30)
    dropdown.grid(row=row, column=col * 4 + 1, sticky="w")
    category_vars[category] = var
    disable_var = tk.BooleanVar(root, value=False)
    checkbox = tk.Checkbutton(root, text="Disable/Enable", variable=disable_var, onvalue=True, offvalue=False)
    checkbox.grid(row=row, column=col * 4 + 2, sticky="w")
    disable_vars[category] = disable_var

# Add a text widget to display the prompt
prompt_display = tk.Text(root, height=10, width=80)
prompt_display.config(state=tk.DISABLED)
prompt_display.grid(row=len(categories)//2 + 1, columnspan=8)

# Add a frame to contain the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=len(categories)//2 + 2, columnspan=8)

# Add a button to randomize the prompt
generate_button = tk.Button(button_frame, text="Randomize", command=generate_prompt)
generate_button.pack(side=tk.LEFT, padx=10)

# Add a reset button
reset_button = tk.Button(button_frame, text="Reset", command=reset_defaults)
reset_button.pack(side=tk.LEFT, padx=10)

# Add a copy to clipboard button
copy_button = tk.Button(button_frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side=tk.LEFT, padx=10)

# Add dark theme toggle to dark
theme_button = tk.Button(button_frame, text="Change light/dark", command=theme_change)
theme_button.pack(side=tk.LEFT, padx=10)

# Start the GUI
root.mainloop()
