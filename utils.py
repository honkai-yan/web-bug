def tupleEquals(t1: tuple, t2:tuple) -> bool:
  if len(t1) != len(t2): return False
  i = 0
  for item in t1:
    if item != t2[i]:
      return False
    i += 1
  return True