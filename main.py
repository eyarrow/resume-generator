import skill
import summary
import experience

if __name__ == '__main__':
  summary_section = summary.generate_summary('summary.txt')

  # Gather skills
  adobe_file = open("Adobe_skills.txt", "r")
  adobe_skills = adobe_file.read()
  adobe_list = adobe_skills.split("\n")
  
  pcc_file = open("PCC_skills.txt", "r")
  pcc_skills = pcc_file.read()
  pcc_list = pcc_skills.split("\n")


  experience_section = experience.add_experience_bullets(adobe_list, pcc_list) 

  # Write summary section to a file
  file = open("summary.tex", "w")
  file.write(summary_section)
  file.close

  #Write experience bullet points to file
  f = open("experience.tex", "a")
  f.write(experience_section)
  f.close
