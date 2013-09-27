import sys

scores_text = open(sys.argv[1])

dict_restaurant_score = {}

for line in scores_text: 
	list_retaurant_score = line.split(":")
	list_retaurant_score[1] = list_retaurant_score[1].strip()
	dict_restaurant_score[list_retaurant_score[0]] = list_retaurant_score[1]

list_to_sort = dict_restaurant_score.items()
sorted_list = sorted(list_to_sort)

for i in range(len(sorted_list)):
	print "Restaurant", sorted_list[i][0], "is rated at", sorted_list[i][1] + "." 
