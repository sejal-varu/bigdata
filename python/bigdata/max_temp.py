from glob import glob

dir_path = "/home/sejal/Documents/datascience/dataset/data/weather_data"
wildcard_path = dir_path + "/weather_data_set_*"

year_temp_map = {}
files = glob(wildcard_path)
for file in files:
	fobj = open(file, mode="r")
	for line in fobj:
		tokens = line.split("|")
		if (len(tokens) == 5):
			try:
				year = int(tokens[1])
				temp = float(tokens[4])
			except:
				pass
			else:
				if year in year_temp_map:
					temp_found = year_temp_map[year]
					if temp > temp_found:
						year_temp_map[year] = temp
				else:
					year_temp_map[year] = temp
			finally:
				pass
print (year_temp_map)
			