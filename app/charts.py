import matplotlib.pyplot as plot


def generate_bar_chart(name, labels, values):
  fig, ax = plot.subplots()
  ax.bar(labels, values)
  plot.savefig(f'./img/{name}_bar.png')
  plot.close()


def generate_py_chart(labels, values):
  fig, ax = plot.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plot.savefig('pie.png')
  plot.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 400, 30]
  # generate_bar_chart(labels, values)
  generate_py_chart(labels, values)
