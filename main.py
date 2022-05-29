if __name__ == "__main__":
    pass

import csv

class MenadzerPolaczen:
  def __init__(self, nazwa_pliku):
    self.filenaCme = nazwa_pliku
    self.data_dict = self.wczytaj_dane()


  def wczytaj_dane(self):
    calls_dict_sum = dict()
    with open(self.nazwa_pliku, 'r') as fin:
      reader = csv.reader(fin, delimiter= ",")
      headers = next(reader)

      for row in reader:
        from_subsr = int(row[0])
        if from_subsr not in calls_dict_sum:
          calls_dict_sum[from_subsr] = 0
        calls_dict_sum[from_subsr] += 1
    return calls_dict_sum

  def pobierz_najczesciej_dzwoniacego(self):
    return max(self.data_dict.items(), key= lambda x: x[1])


if __name__ == '__main__':
 print(MenadzerPolaczen(input()).pobierz_najczesciej_dzwoniacego())
