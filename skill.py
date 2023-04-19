# class Skill:
#   def __init__(self):
#     self.skill = ""

#   def set_skill(self, skill: str) -> str:
#     self.skill = skill

#   # Generates a skill listing in the correct format
#   def create_skill_entry(self):
#     return "\item" + " " + "{" + self.skill + "}"

# class Skills:
#   def __init__ (self):
#     self.skills = [Skill()]

#   def addSkill(self, skill: str) -> str:
#     new_skill = Skill()
#     new_skill.create_skill_entry(skill)
#     self.skills.append(new_skill)

#   # Generates a listing of all skills formatted for LaTex template
#   def generate_skills(self):
#     formatted_output = ""
#     for item in self.skills:
#       formatted_line = item.create_skill_entry
#       formatted_output = formatted_output + formatted_line + '\n'
#     return formatted_output

# generate summary given summary file
def generate_summary(file_name: str) -> str:
  summary_header = "%-------------------------------------------------------------------------------" + '\n' + "%	SECTION TITLE" + '\n' + "%-------------------------------------------------------------------------------" + '\n' + "\cvsection{Summary}""" + '\n' + r"%-------------------------------------------------------------------------------" + '\n' + "%	CONTENT" + '\n' + "%-------------------------------------------------------------------------------" + '\n' + r"\begin{cvparagraph}" + '\n' + "%---------------------------------------------------------" + '\n'
    
  summary_footer = "\end{cvparagraph}"
  try:
    file = open(file_name, "r")
    content = file.read()
  #  content_list = content.splitlines()
    file.close()
  except:
    print("The application could not open the file")
    
  if content:
    return summary_header + '\n' + content + '\n' + summary_footer
  else:
    return None
        


