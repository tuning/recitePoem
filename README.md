# recitePoem

- For parents who help kids recite and review poems:

	- Maintain a list of poems, number of reviews, last time a poem is reviewed, number of days since last review in a CSV file under "result" dir
	
	- Recommend poem titles for todays review:
	
		- the longer the period since last review, the more likely the title will be recommended
		
		- the less number of times the title is reviewed, the more likely the title will be recommended

- Manual:

	- To start, add poem titles to poemlist.txt under "data" dir. Sample text file is provided.
	
	- Adjust parameters such as the number of poems to review.
	
	- Run main script "poemSmart.py" to get recommendations for poem review. If your kid would like to learn a new poem, type 'y' and the title when prompted.
	
- Notes:

	-Currently supports UTF-8 only for Chinese characters.