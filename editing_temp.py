import tempfile
import os
from subprocess import call

# Get the text editor from the shell, otherwise default to Vim
EDITOR = os.environ.get('EDITOR','vim')

# Set initial input with which to populate the buffer
initial_message = "Hello world!"

# Open a temporary file to communicate through (`tempfile` should avoid any filename conflicts)
#
# NOTE: Don't autodelete the file on close!
#       We want to reopen the file incase the editor uses a swap-file.
#


def enable_editing_manually(primary_content):
	with tempfile.NamedTemporaryFile(suffix=".tmp", delete=False,mode = "w+") as tf:

    # Write the initial content to the file I/O buffer
		tf.write("you can edit here  \n   " + primary_content)

    # Flush the I/O buffer to make sure the data is written to the file
		tf.flush()

    # Open the file with the text editor
		call([EDITOR, tf.name])
		edited_content = tf.read()
		print("function runned")
		print(edited_content)
		return edited_content

#with open(tf.name, 'r') as tf:

    # Read the file data into a variable
    #edited_message = tf.read()

    # Output the dataih
    #print(edited_message)


!vim filename