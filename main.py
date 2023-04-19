import skill

if __name__ == '__main__':
  skill_section = skill.generate_summary('summary.txt')

file = open("skill_output.tex", "w")
file.write(skill_section)
file.close
