import sys

for line in sys.stdin:
  parts = line.strip().split()
  for part in parts:
      print part + "\t1"
