import summary
import experience
import tkinter as tk

fields = ('File Path')

def build_resume(event) -> str:
    path = E1.get()

    # Gather skill files
    adobe_file = open(f"{path}/Adobe_skills.txt", "r")
    adobe_skills = adobe_file.read()
    adobe_list = adobe_skills.split("\n")

    pcc_file = open(f"{path}/PCC_skills.txt", "r")
    pcc_skills = pcc_file.read()
    pcc_list = pcc_skills.split("\n")

    experience_section = experience.add_experience_bullets(adobe_list, pcc_list)
    summary_section = summary.generate_summary(f'{path}/summary.txt')
    # Write summary section to a file
    file = open(f"{path}/resume/summary.tex", "w")
    file.write(summary_section)
    file.close 

     #Write experience bullet points to file
    f = open(f"{path}/resume/experience.tex", "a")
    f.write(experience_section)
    f.close


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("400x100")
    L1 = tk.Label(root, text="File Path").pack()
    E1 = tk.Entry(root)
    E1.bind("<Return>", build_resume)
    E1.pack()
    root.mainloop()

  