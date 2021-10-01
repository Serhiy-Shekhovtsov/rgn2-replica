# RGN2-Replica (WIP)

To eventually become an unofficial working Pytorch implementation of [RGN2](https://www.biorxiv.org/content/10.1101/2021.08.02.454840v1), an state of the art model for MSA-less Protein Folding for particular use when no evolutionary homologs are available (ie. for protein design). 

## Install

```bash
$ pip install rgn2-replica
```

## To load sample dataset


```
from datasets import load_from_disk
ds = load_from_disk("data/ur90_small")
print(ds['train'][0])
```
To convert to pandas for exploration
```
df = ds['train'].to_pandas()
df.sample(5)
```


## To train ProteinLM

Run the following command with default parameters

```bash
python -m scripts.lmtrainer
```
This will start the run using sample dataset in repo directory on CPU.


### TO-DO LIST: ordered by priority

* [x] ~~Provide basic package and file structure~~
* [ ] **RGN2**:
	* [x] ~~Contribute adaptation of RGN1 for different ops~~
		* [x] ~~Simple LSTM with:~~ 
		    * [x] ~~Inputs (B, L, emb_dim)~~
		    * [x] ~~Outputs (B, L, 4) (4 features which should be outputs of linear projections)~~
	* [x] ~~Find a good (and reproducible) training scheme~~ in collab w/ [@Serhiy-Shekhovtsov](https://github.com/Serhiy-Shekhovtsov)
	* [x] ~Benchmark regression vs classification of torsional alphabet~
* [ ] **Language Model**: 
	* [x] ~~basic tokenizer~~ by [@gurvindersingh](https://github.com/gurvindersingh)
	* [x] ~~basic architecture~~ by [@gurvindersingh](https://github.com/gurvindersingh)
	* [ ] adapt for desired outputs
	* [ ] find a combination of pretraining losses


* [ ] To be merged when first versions of RGN are ready: 
	* [x] ~~Geometry module~~ 
	* [x] ~~Adapt functionality from [MP-NeRF](https://github.com/EleutherAI/mp_nerf):~~
		* [x] ~~Sidechain building~~
		* [x] ~~Full backbone from CA~~
		* [x] ~~Fast loss functions and metrics~~
		* [x] ~~Modifications to convert LSTM cell into RGN cell~~

* [ ] Contirbute trainer classes / functionality. 
	* [ ] Sequence preprocessing for AminoBERT
		* [x] ~~inverted fragments~~
		* [x] ~~sequence masking~~
		* [x] ~~loss function wrapper v1~~ by [@Serhiy-Shekhovtsov](https://github.com/Serhiy-Shekhovtsov)
		* [x] ~~Sample dataset~~ by [@gurvindersingh](https://github.com/gurvindersingh)
		* [ ] Dataloder
		* [ ] ...

* [x] Contribute Data Infra for training: 
	* [x] Sequences: UniParc sequences, etc [@gurvindersingh](https://github.com/gurvindersingh)
	* [x] Structures: will use the amazing [sidechainnet](https://github.com/jonathanking/sidechainnet) work by Jonathan King  

* [x] ~Contribute Rosetta Scripts~ by [@jeffreyruffolo](https://github.com/jeffreyruffolo)

* **NOTES**: 
* Use functionality provided in [MP-NeRF](https://github.com/EleutherAI/mp_nerf) wherever possible (avoid repetition). 

## Contribute: 

Hey there! New ideas are welcome: open/close issues, fork the repo and share your code with a Pull Request. 

Currently the main discussions / conversation about the model development is happening [in this discord server](https://discord.gg/VpPpa9EZ) under the `/self-supervised-learning` channel.  

Clone this project to your computer:

`git clone https://github.com/EricAlcaide/rgn2-replica`

Please, follow [this guideline on open source contribtuion](https://numpy.org/devdocs/dev/index.html) 

## Citations:

```bibtex
@article {Chowdhury2021.08.02.454840,
    author = {Chowdhury, Ratul and Bouatta, Nazim and Biswas, Surojit and Rochereau, Charlotte and Church, George M. and Sorger, Peter K. and AlQuraishi, Mohammed},
    title = {Single-sequence protein structure prediction using language models from deep learning},
    elocation-id = {2021.08.02.454840},
    year = {2021},
    doi = {10.1101/2021.08.02.454840},
    publisher = {Cold Spring Harbor Laboratory},
    URL = {https://www.biorxiv.org/content/early/2021/08/04/2021.08.02.454840},
    eprint = {https://www.biorxiv.org/content/early/2021/08/04/2021.08.02.454840.full.pdf},
    journal = {bioRxiv}
}

@article{alquraishi_2019,
	author={AlQuraishi, Mohammed},
	title={End-to-End Differentiable Learning of Protein Structure},
	volume={8},
	DOI={10.1016/j.cels.2019.03.006},
	URL={https://www.cell.com/cell-systems/fulltext/S2405-4712(19)30076-6}
	number={4},
	journal={Cell Systems},
	year={2019},
	pages={292-301.e3}

```

