#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:23:53 2020

@author: mingliu
"""

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
250 , and received sentences of between three and nine years in prison . 
"""
docs = [text]

pipe = SummPip(nb_clusters = 3, nb_words = 5)
src_list = pipe.split_sentences(docs)
summary_list = pipe.summarize(src_list)
print(summary_list[0])