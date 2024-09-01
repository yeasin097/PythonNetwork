import tkinter as tk

grade_conversion = {
    "A+": 4.00,
    "A": 3.75,
    "A-": 3.50,
    "B+": 3.25,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.25,
    "D": 2.00,
    "F": 0,
}

term_wise_credit_and_grade = {
    "11": 0,
    "12": 0,
    "21": 0,
    "22": 0,
    "31": 0,
    "32": 0,
    "41": 0,
    "42": 0,
}

term_wise_credit = {
    "11": 0,
    "12": 0,
    "21": 0,
    "22": 0,
    "31": 0,
    "32": 0,
    "41": 0,
    "42": 0,
}
    

def get_entry():
    try:
        result_txt = str(entry_result.get())
        line = result_txt.split()
        entries = len(line) // 10  # Ensure `entries` is an integer

        index_credit = 1
        index_level = 3
        index_term = 6
        index_grade = 8

        sum_of_credit_and_grade = 0
        sum_of_credit = 0

        while entries > 0:
            if index_credit >= len(line) or index_grade >= len(line):
                break

            credit = float(line[index_credit])
            grade = grade_conversion.get(line[index_grade], 0)

            level_term = int(line[index_level]) * 10 + int(line[index_term])

            # Update the indexes
            index_credit += 10
            index_grade += 10
            index_level += 10
            index_term += 10
            entries -= 1

            if grade == 0:
                continue

            sum_of_credit_and_grade += (credit * grade)
            sum_of_credit += credit

            term_wise_credit_and_grade[str(level_term)] += (credit * grade)
            term_wise_credit[str(level_term)] += credit

        # Display term-wise CGPA
        # print("Term wise CGPA")
        
        term_labels = []

        # Creating labels for each term
        for i in range(4):
            for j in range(2):
                label = tk.Label(window, text=f'')
                term_labels.append(label)

        i = 0
        j = 1
        k = 0

        for term in term_wise_credit:
            term_credit = term_wise_credit[term]
            if term_credit != 0:
                term_cgpa = round(term_wise_credit_and_grade[term] / term_credit, 2)
            else:
                term_cgpa = 0.00

            if( i%2 == 1):
                j = 2
            else:
                j = 1
                k += 1

            term_labels[i].config(text=f"Level {k} Term {j}: {term_cgpa}")
            i+=1

            
        for label in term_labels:
            label.pack(pady=5)


            

            
        # print(f"Level: {int(term) // 10} Term: {int(term) % 10} CGPA: {term_cgpa}")

        average_cgpa = round(sum_of_credit_and_grade / sum_of_credit, 2) if sum_of_credit > 0 else 0.00
        # print(f"Total Subjects Calculated, Average CGPA = {average_cgpa}")
        result_level.config(text=f"Average CGPA: {average_cgpa}")

    except Exception as e:
        result_level.config(text=f"Error: {str(e)}")


        

    except:
        result_level.config(text="Something goes wrong")


window = tk.Tk()

window.title("Calculate CGPA")

entry_result = tk.Entry(window, width=40)
entry_result.pack(pady=20)

calculate_button = tk.Button(window, text="Calculate", command=get_entry)
calculate_button.pack(pady=10)

result_level = tk.Label(window, text="CGPA: ")
result_level.pack(pady=10)





window.mainloop()