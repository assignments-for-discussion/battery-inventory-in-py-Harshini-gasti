
def count_batteries_by_usage(cycles):
  return {
    "lowCount": 0,
    "mediumCount": 0,
    "highCount": 0
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
#   assert(counts["lowCount"] == 2)
#   assert(counts["mediumCount"] == 3)
#   assert(counts["highCount"] == 1)
for i in counts:
  if(counts[i]<400):
    lowcount++
  else if(counts[i]>400&&count[i]<900):
    mediumcount++
  else(counts[i]>900):
    highcount++
    print("lowcount is :",lowcount)
    print("mediumcount is :",mediumcount)
    print("highcount is :",highcount)
  print("Done counting :)")
  
  


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
