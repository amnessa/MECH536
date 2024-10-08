import numpy as np

# Çağdaş Güven 2738938

# if you have used AI tools, add your prompt, level of satisfaction with the result, pros and cons etc as a comment here... if done it the good old way, say so.

# just submit this function in a file that is named as Shapes_studentID.py and in your implementations 
# before you submit make sure the STUDENTID is replaced with yours
# your python file should only have the following two functions, 
# and if you have written support functions, they should be included as well so that I can test it
# ABSOLUTELY NO TEST CODE OR ANYTHING ELSE SHOULD BE in your FIL
# GET THE HABIT OF TESTING YOUR CODE BY IMPORTING IT IN A SEPERATE FILE
# DO NOT print anything in your functions. If you do so in testing, get rid of them before submission.

# note that your code should not crash! for example if by accident r=-5, your code should work, its your preference how to handle wrong inputs, 
# but best way in assignments it either to raise an exception or leaving variables with their default values if the user passed values do not make sense.



# I have tested generating this code on Gemini and I got raw version where no exception handling existed.
# Then I tried Chatgpt (freeversion) and without any input from user ChatGpt implemented exception handling but used assert method which crashes the program
# So I handled the exception, and got help from AI for square function

def Square_2738938(M=np.array([3, 4]), N=100):
    """
    Generates N many random points on a square's boundary.

    Args:
      M: A numpy array representing the coordinates of the opposite corner 
         from the origin (0, 0) of the square.
      N: The total number of points to generate.

    Returns:
      A numpy array of shape (2, N) containing the coordinates of the generated points.
    """
    
    try:
        # Validate inputs
        if not isinstance(M, np.ndarray) or M.shape != (2,):
            raise ValueError("M should be a 2-element numpy array representing [x, y] coordinates.")
        
        if not isinstance(N, int) or N <= 0:
            raise ValueError("N should be a positive integer.")

        # Calculate how many points should be generated on each side
        points_per_side = N // 4
        remainder = N % 4
        
        # Generate points for each edge
        left_edge = np.vstack([np.zeros(points_per_side), np.random.uniform(0, M[1], points_per_side)])
        right_edge = np.vstack([np.full(points_per_side, M[0]), np.random.uniform(0, M[1], points_per_side)])
        bottom_edge = np.vstack([np.random.uniform(0, M[0], points_per_side), np.zeros(points_per_side)])
        top_edge = np.vstack([np.random.uniform(0, M[0], points_per_side), np.full(points_per_side, M[1])])
        
        # Handle any remaining points due to rounding
        remaining_points = []
        for _ in range(remainder):
            side = np.random.choice(["left", "right", "bottom", "top"])
            if side == "left":
                remaining_points.append([0, np.random.uniform(0, M[1])])
            elif side == "right":
                remaining_points.append([M[0], np.random.uniform(0, M[1])])
            elif side == "bottom":
                remaining_points.append([np.random.uniform(0, M[0]), 0])
            elif side == "top":
                remaining_points.append([np.random.uniform(0, M[0]), M[1]])
        
        # Combine all points
        D = np.hstack((left_edge, right_edge, bottom_edge, top_edge))
        if remaining_points:
            remaining_points = np.array(remaining_points).T
            D = np.hstack((D, remaining_points))

        return D

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None  # Return None or some default value

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None  # Return None or some default value





def Circle_2738938(r=13, C=np.array([5, 12]), N=250, n=0.0):
    """
    Generates N many random points on a circle's boundary.

    Args:
      r: The radius of the circle.
      C: A numpy array representing the coordinates of the center [x, y].
      N: The total number of points to generate.
      n: The noise level.

    Returns:
      A numpy array of shape (2, N) containing the coordinates of the generated points.
    """

    try:
      if r <= 0:
          raise ValueError("Radius should be a positive number.")
      if len(C) != 2:
          raise ValueError("C should be a 2-element numpy array representing [x, y] coordinates.")
      if N <= 0:
          raise ValueError("N should be a positive integer.")
      if n < 0:
          raise ValueError("Noise level should be non-negative.")
    except ValueError as e:
      print(f"Invalid input: {e}")
      return None  # Return None to indicate an issue with inputs
  
    # Continue with the circle generation if inputs are valid
    angles = np.random.uniform(0, 2 * np.pi, N)
    x_coords = r * np.cos(angles) + C[0]
    y_coords = r * np.sin(angles) + C[1]
    D = np.vstack((x_coords, y_coords))
    
    if n != 0:
        noise = np.random.rand(2, N) * n
        D = D + noise

    return D
