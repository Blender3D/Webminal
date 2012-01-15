import threading, subprocess

class Terminal(threading.Thread):
  def __init__(self):
    super(Terminal, self).__init__()
    
    self.process = None
  
  def run(self):
    print ' * Starting ShellInABox'
    self.process = subprocess.Popen(
      'shellinaboxd -s /:LOGIN --disable-ssl --css static/shellinabox.css', 
      stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT,
      shell=True
    )
