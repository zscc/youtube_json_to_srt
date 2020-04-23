import json
import pprint

def convert_time(time):
	millis = int(time)
	
	seconds = (millis/1000)%60
	seconds_int = int(seconds)

	minutes = (millis/(1000*60))%60
	minutes_int = int(minutes)

	hours = (millis/(1000*60*60))%24
	hours_int = int(hours)

	mil = millis - (seconds_int*1000 + minutes_int*60*1000 + hours_int*60*60*1000) 

	result = "%02d:%02d:%02d,%03d" % (hours, minutes, seconds, mil)
	print(result)
	
	return result

def write_to_srt(write_to_target, counter, \
	start_time_in_ms, duration_in_ms, text):
	start_time = convert_time(start_time_in_ms)
	end_time = convert_time(start_time_in_ms + duration_in_ms)
	#write_to_target.write(str(counter)+"\n"+str(start_time)+" --> " \
	#	+str(end_time)+"\n"+text+'\n')
	write_to_target.write(str(counter))
	write_to_target.write("\n")
	write_to_target.write(str(start_time))
	write_to_target.write(" --> ")
	write_to_target.write(str(end_time))
	write_to_target.write("\n")
	write_to_target.write(text + '\n\n')
	# write_to_target.write('\n')

def main():
	current_time = 0
	counter = 1
	with open('../input/7_part2_chinese.json', 'r') as f:
		sub_dict = json.load(f)

	write_to = open('../output/7_part2_chinese_v0.srt', 'w+')

	for i in sub_dict["events"]:
		tStartMs = i["tStartMs"]
		dDurationMs = i["dDurationMs"]
		text = i["segs"][0]["utf8"]
		write_to_srt(write_to, counter, tStartMs, dDurationMs, text)
		counter += 1


if __name__ == "__main__":
	# execute only if run as a script
	main()