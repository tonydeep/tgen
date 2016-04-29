#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

config = {
          'alpha': 1e-3,
          'randomize': True,
          'num_hidden_units': 128,
          'emb_size': 50,
          'batch_size': 20,
          'optimizer_type': 'adam',
          'max_cores': 4,
          'use_tokens': True,
          'nn_type': 'emb_attention_seq2seq',
          'sort_da_emb': True,
          'cell_type': 'lstm',
          'dropout_keep_prob': 1,
          'use_dec_cost': False,
          #'average_models': True,
          #'average_models_top_k': 3,

          'validation_size': 100,
          'validation_freq': 1,
          'passes': 1000,
          'min_passes': 100,
          'improve_interval': 50,
          'top_k': 10,
          'bleu_validation_weight': 1,
          'beam_size': 1, # 20,
          'sample_top_k': 1,
          'length_normalized_decoding': False,
          'alpha_decay': 0, # 0.03

          #'classif_filter': {
              #'language': 'en',
              #'selector': '',
              ##'nn': '1-hot',
              #'nn': 'emb',
              ##'nn_shape': 'ff1',
              #'nn_shape': 'rnn',
              #'num_hidden_units': 128,
              ##'passes': 200,
              #'passes': 100,
              #'min_passes': 20,
              #'randomize': True,
              #'batch_size': 20,
              #'alpha': 1e-3,
              #'emb_size': 50,
              #'max_tree_len': 50,
              #'validation_freq': 1,
              #}
          }
