#pattern
import time
import os


BLACK_SQUARE = "\x1b[48;5;0m"   
WHITE_SQUARE = "\x1b[48;5;15m"  
END = "\x1b[0m"                 

def plot_square(color):
    
    print(f"{color}  {END}", end='')

def big_square():
    
    for row in range(3):
        for col in range(3):
            
            if (row == 1 and col == 1) or (row != 1 and col != 1):
                plot_square(WHITE_SQUARE)  
            else:
                plot_square(BLACK_SQUARE)  
        print()  

def main():
    frames = 0
    while True:
        big_square()  

        frames += 1
        if frames >= 3:
            os.system('cls' if os.name == 'nt' else 'clear')  
            frames = 0

        time.sleep(1)  

if __name__ == "__main__":
    main()

