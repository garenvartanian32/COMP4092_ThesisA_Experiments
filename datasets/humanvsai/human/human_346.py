def getEntropies(m):
  entropy = 0.0
  max_entropy = 0.0
  for module in m.children():
    e, m = getEntropies(module)
    entropy += e
    max_entropy += m
  e, m = getEntropy(m)
  entropy += e
  max_entropy += m
  return entropy, max_entropy