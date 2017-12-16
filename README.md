# CoNLL-U_cycles
## Summary
CoNLL-U_cycles takes a [CoNLL-U](http://universaldependencies.org/format.html) file and determines 
if there are cycles in a dependency tree. This script catches cyclic arcs as errors. CoNLL-U is often the output of NLP
tasks.
## Prerequisites
* [Python 3.6](https://www.python.org/)
* [CoNLL-U Parser](https://github.com/EmilStenstrom/conllu) parses 
a [CoNLL-U formatted](http://universaldependencies.org/format.html) file.
## Usage
    python main.py <CoNLL-U file>
## Example Cases:
Here presents the example cases provided with the scripts.
### Cycle not Present
Take a look at a test case without a cycle: [CoNLL-U sans cycle](conllu_sans_cycle.txt)
###
    cat conllu_sans_cycle.txt
    1    They     they    PRON    PRP    Case=Nom|Number=Plur               2    nsubj    2:nsubj|4:nsubj
    2    buy      buy     VERB    VBP    Number=Plur|Person=3|Tense=Pres    0    root     0:root
    3    and      and     CONJ    CC     _                                  4    cc       4:cc
    4    sell     sell    VERB    VBP    Number=Plur|Person=3|Tense=Pres    2    conj     0:root|2:conj
    5    books    book    NOUN    NNS    Number=Plur                        2    obj      2:obj|4:obj
    6    .        .       PUNCT   .      _                                  2    punct    2:punct
    
    python main.py conllu_sans_cycle.txt
    No cycles found.
Take a look at a test case with a cycle: [CoNLL-U con cycle](conllu_con_cycle.txt).
###
    cat 
## Authors
* Allen Mao (Google Code-In 2017)
## License
This project is licensed under the MIT License - see the [License](LICENSE)

