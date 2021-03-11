# SummPip

**This code is for Sigir 2020 paper Unsupervised Multi-Document Summarizationwith Sentence Graph Compression**

**Python version**: this code is in Python3.6

## Dataset

[source data](https://drive.google.com/file/d/1_iDBecWsEkzuEou5-xi0z2ek3oJJ8CPB/view?usp=sharing) which has minimal text pre-processing

[target data](https://drive.google.com/file/d/1T9uE2sF3bN3a1T2KLp7mR4xK9MqqpkH1/view?usp=sharing) (for evaluation)

## Test SummPip on Multi-News

**Step1**: place downloaded dataset in the folder `./dataset/multi_news/`.

**Step2**: download the pre-trained [word2vec model](https://drive.google.com/file/d/1DVaktsGKbH8oPy28rrHuVgL_QVDsbfSA/view?usp=sharing) and place it in the folder `./word_vec/multi_news`. 

- If you want to run SummPip on your own dataset, you need to pre-train a W2V model yourself first with [gensim](https://radimrehurek.com/gensim/index.html).

**Step3**: Unsupervised Extractive Summarisation

```bash
python run_multinews.py
```

## Use SummPip on your dataset

Example of multiple documents, separated by "story_separator_special_tag" (example taken from truncated Multi_News dataset)

- You may want to change `-nb_clusters` and `-nb_words` to control the length of the output summary when applying SummPip on your own dataset. 

```python
from summarizer import SummPip

text = """
Atlanta ( CNN ) Sixteen US Postal Service workers got sentences of between three to nine years in federal prison for accepting bribes
to deliver cocaine on their routes in Atlanta . Drug traffickers bribed the postal workers , sometimes with amounts as low as $ 250 , 
to deliver drugs to designated addresses , the US Attorney 's Office said in a statement this week . " US Postal Service workers are 
typically valuable members of the community , entrusted to deliver the mail every day to our homes , " US Attorney Byung J. Pak said . 
" This important operation identified and prosecuted 16 corrupt individuals who chose to abuse that trust and instead used their 
positions to bring what they thought were large amounts of dangerous drugs into those same communities for a Operation discovered in 
2015 Federal agents learned about the operation in 2015 , while working to take down a drug trafficking organization in Atlanta . Drug 
traffickers targeted postal workers because their jobs made it less likely for them to be caught by law enforcement officials , federal 
authorities story_separator_special_tag ATLANTA – The last defendant of a group of 16 U.S. Postal Service letter carriers and clerks 
from across the Atlanta area was sentenced to federal prison for accepting bribes to deliver packages of cocaine – two kilograms or 
more at a time – in a wide - reaching undercover operation . The defendants were willing to make the deliveries for bribes as low as $ 
250 , and received sentences of between three and nine years in prison . “ U.S. Postal Service workers are typically valuable members 
of the community , entrusted to deliver the mail every day to our homes , ” said U.S. Attorney Byung J. “ BJay ” Pak . “ This important 
operation identified and prosecuted 16 corrupt individuals who chose to abuse that trust and instead used their positions to bring what 
they thought were large amounts of dangerous drugs into those same communities for a quick payoff . ” “ The FBI places a high priority 
on public corruption based investigations and we hope this sentencing will serve as a deterrent for others , ” said Chris 
story_separator_special_tag Sixteen U.S. Postal Services workers in metro Atlanta were sentenced to federal prison for accepting bribes 
, some as low as $ 250 , to deliver cocaine , The U.S. Attorney for the Northern District of Georgia said in a news release Tuesday . 
They each received sentences between three and nine years , federal officials said . Federal agents first learned of the crimes in 2015 
while investigating a drug trafficking organization in Atlanta , according to the release . Drug traffickers bribed the postal workers 
to deliver the drugs because they believed they were less likely to be caught by law enforcement officials . To catch the postal 
workers , federal agents posed as drug traffickers looking for postal employees delivering packages of cocaine in exchange for money 
while law enforcement officials recorded the interactions . ALSO|2 arrested in killing at DeKalb gas station MORE|Ex - employee wanted 
in suspected arson at downtown Decatur coffee shop Here is a list of metro Atlanta postal workers sentenced in the crime : Cydra 
Rochelle Alexander , 33 , of Riverdale , was a letter
"""
docs = [text]

pipe = SummPip(nb_clusters = 9, nb_words = 5)
src_list = pipe.split_sentences(docs)
summary_list = pipe.summarize(src_list)
print(summary_list[0])

"""
postal service letter carriers and clerks from across the atlanta area was sentenced to federal prison for accepting bribes to deliver 
packages of cocaine - two kilograms or more at a time - in a wide - reaching undercover operation . drug traffickers bribed 
the postal workers , federal officials said . postal services workers in metro atlanta were sentenced to federal prison for accepting 
bribes , some as low as $ 250 , to deliver cocaine , the u.s. attorney for the northern district of georgia said in a news release 
tuesday . drug traffickers targeted postal workers because their jobs made it less likely for them to be caught by law enforcement 
officials , federal authorities atlanta the last defendant of a group of 16 u.s. atlanta ( cnn ) sixteen us postal service 
workers got sentences of between three to nine years in federal prison for accepting bribes to deliver cocaine on their routes in 
atlanta . the defendants were willing to make the deliveries for bribes as low as $ 250 , and received sentences of between three and 
nine years in prison . " " the fbi places a high priority on public corruption based investigations and we hope this 
sentencing will serve as a deterrent for others , " said chris sixteen u.s. federal agents learned about the operation in 2015 , 
while working to take down a drug trafficking organization in atlanta . " this important operation identified and prosecuted 16 
corrupt individuals who chose to abuse that trust and instead used their positions to bring what they thought were large amounts of 
dangerous drugs into those same communities for a quick payoff .
"""

```


