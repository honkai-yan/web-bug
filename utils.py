def tupleEquals(t1: tuple, t2:tuple) -> bool:
  if len(t1) != len(t2): return False
  for i in len(t1):
    if t1[i] != t2[i]: return False
  return True