import os
import glob


def concatenate_slides():
    # Initialize an empty string to store all content
    all_content = ""

    # Check if slides.md exists and read its content
    if os.path.exists("slides.md"):
        with open("slides.md", "r", encoding="utf-8") as file:
            all_content += file.read() + "\n\n"

    # Get all .md files in the ./slides directory
    slide_files = glob.glob("./slides/*.md")

    # Sort the files to maintain order
    slide_files.sort()

    # Read and concatenate content from each file
    for slide_file in slide_files:
        with open(slide_file, "r", encoding="utf-8") as file:
            all_content += f"\n\n# Content from {slide_file}\n\n"
            all_content += file.read()

    # Write the concatenated content to context.txt
    with open("context.txt", "w", encoding="utf-8") as output_file:
        output_file.write(all_content)

    print(
        f"Successfully concatenated content from slides.md and {len(slide_files)} slide files into context.txt"
    )


# Execute the function
concatenate_slides()
