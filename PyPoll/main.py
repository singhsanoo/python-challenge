from distutils import text_file
import os
import csv

file_path = os.path.join('.', 'Resources', 'election_data.csv')
num_votes = 0
vote_count_dict = {}

with open (file_path,'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')

    #skip header
    header = next(data)

    for row in data:
        num_votes += 1

        if row[2] not in vote_count_dict:
            vote_count_dict.update({row[2] : 0})
        
        vote_count_dict[row[2]] += 1

#creating list of candidates from the dictonary    
candidate_list = [*vote_count_dict]

#getting name of the candidate with highest(max) vote 
winner = max(vote_count_dict, key=vote_count_dict.get)


#printing header
result_header = f"""Election Results
{'-' * 30}
Total Votes: {num_votes}
{'-' * 30}"""
print(result_header)

#printing vote summary
for key in vote_count_dict:
    #calculating percetage of vote received by each candidates and rounding it to 3 decimals
    percent_of_vote = round(vote_count_dict[key]/num_votes * 100, 3)
    print (f"{key} : {percent_of_vote}% ({vote_count_dict[key]})")
    
#printing footer and winner
result_footer = f"""{'-' * 30}
Winner: {winner}
{'-' * 30}"""

print(result_footer)

#Write Output to the text file
output_path = os.path.join(".", "analysis", "result.txt")
with open (output_path, 'w') as textfile:
    textfile.write(result_header)

        #writing vote summary
    for key in vote_count_dict:
        percent_of_vote = round(vote_count_dict[key]/num_votes * 100, 3)
        textfile.write (f'\n{key} : {percent_of_vote}% ({vote_count_dict[key]})')

        #writing footer and winner
    textfile.write(f'\n{result_footer}')





