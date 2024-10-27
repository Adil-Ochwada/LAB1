#flag
BLUE = '\u001b[44m'  
WHITE = '\u001b[47m' 
RED = '\u001b[41m'   
RESET = '\u001b[0m'  

def drawer(color, length=1):
    print(color + " " * length + RESET, end='')


def draw_french_flag(height, width):
    
    stripe_width = width // 3

    for h in range(height):
        for w in range(width):
            if w < stripe_width:          
                drawer(BLUE)
            elif w < 2 * stripe_width:      
                drawer(WHITE)
            else:                           
                drawer(RED)

        print()  

def main():
    height = 11  
    width = 51   
    draw_french_flag(height, width)

if __name__ == "__main__":  
    main()

#graph
def draw_parabola():
    for y in range(10, -11, -1):  
        for x in range(-10, 11, 1):  
            if x == 0 and y == 0:
                print('+', end=' ')  # Origin
            elif x == 0:
                print('|', end=' ')  # Y-axis
            elif y == 0:
                print('-', end=' ')  # X-axis
            elif y == x ** 2:
                print('*', end=' ')  
            else:
                print(' ', end=' ')  
        print()


draw_parabola()

#percentage
BLUE = '\u001b[44m'
RESET = '\u001b[0m'

def drawer(percentage):
    print(BLUE + " " * int(percentage) + RESET, f"{percentage:.2f}%")

def percentage_diagram(sequence):
    
    conditions = [("< 0", lambda x: x < 0), ("> 0", lambda x: x > 0)]
    condition_counts = {label: 0 for label, _ in conditions}

    try:
        with open(sequence, 'r') as file:
            data = list(map(float, file.read().split()))
    except FileNotFoundError:
        print("File not found. Make sure 'sequence.txt' is in the directory.")
        return
    if not data:
        print("No data in file.")
        return

    
    for value in data:
        for label, condition in conditions:
            if condition(value):
                condition_counts[label] += 1
                break

    print("Percentage Diagram for Numbers Less and Greater than Zero:")
    Numbers = len(data)
    for label, count in condition_counts.items():
        percentage = (count / Numbers) * 100
        print(f"{label}: ", end='')
        drawer(percentage)

if __name__ == "__main__":
    percentage_diagram("sequence.txt")

