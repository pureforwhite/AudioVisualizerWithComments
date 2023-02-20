import pygame
import pyaudio
import struct

# Define the screen size
screen_size = (640, 480)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(screen_size)

# Initialize Pyaudio
p = pyaudio.PyAudio()

# Open the audio file
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# Loop through the audio data and draw the visualization
while True:
    # Get the audio data from the stream
    data = stream.read(1024)
    # Convert the data to integers
    data_int = struct.unpack("<1024h", data)
    # Calculate the maximum amplitude of the data
    max_amplitude = max(data_int)
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw the visualization
    pygame.draw.line(screen, (255, 255, 255), (0, screen_size[1]//2), (screen_size[0], screen_size[1]//2))
    pygame.draw.line(screen, (255, 0, 0), (0, screen_size[1]//2), (max_amplitude*(screen_size[0]//2)//32767 + screen_size[0]//2, screen_size[1]//2), 3)
    # Update the screen
    pygame.display.update()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the program
            pygame.quit()
            stream.stop_stream()
            stream.close()
            p.terminate()
            quit()
