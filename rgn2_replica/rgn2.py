# Author: Eric Alcaide ( @hypnopump ) 
import os
import sys
import torch
import numpy as np

from rgn2_replica.utils import *


class AminoBERT(torch.nn.Module): 
    """ AminoBERT module providing high-quality embeddings for AAs. """
    def __init__(self, **kwargs): 
        return


class RGN2_LSTM_Naive(torch.nn.Module): 
    def __init__(self, layers, emb_dim=1280, hidden=[256, 128, 64], 
                 bidirectional=True, mlp_hidden=[32, 4]): 
        """ RGN2 module which turns embeddings into a Cα trace.
            Inputs: 
            * layers: int. number of rnn layers
            * emb_dim: int. number of dimensions in the input
            * hidden: int or list of ints. hidden dim at each layer
            * bidirectional: bool. whether to use bidirectional LSTM
        """
        super(RGN2_LSTM_Naive, self).__init__()
        hidden_eff = lambda x: x + x*int(bidirectional)
        # store params
        self.layers = layers
        self.hidden = [emb_dim]+hidden if isinstance(hidden, list) else \
                      [emb_dim] + [hidden]*layers
        self.bidirectional = bidirectional
        self.mlp_hidden = mlp_hidden
        # declare layers
        self.stacked_lstm = torch.nn.ModuleList([
            torch.nn.LSTM(input_size = hidden_eff(self.hidden[i]) if i!=0 else self.hidden[i],
                          hidden_size = self.hidden[i+1],
                          batch_first = True,
                          bidirectional = bidirectional,
                         ) for i in range(self.layers)
        ])
        self.last_mlp = torch.nn.Sequential(
            torch.nn.Linear(hidden_eff(self.hidden[-1]), self.mlp_hidden[0]),
            torch.nn.SiLU(),
            torch.nn.Linear(self.mlp_hidden[0], self.mlp_hidden[-1]) 
        )
    
    def forward(self, x): 
        """ Inputs: (..., Emb_dim) -> Outputs: (..., 4). 
			
			Note: 4 last dims of input is angles of previous point.
			      for first point, add dumb token [-5, -5, -5, -5]
        """
        for i,rnn_layer in enumerate(self.stacked_lstm): 
            x, (h_n, c_n) = rnn_layer(x)
        return self.last_mlp(x)

    def predict_fold(self, x):
    	""" Autoregressively generates the protein fold
    		Inputs: (L, Emb_dim) -> Outputs: (L, 4). 

    		Note: 4 last dims of input is dumb token for first res. 
    			  Use same as in `.forward()` method.
    	"""
    	preds_list = []
    	for i in range(x.shape[-2]):
    		if i == 0: 
    			input_step = x[i:i+1, :]
    		else: 
    			# add angle predicton from pred step to this one.
    			input_step = torch.cat([x[i:i+1, :-4], preds_list[-1][:, -4:]])

    		preds_list.append( self.forward(input_step) )

    	return torch.cat(preds_list, dim=-2) 
    	


class Refiner(torch.nn.Module): 
    """ Refines a protein structure by invoking several Rosetta scripts. """
    def __init__(self, **kwargs): 
        return



