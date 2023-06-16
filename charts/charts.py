import matplotlib.pyplot as plt 

def generate_pi_chart():
  labels = ['A', 'B', 'C']
  values = [200, 34,120]
  
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  plt.savefig('pie.png')
  plt.close()