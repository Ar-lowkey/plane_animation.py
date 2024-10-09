import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create the plane
plane = turtle.Turtle()
plane.shape("triangle")
plane.color("red")
plane.penup()

# Create the target circle
target = turtle.Turtle()
target.shape("circle")
target.color("green")
target.penup()
target.goto(100, 0)  # Set the circle's position

# Function to start dragging
def start_drag(x, y):
    plane.ondrag(drag_plane)

# Function to drag the plane
def drag_plane(x, y):
    plane.goto(x, y)

# Function to drop the plane and check for collision
def drop_plane(x, y):
    plane.ondrag(None)  # Disable dragging
    if plane.distance(target) < 20:  # Detect if dropped on the circle
        print("hello :}")
    plane.ondrag(drag_plane)  # Re-enable dragging

# Set up dragging events
plane.ondrag(drag_plane)  # Bind drag event to move plane
plane.ondrag(start_drag)  # Bind click event to start drag
screen.onscreenclick(drop_plane, 1)  # Drop plane on click

# Start the main loop to keep the window open
turtle.done()
