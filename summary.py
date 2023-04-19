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