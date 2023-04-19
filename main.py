import skill
import summary
import experience

if __name__ == '__main__':
  summary_section = summary.generate_summary('summary.txt')
  experience_section = experience.add_experience_bullets() 

  # Write summary section to a file
  file = open("summary.tex", "w")
  file.write(summary_section)
  file.close

  #Write experience bullet points to file
  f = open("experience.tex", "a")
  f.write(experience_section)
  f.close
