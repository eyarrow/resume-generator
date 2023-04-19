cv_entry_header = "%---------------------------------------------------------" + "\n" + "  \cventry" + "\n"
cv_entry_footer = "      \end{cvitems}" + "\n" + "    }" + "\n\n" "%---------------------------------------------------------" "\n"
cv_job1 = r"    {Technical Support Engineer II} % Job title" + "\n" + r"    {Adobe} % Organization" + "\n" + r"    {Portland, OR} % Location" + "\n" + "    {Jun. 2019 - Sep. 2022} % Date(s)" + "\n" + "    {" + "\n" + r"      \begin{cvitems} % Description(s) of tasks/responsibilities" + "\n"
cv_job2 = r"    {Systems Technician} % Job title" + "\n" + r"    {Portland Community College} % Organization" + "\n" + r"    {Portland, OR} % Location" + "\n" + "    {Mar. 2015 - Jun. 2019} % Date(s)" + "\n" + "    {" + "\n" + r"      \begin{cvitems} % Description(s) of tasks/responsibilities" + "\n"

def add_experience_bullets():
    output = cv_entry_header + cv_job1 + cv_entry_footer + cv_job2 + cv_entry_footer
    return output
    