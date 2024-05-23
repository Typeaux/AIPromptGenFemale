# Random Prompt Generator

This Python script generates random prompts by selecting items from predefined categories. Each category contains a list of items from which one is randomly chosen to create a prompt. The generated prompt is displayed in a graphical user interface (GUI) and can be copied to the clipboard for further use.

## How to Use

1. **Run the Script**: Execute the script using Python.
2. **Select Categories**: For each category, choose an item from the dropdown menu. You can also leave the dropdown blank to randomly select an item from that category. Additionally, you can disable a category by unchecking the "Disable/Enable" checkbox next to it. Disabled categories will be omitted from the prompt generation.
3. **Generate Prompt**: Click the "Generate" button to create a random prompt based on your selections.
4. **Copy Prompt**: Click the "Copy to Clipboard" button to copy the generated prompt to the clipboard.
5. **Reset Prompt**: Click the "Reset" button to reset the values of the dropdown boxes, the checkboxes, and the prompt output window, to their default state.
6. **Fill from Prompt**: Click the "Fill from Prompt" button to populate the dropdown menus based on the current prompt output. This allows you to tweak specific options while keeping the rest of the prompt unchanged.
7. **Save Preset**: Enter a name for your preset in the text entry box and click the "Save Preset" button to save the current configuration of dropdowns, checkboxes, and generated prompt.
8. **Load Preset**: Select a saved preset from the list and click the "Load Preset" button to load the configuration into the dropdowns and checkboxes.

   
## Features

-    Dropdown Menus: Allow you to choose specific items for each category.
-    Enable/Disable Checkboxes: Control whether a category is included in the prompt generation. If a category is disabled, it will be ignored when generating the prompt.
-    Random Prompt Generation: Randomly selects items from enabled categories to create a unique prompt.
-    Copy to Clipboard: Copies the generated prompt to the clipboard for easy use.
-    Reset: Resets the interface to default settings.
-    Fill from Prompt: Populates the dropdown menus based on the current prompt output for easy tweaking.
-    Save and Load Presets: Save and load custom configurations of dropdowns, checkboxes, and prompts.
 
    
## Categories

The script contains the following categories:

- **Occupation**: Various occupations ranging from conventional to futuristic.
- **Background**: Settings or environments for the character.
- **Background Color**: Different background colors or patterns.
- **Camera/View Angle**: Different angles or perspectives for viewing the scene.
- **Scene Lighting**: Various lighting conditions for the scene.
- **Age**: Different ages for the character.
- **Character Pose**: Different poses or positions for the character.
- **Hair Length**: Various lengths of hair for the character.
- **Hair Style**: Different styles or cuts of hair for the character.
- **Hair Color**: Different colors of hair for the character.
- **Eye Shape**: Different shapes of eyes for the character.
- **Eye Color**: Different colors of eyes for the character.
- **Face Shape**: Different shapes of the face for the character.
- **Nose Shape**: Different shapes of the nose for the character.
- **Lip Shape**: Different shapes of the lips for the character.
- **Lip Color**: Different colors of the lips for the character.
- **Lip Action**: Different actions or expressions of the lips for the character.
- **Skin Tone**: Different tones of skin for the character.
- **Body Type**: Different types of body shapes for the character.
- **Bust Size**: Different sizes of bust for the character.
- **Waist Size**: Different sizes of waist for the character.
- **Hip Size**: Different sizes of hips for the character.
- **Facial Expression**: Different facial expressions for the character.
- **Mood**: Different moods or emotions for the character.
- **Personality**: Different personality traits for the character.
- **Clothing Style**: Different styles of clothing for the character.
- **Clothing Color**: Different colors of clothing for the character.
- **Clothing Details**: Different details or embellishments on the clothing.
- **Clothing Accessories**: Different accessories worn by the character.

## Dependencies

- **Tkinter**: Python's standard GUI library.

## Acknowledgments

This script utilizes the Tkinter library for creating the graphical user interface.
