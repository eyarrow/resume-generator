cv_entry_header = "%---------------------------------------------------------" + "\n" + "  \cventry" + "\n"
cv_entry_footer = "      \end{cvitems}" + "\n" + "    }" + "\n\n" "%---------------------------------------------------------" "\n"
cv_job1 = r"    {Technical Support Engineer II} % Job title" + "\n" + r"    {Adobe} % Organization" + "\n" + r"    {Portland, OR} % Location" + "\n" + "    {Jun. 2019 - Sep. 2021} % Date(s)" + "\n" + "    {" + "\n" + r"      \begin{cvitems} % Description(s) of tasks/responsibilities" + "\n"
cv_job2 = r"    {Systems Technician} % Job title" + "\n" + r"    {Portland Community College} % Organization" + "\n" + r"    {Portland, OR} % Location" + "\n" + "    {Mar. 2015 - Jun. 2019} % Date(s)" + "\n" + "    {" + "\n" + r"      \begin{cvitems} % Description(s) of tasks/responsibilities" + "\n"
cventries_footer = "\end{cventries}"
def return_formatted_skill(skill: str) -> str:
    return "        \item" + " " + r"{" + skill + "}" + "\n"

def return_formatted_bullets(skill_list: list) -> str:
    bullet_points = ""
    for item in skill_list:
        format_skill = return_formatted_skill(item)
        bullet_points = bullet_points + format_skill
    return bullet_points

def add_experience_bullets(job1: list, job2: list) -> str:
    experience_bullets_job1 = return_formatted_bullets(job1)
    experience_bullets_job2 = return_formatted_bullets(job2)
    output = cv_entry_header + cv_job1 + experience_bullets_job1 + cv_entry_footer + cv_entry_header + cv_job2 +  experience_bullets_job2 + cv_entry_footer + cventries_footer
    return output
    