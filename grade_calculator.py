# Student Grade Calculator

def get_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

def main():
    print("=== Student Grade Calculator ===")
    scores = []
    while True:
        score_input = input("Enter student score (or 'done' to finish): ")
        if score_input.lower() == 'done': break
        try:
            score = float(score_input)
            scores.append(score)
        except ValueError:
            print("Please enter a valid number")
    
    if scores:
        average = sum(scores) / len(scores)
        grade = get_grade(average)
        status = "PASS" if average >= 60 else "FAIL"
        print(f"\nAverage: {average:.2f} | Grade: {grade} | Status: {status}")

if __name__ == "__main__": main()
